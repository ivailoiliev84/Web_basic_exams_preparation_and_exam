from django.shortcuts import render, redirect

# Create your views here.
from recipes.main_app.forms import RecipeForm
from recipes.main_app.models import Recipe


def get_ingredients(ingredients):
    start = 0
    end = 0
    ing = []
    for el in ingredients:
        if el == ',' or len(ingredients) == end - 1:
            ing.append(str(ingredients[start:end - 1]))
            start = end + 1
            end += 1
        end += 1

    return ing


def home(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request, 'index.html', context)


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = RecipeForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)

    context = {
        'form': form
    }
    return render(request, 'edit.html', context)


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = get_ingredients(recipe.ingredients)

    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'details.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(request.POST, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            recipe.delete()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    context = {
        'recipe': recipe,
        'form': form
    }
    return render(request, 'delete.html', context)
