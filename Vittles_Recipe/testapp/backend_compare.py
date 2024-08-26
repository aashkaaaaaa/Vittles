# import tkinter as tk
# from tkinter import ttk
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from PIL import Image, ImageTk
# import requests
from io import BytesIO

# Load the dataset
df = pd.read_csv('testapp/data/CopiedFile.csv')

# Create the count matrix
count_vectorizer = CountVectorizer()
count_matrix = count_vectorizer.fit_transform(df['ingredients_name'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(count_matrix, count_matrix)


def recommend_recipe(selected_ingredients):
    if not selected_ingredients:
        return [{"id": None, "name": "No ingredients selected.", "image_url": None}]
    
    # Combine the selected ingredients into a single string
    ingredients_str = ' '.join(selected_ingredients)
    
    # Filter the dataframe to include only recipes that contain all selected ingredients
    filtered_df = df[df['ingredients_name'].apply(lambda x: all(item in x for item in selected_ingredients))]
    
    if filtered_df.empty:
        return [{"id": None, "name": "No recipes found with the selected ingredients.", "image_url": None}]
    
    # Return recipes directly if exact matches are found
    recommended_recipes = []
    for index, row in filtered_df.iterrows():
        recipe_info = {
            'id': row['id'],
            'name': row['name'],
            'image_url': row['image_url']
        }
        recommended_recipes.append(recipe_info)
    
    # Limit to 50 recommendations if needed
    return recommended_recipes
