class RecipeList:
    def __init__(self, initial_recipes):
        self.recipes = initial_recipes
        self.elf1 = 0
        self.elf2 = 1

    def cycle(self):
        score = self.recipes[self.elf1] + self.recipes[self.elf2]
        if score < 10:
            self.recipes.append(score)
        else:
            self.recipes.append(1)
            self.recipes.append(score - 10)
        self.elf1 = (self.elf1 + 1 +
                     self.recipes[self.elf1]) % len(self.recipes)
        self.elf2 = (self.elf2 + 1 +
                     self.recipes[self.elf2]) % len(self.recipes)


def day14(number_of_recipes):
    recipes = RecipeList([3, 7])
    while len(recipes.recipes) < number_of_recipes + 10:
        recipes.cycle()
    return ''.join([str(c)
                    for c in recipes.recipes[number_of_recipes:number_of_recipes+10]])


# print(day14(890691))
# 8176111038
