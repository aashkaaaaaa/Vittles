from crewai import Agent,Task,Process,Crew
import os
import re
import pandas as pd

csv_file_path = 'testapp/data/CopiedFile.csv'

def recommend_recipes_with_rating_10(csv_file_path, is_verbose=True):
    
    os.environ['OPENAI_API_BASE'] = "https://api.groq.com/openai/v1"
    os.environ['OPENAI_MODEL_NAME'] = "llama3-8b-8192"
    os.environ['OPENAI_API_KEY'] = "#API ID Upload"

    is_verbose = True
    csv_file_path = "testapp/data/CopiedFile.csv"
    data = pd.read_csv(csv_file_path)

    responder = Agent(
        role = "recommend recipe",
        goal = f"Based on the ${data} file above show the recipes with Rating 10",
        backstory = f"You are an simple AI assistant whose job is to recommend all the recipes whose Rating are equal to 10 in the ${data} variable which contains a .csv file",
        verbose = True,
        allow_delegation = False
    )

    recommend_recipe = Task(
        description = f"Search the entire dataset from ${data} and display all the id, name, and image_url of all recipes that have a rating of 10.", # Format the output as a list of dictionaries, where each dictionary represents a recipe ith the keys 'id', 'name', and 'image_url'. The list should include all recipes with a rating of 10.",
        agent = responder,
        expected_output = "A list of dictionaries where each dictionary contains the 'id', 'name', and 'image_url' of recipes with a Rating of 10. in form of table without any writing summary without any comments and without any note"
        # expected_output = "Search and display all recipes from the ${data} variable which have a Rating of 10 "
    )
# atleast 5
    crew = Crew(
        agents=[responder],
        tasks=[recommend_recipe],
        verbose=3,
        process = Process.sequential
    )

    output = str(crew.kickoff())
    pattern = r"{([^}]*)}"

    match = re.search(pattern, output)
    print("myout")
    print(match)
    return match

# recommend_recipes_with_rating_10(csv_file_path)

