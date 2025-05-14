from crewai import Crew, Process
from agents import agents
from tasks import tasks
import json
# from langfuse import Langfuse
from dotenv import load_dotenv
load_dotenv()

crew = Crew(
    agents=list(agents.values()),
    tasks=tasks,output_log_file=True,
    # manager_agent=agents["manager"],
    process=Process.sequential
)
# langfuse = Langfuse()
#
# def log_output(agent_name, input_text, output_text):
#     langfuse.trace(
#         name=f"{agent_name} trace",
#         input=input_text,
#         output=output_text
#     )

if __name__ == "__main__":
    print("🚀 Running CrewAI Fashion Competitor Analysis...\n")
    crew_output = crew.kickoff()
    print("\n✅ Final Output:\n")
    # print(crew_output)

    # Accessing the crew output
    print(f"Raw Output: {crew_output.raw}")
    if crew_output.json_dict:
        print(f"JSON Output: {json.dumps(crew_output.json_dict, indent=2)}")
    if crew_output.pydantic:
        print(f"Pydantic Output: {crew_output.pydantic}")
    print(f"Tasks Output: {crew_output.tasks_output}")
    print(f"Token Usage: {crew_output.token_usage}")


