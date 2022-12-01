rawCalories = []
totalCalories = 0
maxCaloriesCarried = 0

with open('input.txt') as f:
    rawCalories =  [line.rstrip() for line in f]

currentCaloriesCarried = 0
for i in range(0, len(rawCalories)):
    if rawCalories[i] == "":
        if currentCaloriesCarried > maxCaloriesCarried:
            maxCaloriesCarried = currentCaloriesCarried
        currentCaloriesCarried = 0
        continue
    calories = int(rawCalories[i])
    totalCalories += calories
    currentCaloriesCarried += calories
        
print(f"Max calories carried : {maxCaloriesCarried}") 
print(f"Total calories carried : {totalCalories}") 
