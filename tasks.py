from crewai import Task
from agents import researcher, writer

# Task 1: Research
research_task = Task(
    description=(
        "Search the internet for the latest trends in {topic}. "
        "Find at least 3 specific examples or new technologies. "
        "Identify key pros and cons."
    ),
    expected_output='A detailed research report with bullet points and source URLs.',
    agent=researcher,
)

# Task 2: Writing
write_task = Task(
    description=(
        "Review the Researcher's notes on {topic}. "
        "Filter out any information that sounds like rumors or fake products. "
        "Compile a 'State of the Art' technical briefing."
        "Use <br> for line breaks between points."
    ),
    expected_output=(
        "A Markdown report containing:\n"
        "1. Executive Summary (2 sentences max)\n"
        "2. Key Features Table (Pros/Cons)\n"
        "3. Technical Specifications (Bullet points)\n"
        "Tone: Clinical, dry, and objective."
    ),
    agent=writer,
    context=[research_task]
)