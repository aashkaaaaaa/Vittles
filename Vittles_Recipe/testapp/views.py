from django.shortcuts import render, redirect
import json
from . import backend_compare, backend_recommend
import csv
from urllib.parse import urlencode  # For secure encoding
from urllib.parse import parse_qs  # For secure decoding

# Create your views here.
def get_ingreds_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        ingred_list = []
        for row in reader:
            item=row['ingredients'],
            # print((item[0].lower(), item[0]))
            ingred_list += [(item[0],item[0])]
        # print(ingred_list)
        return ingred_list


from .forms import IngredientForm

def ingredient_form_view(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            # Process the form data here
            selected_ingredients = form.cleaned_data['ingredients']
            selected_ingredients_list = list(selected_ingredients)
            # pass selected_ingredients_list to backend
            for item in selected_ingredients_list:
                print(item)

            # REDIRECT PART
            # # ... (Your view logic to create the ingredient_list)
            # encoded_list = json.dumps(selected_ingredients_list)
            # # Securely encode the data using urlencode
            # url_params = urlencode({'ingredients': encoded_list})
            # return redirect('/testapp/vittlesout/', f'?{url_params}')

            # RENDER PART
            recipe_data = backend_compare.recommend_recipe(selected_ingredients_list)

            context = {'recipes': recipe_data}
            return render(request, 'recipes.html', context)
    else:
        form = IngredientForm()

    return render(request, 'ingredient_form.html', {'form': form})

def recipes_view(request):
    encoded_list = request.GET.get('ingredients')
    # Securely decode the data using parse_qs
    decoded_dict = parse_qs(encoded_list)
    selected_ingredients_list = json.loads(decoded_dict.get('ingredients', [''])[0]) if encoded_list else []
    # ... (Use ingredient_list in your template or logic)

    recipe_data = backend_compare.recommend_recipe(selected_ingredients_list)

    context = {'recipes': recipe_data}
    print(context)
    return render(request, 'recipes.html', context)


def recipe_detail(request, recipe_id):
    csv_file_path = 'testapp/data/CopiedFile.csv'

    try:
        # Open and read CSV file
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Iterate through CSV rows to find the recipe with the matching ID
            for row in reader:
                if int(row['id']) == int(recipe_id):
                    # Create or get the RecipeInfo instance
                    print(row['id'])
                    print(recipe_id)
                    print("created")
                    context = {'recipe': row}
                    return render(request, 'recipe_detail.html', context)

        # If ID not found, handle gracefully
        return render(request, 'recipe_detail.html', {'error': f'Recipe with ID {recipe_id} not found in CSV'})

    except FileNotFoundError:
        # Handle file not found error
        return render(request, 'recipe_detail.html', {'error': 'CSV file not found'})

    except Exception as e:
        # Handle other exceptions
        return render(request, 'recipe_detail.html', {'error': str(e)})



def recipe_recommend_llama(request):
    csv_file_path = 'testapp/data/CopiedFile.csv'
    output = backend_recommend.recommend_recipes_with_rating_10(csv_file_path)
    context = {'llamaout': output}
    return render(request, 'llama_output.html', context)
