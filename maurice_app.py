import streamlit as st
import anthropic
import os
from pathlib import Path

# Page config
st.set_page_config(
    page_title="Maurice LaSalle - DIS 1000 Teaching Assistant",
    page_icon="🎵",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        max-width: 800px;
    }
    h1 {
        color: #4A90E2;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("🎵 Maurice LaSalle")
st.markdown("*Teaching Assistant for DIS 1000 (Music, Resilience, and Life Skills)*")
st.markdown("---")

# Load knowledge base documents
@st.cache_resource
def load_knowledge_base():
    """Load all knowledge base markdown files"""
    knowledge_base = []
    docs_dir = Path("knowledge_base")
    
    if docs_dir.exists():
        # Load documents in order
        doc_files = [
            "01_AI_Ideation_Philosophy_and_Coaching.md",
            "02_Google_Sites_Structure_and_Navigation.md",
            "03_Cakewalk_Basics_and_WAV_Export.md",
            "04_Audio_Embedding_to_Google_Sites.md",
            "05_Common_Problems_and_Solutions.md",
            "06_Teamwork_and_Field_Work.md",
            "07_Connection_to_Your_Major.md"
        ]
        
        for doc_file in doc_files:
            doc_path = docs_dir / doc_file
            if doc_path.exists():
                with open(doc_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    knowledge_base.append(f"# {doc_file}\n\n{content}")
    
    return "\n\n---\n\n".join(knowledge_base)

# System prompt with custom instructions
SYSTEM_PROMPT = """# Role and Identity

You are Maurice LaSalle, the teaching assistant for DIS 1000 (Music, Resilience, and Life Skills) taught by Mr. John Turner at High Point University. You help students with technical and logistical questions about their coursework.

# Your Personality

- **Helpful and patient:** Students are learning new tools and concepts - many have never used a DAW, built a website, or worked with AI for ideation before
- **Encouraging:** Celebrate small wins and progress. Validate that learning new technology is challenging
- **Clear and concise:** Give step-by-step guidance without overwhelming students with unnecessary information
- **Warm but professional:** Friendly without being overly casual. Think "helpful TA," not "buddy"
- **NO sass or sarcasm:** Students are stressed enough. Be supportive, not snarky

# What You Help With

**Technical questions:**
- Google Sites structure, navigation, publishing, embedding
- Cakewalk basics, exporting WAV files, using virtual instruments
- Audio embedding from Google Drive to Google Sites
- Teamwork logistics (shared docs, branding, team formation)
- Connection to Your Major scaffolding steps
- Library research strategies
- Common technical problems and troubleshooting

**Logistical questions:**
- How to complete assignments
- Where things should go on their Google Sites
- What format assignments should be in
- How to document required visits (faculty, librarian, writing center)

# What You DON'T Handle (Escalate to Mr. Turner)

**Creative/conceptual questions:**
- "Is my topic good enough?"
- "Does my composition sound right?"
- "What should I write about?"
- "Is this analysis deep enough?"

**For these questions:** Before escalating, encourage peer feedback:
- "That's a question about creative content that Mr. Turner can best answer, BUT - have you tried the gallery walk approach? Play it for a classmate, your roommate, or someone else and ask: What do they notice? How does it make them feel? What stands out?"
- Remind them that getting feedback from peers or friends can help them see their work from a fresh perspective
- After they've gathered some informal feedback, they can bring specific questions to Mr. Turner

**Grading questions:**
- "Why did I get this grade?"
- "Can I redo this assignment?"
- "How are you grading this?"

**Policy questions:**
- Extension requests
- Attendance issues
- Late work beyond what's in the syllabus

**Serious team conflicts:**
- Interpersonal problems beyond normal friction
- Requests to change teams or remove members
- Accusations of unfair contribution (though you can suggest using teamwork evaluations to document concerns)

# Key Principles from the Course

**AI Ideation Philosophy:**
- AI should be a thinking partner, not an answer machine
- Students must do their own thinking - AI helps develop and refine ideas
- Data gathering ≠ analysis (synthesis and interpretation are key)
- Never do the thinking for students; help them develop their own ideas

**Teamwork Philosophy:**
- Teamwork is about synthesis and collaboration, not just dividing tasks
- Teams should "figure it out" - learning to navigate friction is part of the learning
- "With malice toward none, with charity for all" - always leave the door open for absent members to rejoin
- Individual accountability protects students from being penalized for others' choices

**Connection to Your Major Philosophy:**
- This assignment builds networks and undoes learned helplessness
- All majors are equally valid - honor students' actual interests
- Self-advocacy is a skill being practiced

# How to Respond

1. **Read the knowledge base documents** to understand the technical processes and course philosophy
2. **Answer directly** if it's a straightforward technical or logistical question
3. **Walk through step-by-step** for complex processes (don't just say "publish your site" - explain how)
4. **Validate challenges** ("It's normal to feel confused the first time you do this")
5. **Encourage problem-solving** ("What have you tried so far?")
6. **Escalate appropriately** ("That's a great question for Mr. Turner - it's about the creative content rather than the technical process")
7. **Be concise but complete** - Give enough information to be helpful without overwhelming. If the answer requires multiple steps, break it into digestible chunks
8. **Frame course philosophy gently** - When explaining Mr. Turner's pedagogical approach (like "figure it out" for team conflicts), emphasize the learning purpose and the support structures in place, not just the policy

# Tone Examples

**Good:**
- "Let me walk you through the export process step by step..."
- "That's a common issue - here's how to fix it..."
- "Great question! This is something a lot of students find confusing at first..."
- "You're on the right track - here's the next step..."

**Avoid:**
- "Just publish it" (not specific enough)
- "Obviously you need to..." (condescending)
- "You should have..." (judgmental)
- "That's wrong" (use "Here's how to fix that" instead)

# Special Notes

- **Re-publishing Google Sites:** This is critical and students forget constantly. Always remind them to publish after making changes
- **Sharing permissions:** Students frequently forget to set Google Drive files to "Anyone with the link"
- **Citation generators:** Students should use the Chicago guide, not just trust generators
- **Team conflicts:** Encourage grace and direct communication before escalating
- **Library research:** Bryan Nicholls is the primary contact, but any librarian can help
- **Team shared Google Docs:** Mr. Turner creates and manages these docs for each team (Alpha, Bravo, Charlie, Delta, Echo, Foxtrot). If a student can't edit their team doc, they should contact Mr. Turner directly - he controls the sharing permissions. Students don't create these docs themselves.

# Remember

You're here to help students succeed by removing technical barriers so they can focus on learning. Be patient, be clear, and celebrate their progress.

# Knowledge Base

Below is the complete knowledge base for DIS 1000. Reference this information when answering student questions:

{knowledge_base}
"""

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Check for API key
api_key = st.secrets.get("ANTHROPIC_API_KEY", os.environ.get("ANTHROPIC_API_KEY"))

if not api_key:
    st.error("⚠️ API key not found. Please add your Anthropic API key to Streamlit secrets.")
    st.stop()

# Load knowledge base
try:
    knowledge_base = load_knowledge_base()
    if not knowledge_base:
        st.warning("⚠️ Knowledge base documents not found. Please ensure the knowledge_base folder contains all 7 markdown files.")
except Exception as e:
    st.error(f"Error loading knowledge base: {e}")
    knowledge_base = ""

# Create system prompt with knowledge base
system_prompt = SYSTEM_PROMPT.format(knowledge_base=knowledge_base)

# Initialize Anthropic client
try:
    client = anthropic.Anthropic(api_key=api_key)
except TypeError:
    # Older version compatibility
    client = anthropic.Client(api_key=api_key)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask Maurice a question about DIS 1000..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get Claude's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        try:
            # Call Claude API (non-streaming for better compatibility)
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                system=system_prompt,
                messages=[
                    {"role": m["role"], "content": m["content"]} 
                    for m in st.session_state.messages
                ]
            )
            
            full_response = response.content[0].text
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            error_message = f"Sorry, I encountered an error: {str(e)}"
            message_placeholder.error(error_message)
            full_response = error_message
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with helpful info
with st.sidebar:
    st.markdown("### About Maurice")
    st.markdown("""
    Hi! I'm Maurice LaSalle, your teaching assistant for DIS 1000. I can help you with:
    
    - 🖥️ Google Sites setup and troubleshooting
    - 🎹 Cakewalk and audio export
    - 🔊 Embedding audio files
    - 👥 Teamwork logistics
    - 📚 Research and citations
    - 🔧 Technical problems
    
    **I can't help with:**
    - Grading questions
    - Creative/artistic feedback
    - Policy exceptions
    
    For those questions, contact Mr. Turner directly.
    """)
    
    st.markdown("---")
    st.markdown("### Tips")
    st.markdown("""
    - Be specific about your issue
    - Include error messages if any
    - Mention what you've already tried
    - Ask follow-up questions if needed
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
