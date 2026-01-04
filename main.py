import streamlit as st
from crew import BlogCrew
import sys
import io

st.set_page_config(
    page_title="ContentCrew AI",
    page_icon=" ",
    layout="wide"
)

st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 50px;
        font-weight: bold;
        background-color: #00AA00; /* Green accent */
        color: white;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

st.title("AI Blog Writing Studio")
st.markdown("Generate high-quality, researched blog posts with a multi-agent AI team.")
st.divider()

st.subheader("1. Define Your Content")

topic = st.text_area(
    "What should we write about?",
    placeholder="E.g., The Future of Quantum Computing in 2026",
    height=80,
    label_visibility="collapsed"
)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    tone = st.selectbox("Tone", ["Professional", "Witty", "Academic", "Persuasive"])
with col2:
    audience = st.selectbox("Audience", ["Tech Savvy", "General Public", "Investors"])
with col3:
    st.write("") 
    st.write("")
    run_btn = st.button("Start...", type="primary")

st.divider()

class StreamlitOutputStream(io.StringIO):
    def __init__(self, status_container):
        super().__init__()
        self.status_container = status_container

    def write(self, s):
        if "Researcher" in s:
            self.status_container.update(label="Researcher is finding facts...", state="running")
        elif "Writer" in s:
            self.status_container.update(label="Writer is drafting content...", state="running")
        elif "Editor" in s:
            self.status_container.update(label="Editor is refining the text...", state="running")

if run_btn and topic:

    with st.status("Initializing Agents...", expanded=True) as status:
        
        sys.stdout = StreamlitOutputStream(status)
        
        try:
            inputs = {'topic': topic, 'tone': tone, 'audience': audience}
            result = BlogCrew().crew().kickoff(inputs=inputs)
            status.update(label="Blog Post Generated!", state="complete", expanded=False)
            
        except Exception as e:
            status.update(label="An Error Occurred", state="error")
            st.error(f"Error: {e}")
            st.stop()

    st.markdown("### Your Generated Blog Post")
    st.markdown(result)

    st.download_button(
        label="Download as Markdown",
        data=str(result),
        file_name="blog_post.md",
        mime="text/markdown"
    )

elif run_btn and not topic:
    st.warning("Please enter a topic to start.")