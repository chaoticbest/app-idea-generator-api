from dataclasses import dataclass
from agents import Agent, Runner
import json
from dotenv import load_dotenv
load_dotenv()

@dataclass
class AppIdea:
    name: str
    description: str

async def generate_idea(category):
    instructions = f"""Generate 5 creative app ideas for the category "{category}". 
        
        These app ideas are part of a "100 Vibe Apps in 100 Days" project, so they should be creative, entertaining, and engaging.
        They should also be relatively small, simple, and easy to build using AI code generation tools.

        For each app idea, provide:
        - A short, descriptive name (2-5 words)
        - A brief description of what the app does (1 sentence)
        
        Format your response as a JSON array with objects containing "name" and "description" fields.
        
        Example format:
        [
          {{
            "name": "App Name",
            "description": "Brief description of what the app does."
          }}
        ]
        
        Make the ideas creative, practical, and relevant to the category."""
    
    agent = Agent(name="idea_generator", instructions=instructions)
    
    result = await Runner.run(agent, "Generate ideas.")
    
    # Parse the result to get a single idea from the array
    try:
        # The result is a RunResult object, we need to get the final_output
        if hasattr(result, 'final_output'):
            json_string = result.final_output
        else:
            json_string = str(result)
        
        # Parse the JSON string
        ideas = json.loads(json_string)
        
        # If it's a list, take the first idea
        if isinstance(ideas, list) and len(ideas) > 0:
            first_idea = ideas[0]
            return AppIdea(name=first_idea["name"], description=first_idea["description"])
        else:
            # Fallback: create a default idea
            return AppIdea(name="Creative App Idea", description="A creative app idea for the specified category.")
    except Exception as e:
        print(f"Error parsing result: {e}")
        # Fallback: create a default idea
        return AppIdea(name="Creative App Idea", description="A creative app idea for the specified category.")
