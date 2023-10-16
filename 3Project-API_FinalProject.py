import requests

from pprint import pprint
from nltk.corpus import words


# the first function that checks dietary restrictions
def diet():

    dietList = ["pescetarian", "lacto vegetarian", "ovo vegetarian", "vegan", "paleo", "primal", "vegetarian"]
    intoleranceList = ["dairy", "egg", "gluten", "peanut", "sesame", "seafood", "shellfish", "soy", "sulfite", "treenut", "wheat"]

    while True:
        foodType = input("Please enter the type of food: ")
        print("Restrictions: pescetarian, lacto vegetarian, ovo vegetarian, vegan, paleo, primal, and vegetarian. ")

        dietType = input("Please enter dietary restrictions: ")
        dietType = dietType.lower()
        print("Possible values are: dairy, egg, gluten, peanut, sesame, seafood, shellfish, soy, sulfite, tree nut, and wheat. ")

        intoleranceType = input("Please enter any food intolerance: ")
        intoleranceType = intoleranceType.lower()

        if dietType in dietList and intoleranceType in intoleranceList:

            # the request
            url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"
            querystring = {"query":foodType,"diet":dietType,"intolerances":intoleranceType}
            headers = {
            	"content-type": "application/octet-stream",
            	"X-RapidAPI-Key": "0a263239demshfe705ee15e1aceep15afe6jsne158ca94d6b8",
            	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            myJSON = response.json()

            if myJSON['results'] == []:
                print()
                print("That was not one of the proper entries. ")
                diet()

            food_lst = []
            for food in myJSON['results']:
                food_lst.append(food['title'])
            pprint(food_lst)

            break
        else:
            print("")
            print("That was not one of the proper entries.")

def ingridient():

    myJSON = ''
    number = ''

    ingredient_lst = []
    ingredient = ''

    while ingredient != "q":
        ingredient = input("Please enter an ingredient or q to quit: ")
        if ingredient == 'Q':
            ingredient = 'q'

        ingredient_lst.append(ingredient)
    ingredient_lst = ingredient_lst[:-1]

    for ingredient in ingredient_lst:
        if (ingredient in words.words()) is False:
            print("That was not one of the proper entries.")
            ingridient()
        else:
            continue

    number = int(input("Please enter number of recipes: "))

    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
    querystring = {"ingredients":ingredient_lst, "number":number}

    headers = {
        "content-type": "application/octet-stream",
        "X-RapidAPI-Key": "0a263239demshfe705ee15e1aceep15afe6jsne158ca94d6b8",
        "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    myJSON = response.json()

    food_lst = []

    for i in range(number):
        food = myJSON[i]['title']
        food_lst.append(food)

    print(food_lst)

print("--------------------------------------")
ingridient()
