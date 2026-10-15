#3.1
from shutil import copy


fav_foods = ["strawberies", "mango", "grilled cheese", "salmon", "pancakes"]
print(fav_foods[3])
print(fav_foods[-1])
fav_foods.append("cookies")
fav_foods.insert(0, "apple")
fav_foods.remove("grilled cheese")
#when removing the 3rd food, I accidentally wrote fav_food instead of fav_foods which resulted in this error: NameError: name 'fav_food' is not defined
print(len(fav_foods))

for item in fav_foods:
    print(str(item).upper())

new_list = fav_foods[0:4:3]
print (new_list)

def new_list():
    if "potato" in fav_foods:
        # I originally mispelled "potato" as "potatos" which resulted in this error: False
        # I also originally wrote a parameter in the function when defining it, which resulted in this error: TypeError: new_list() takes 1 positional argument but 0 were given
        print("A potato!")

    else: 
        print("No potato!")
new_list()

#3.2
numbers = range(0,20)
def get_first_15(numbers):
    first_15 = numbers[0:15]
    return first_15

def get_every_5th(first_15):
    every_5th = first_15[4::5]
    return every_5th 

def reverse_and_stride(every_5th):
    reverse = every_5th[::-1]
    return reverse
    return reverse[::3]

#3.3
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers = [list_1, list_2, list_3]
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(numbers[2][0:3])
print(numbers[1][1])
#When I originally wrote numbers[1][2] instead of numbers[1][1], I got the error: IndexError: list index out of range

numbers.append([10, 11, 12])

def sum_nested(numbers):
    total = 0
    for row in numbers:
        for number in row:
            total += number
    return total
print(sum_nested(numbers))

#3.4
#I had no idea how to do this so I had to do some research and I made an error every line from typos, incorrect functions definitions, and indentations.
import copy

def create_5_by_5():
    grid = []
    count = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        grid.append(row)
    return grid

def replace_multiples_of_3(grid):
    updated_grid = copy.deepcopy(grid)
    for i in range(len(updated_grid)):
        for j in range(len(updated_grid[i])):
            if updated_grid[i][j] % 3 == 0:
                updated_grid[i][j] = "?"
    return updated_grid

def sum_remaining_elements(grid):
    total = 0
    for row in grid:
        for number in row:
            if number != "?":
                total += number
    return total

initial_grid = create_5_by_5()
modified_grid = replace_multiples_of_3(initial_grid)
final_sum = sum_remaining_elements(modified_grid)
print("Initial Grid:")
for r in initial_grid:
    print(r)
print("\nModified Grid:")
for r in modified_grid:
    print(r)
print(f"\nFinal Sum of Remaining Elements: {final_sum}")

#I kept calling the variables different things which really scewed it up. It kept telling me the variable wasn't defined. 


#4.1
ages = {"Katie": 30, "Mariam": 42, "Safia": 25, "Mira": 48}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(f"{name} is {age} years old.")

#5.2 favorite function
numbers = range(0,20)
def get_first_15(numbers):
    first_15 = numbers[0:15]
    return first_15
print(get_first_15(numbers))