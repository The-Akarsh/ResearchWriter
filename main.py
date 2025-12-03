from crewai import Crew, Process
from agents import researcher, writer
from tasks import research_task, write_task

# 1. Assemble the Crew
tech_crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential  # Run Research FIRST, then Write
)

# 2. User Input
print("\n🔍 SYSTEM INITIALIZED: Starting Agentic Research...")
topic = input("Target Topic: ")
result = tech_crew.kickoff(inputs={'topic': topic})

# 3. Clean Output
print("\n\n📊 FINAL REPORT GENERATED")
print("=========================")
print(result)