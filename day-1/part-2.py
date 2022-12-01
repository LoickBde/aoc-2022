rawCalories = []
caloriesCarriedByElf = []
totalCalories = 0
maxCaloriesCarried = 0

with open('input.txt') as f:
    rawCalories =  [line.rstrip() for line in f]

currentCaloriesCarried = 0
for i in range(0, len(rawCalories)):
    if rawCalories[i] == "":
        caloriesCarriedByElf.append(currentCaloriesCarried)
        currentCaloriesCarried = 0
        continue
    calories = int(rawCalories[i])
    totalCalories += calories
    currentCaloriesCarried += calories

caloriesCarriedByElf.sort(reverse=True)  

print(f"Calories sum of the top three elves? {sum(caloriesCarriedByElf[:3])}") 