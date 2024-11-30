import re
import copy

f = open('d21.in', 'r')


def readInput(f):
    foods = []
    for line in f.read().strip().split('\n'):
        ingredients, allergens = re.match(r'(.*) \(contains (.*)\)', line).groups()
        foods.append([set(ingredients.split()), set(allergens.split(', '))])
    return foods


def parseFoods(foods):
    possibleIngredients = {}
    mapping = dict() # ingredient => allergen
    while True:
        findNew = set()
        for i in range(len(foods)-1):
            if len(foods[i][0])==1 and len(foods[i][1])==1:
                allergen = list(foods[i][1])[0]
                ingredient = list(foods[i][0])[0]
                mapping[ingredient] = allergen
                findNew.add(ingredient)
        for i in range(len(foods)-1):
            for j in range(i+1, len(foods)):
                allergen = tuple(sorted(list(foods[i][1] & foods[j][1])))
                if not allergen: continue
                if allergen not in possibleIngredients:
                    possibleIngredients[allergen] = foods[i][0] & foods[j][0]
                else:
                    possibleIngredients[allergen] = possibleIngredients[allergen] & (foods[i][0] & foods[j][0])
                if len(allergen) == 1 and len(possibleIngredients[allergen]) == 1:
                    ingredient = list(possibleIngredients[allergen])[0]
                    mapping[ingredient] = allergen[0]
                    findNew.add(ingredient)
        if not findNew: break
        for i in range(len(foods)):
            newIngredients = foods[i][0] & findNew
            if not newIngredients: continue
            for ingredient in newIngredients:
                foods[i][0].remove(ingredient)
                if mapping[ingredient] in foods[i][1]:
                    foods[i][1].remove(mapping[ingredient])
    return foods, mapping


def findPuzzle1(foods):
    foods, mapping = parseFoods(foods)
    return sum([len(food[0]) for food in foods])


def findPuzzle2(foods):
    foods, mapping = parseFoods(foods)
    ingredients = [item[0] for item in sorted(mapping.items(), key=lambda item: item[1])]
    return ','.join(ingredients)


foods = readInput(f)
print("Puzzle 1: ", findPuzzle1(copy.deepcopy(foods)))
print("Puzzle 1: ", findPuzzle2(copy.deepcopy(foods)))
