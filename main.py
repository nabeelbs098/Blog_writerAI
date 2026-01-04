import streamlit as st
from crew import BlogCrew
import sys
import io
import time

# 1. Page Config (Must be the first line)
st.set_page_config(
    page_title="ContentCrew AI",
    page_icon="✍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS to hide clutter and style buttons
st.markdown("""
<style>
    /* Main Background adjustments */
    .stAppHeader {background-color: transparent;}
    
    /* Style the main button */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
    }
    
    /* Custom container for the output */
    .output-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #d1d5db;
    }
    
    /* Dark mode adjustments (optional, usually Streamlit handles this) */
    @media (prefers-color-scheme: dark) {
        .output-container {
            background-color: #262730;
            border-color: #41434e;
        }
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2065/2065064.png", width=80)
    st.title("ContentCrew Settings")
    
    st.markdown("### 1. Topic Definition")
    topic = st.text_area(
        "What should we write about?",
        placeholder="E.g., The Future of Quantum Computing in 2026",
        height=100
    )
    
    st.markdown("### 2. Style & Tone")
    col1, col2 = st.columns(2)
    with col1:
        tone = st.selectbox("Tone", ["Professional", "Witty", "Academic", "Persuasive"])
    with col2:
        audience = st.selectbox("Audience", ["Tech Savvy", "General Public", "Investors"])
        
    st.divider()
    
    # Big Main Button
    run_btn = st.button("🚀 Launch Crew", type="primary")
    
    st.markdown("---")
    st.caption("Powered by CrewAI & Groq")

# 4. Main Content Area
st.title("✍️ AI Blog Writing Studio")
st.markdown("Generate high-quality, researched blog posts with a multi-agent AI team.")

# 5. Output Capture Class
class StreamlitOutputStream(io.StringIO):
    def __init__(self, placeholder, status_container):
        super().__init__()
        self.placeholder = placeholder
        self.status_container = status_container
        self.buffer = ""

    def write(self, s):
        self.buffer += s
        # Only update periodically to save performance, or update status label
        if "Researcher" in s:
            self.status_container.update(label="🕵️ Researcher is finding facts...", state="running")
        elif "Writer" in s:
            self.status_container.update(label="✍️ Writer is drafting content...", state="running")
        elif "Editor" in s:
            self.status_container.update(label="🧐 Editor is refining the text...", state="running")
            
        self.placeholder.code(self.buffer[-2000:], language="text")

# 6. Execution Logic
if run_btn and topic:
    # Create two tabs: One for the clean result, one for the raw logs
    tab1, tab2 = st.tabs(["📄 Final Article", "⚙️ Agent Workflows"])
    
    with tab2:
        st.subheader("Live Agent Activity")
        log_placeholder = st.empty()
    
    with tab1:
        # The "Status" container creates a nice expandable box
        with st.status("🚀 Initializing Agents...", expanded=True) as status:
            
            # Redirect stdout
            sys.stdout = StreamlitOutputStream(log_placeholder, status)
            
            try:
                inputs = {
                    'topic': topic, 
                    'tone': tone,
                    'audience': audience # Note: Ensure you add {audience} to your tasks.yaml if you want to use it!
                }
                
                # Run the Crew
                result = BlogCrew().crew().kickoff(inputs=inputs)
                
                # Success State
                status.update(label="✅ Blog Post Generated Successfully!", state="complete", expanded=False)
                
            except Exception as e:
                status.update(label="❌ An Error Occurred", state="error")
                st.error(f"Error: {e}")
                st.stop()

    # Display Result
    st.markdown("### Your Generated Blog Post")
    st.markdown("---")
    st.markdown(result)
    
    # Download Button
    st.download_button(
        label="📥 Download as Markdown",
        data=str(result),
        file_name="blog_post.md",
        mime="text/markdown"
    )

elif run_btn and not topic:
    st.warning("⚠️ Please enter a topic to start.")