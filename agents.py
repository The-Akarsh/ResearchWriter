import os
from dotenv import load_dotenv
from crewai import Agent, LLM
from google.genai import types 

load_dotenv()

# 1. DEFINE THE BRAIN + NATIVE SEARCH
# Create the search tool configuration
# Note: We do not need to export this variable. It stays local to this file.
google_search_tool = types.Tool(
    google_search=types.GoogleSearch()
)

# Attach it to the LLM
my_llm = LLM(
    model=os.getenv("MODEL"),
    api_key=os.getenv("GEMINI_API_KEY"),
    tools=[google_search_tool] 
)

# 2. DEFINE AGENT 1: THE RESEARCHER
researcher = Agent(
    role='Senior Research Analyst',
    goal='Uncover cutting-edge developments in {topic}',
    verbose=True, 
    memory=True,  
    backstory=(
        "You are a veteran analyst at a top tech firm."
        "You refuse to accept generic answers; you dig deep."
        "You prioritize real-time data from Google Search."
    ),
    tools=[], # Empty because the LLM handles it natively
    llm=my_llm
)

# 3. DEFINE AGENT 2: THE ANALYST
writer = Agent(
    role='Lead Technical Analyst',
    goal='Summarize complex search results into strict, factual bullet points.',
    verbose=False, 
    memory=True,
    backstory=(
        "You are a blunt, no-nonsense technical analyst."
        "You hate fluff, adjectives, and marketing buzzwords."
        "You only care about raw data, specs, and verified facts."
    ),
    tools=[], 
    llm=my_llm
)