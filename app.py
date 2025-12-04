import streamlit as st
from crewai import Crew, Process
from agents import researcher, writer
from tasks import research_task, write_task

# 1. CONFIGURATION
st.set_page_config(
    page_title="Agentic Research Pro", 
    page_icon="🤖",
    # Removed layout="wide" to ensure text doesn't stretch too thin
    initial_sidebar_state="collapsed"
)

# 2. CUSTOM CSS
st.markdown("""
<style>
    #MainMenu {visibility: visible;} 
    footer {visibility: hidden;}
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #0E1117;
        color: #FAFAFA;
        text-align: center;
        padding: 10px;
        border-top: 1px solid #333;
        z-index: 1000;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. HEADER
st.title("🤖 Agentic Research Pro")
st.caption("Powered by **Gemini 2.5 Grounding** & **CrewAI**")

# 4. INPUT AREA
st.markdown("---")
col_input, col_btn = st.columns([4, 1])

with col_input:
    topic = st.text_input("Enter Research Topic:", placeholder="e.g. Solid State Batteries, Agentic AI")

with col_btn:
    st.markdown("##") 
    run_btn = st.button("🚀 Launch Agent", type="primary", use_container_width=True)

# 5. EXECUTION LOGIC
if run_btn:
    if not topic:
        st.toast("❌ Please enter a topic first!", icon="⚠️")
    else:
        status_text = st.empty()
        status_text.info("🔄 Initializing Agents...")
        
        try:
            with st.spinner('Agents are searching Google & synthesizing data...'):
                tech_crew = Crew(
                    agents=[researcher, writer],
                    tasks=[research_task, write_task],
                    process=Process.sequential
                )
                result = tech_crew.kickoff(inputs={'topic': topic})
            
            status_text.empty()
            st.toast("Report Generation Complete!", icon="✅")
            
            with st.container():
                st.markdown("### 📑 Research Findings")
                # Using st.markdown to render the tables correctly
                st.markdown(result)
                
            st.markdown("---")
            st.download_button(
                label="📥 Download Briefing",
                data=str(result),
                file_name=f"{topic}_briefing.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 6. FOOTER
st.markdown(
    """
    <div class="footer">
        <p>Built for <b>Hack Imagine 2025</b> | Powered by Gemini 2.5 Flash | Zero-Cost Architecture</p>
    </div>
    """,
    unsafe_allow_html=True
)