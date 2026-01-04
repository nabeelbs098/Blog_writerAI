import streamlit as st
from crew import BlogCrew
import sys
import io

# 1. Page Config
st.set_page_config(
    page_title="ContentCrew AI",
    page_icon=" ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS (Cleaner look)
st.markdown("""
<style>
    .stAppHeader {background-color: transparent;}
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2065/2065064.png", width=80)
    st.title("ContentCrew")
    
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
    run_btn = st.button("🚀 Launch Crew", type="primary")

# 4. Main Content Area
st.title(" AI Blog Writing Studio")

# 5. Output Handler (Modified to be invisible)
class StreamlitOutputStream(io.StringIO):
    def __init__(self, status_container):
        super().__init__()
        self.status_container = status_container

    def write(self, s):
        # We only look for keywords to update the status spinner
        # We DO NOT print the raw text to the screen anymore
        if "Researcher" in s:
            self.status_container.update(label="Researcher is finding facts...", state="running")
        elif "Writer" in s:
            self.status_container.update(label="Writer is drafting content...", state="running")
        elif "Editor" in s:
            self.status_container.update(label="Editor is refining the text...", state="running")

# 6. Execution Logic
if run_btn and topic:
    # Use a status container for the "thinking" animation
    with st.status("🚀 Initializing Agents...", expanded=True) as status:
        
        # Redirect stdout to our cleaner handler
        sys.stdout = StreamlitOutputStream(status)
        
        try:
            inputs = {
                'topic': topic, 
                'tone': tone,
                'audience': audience
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