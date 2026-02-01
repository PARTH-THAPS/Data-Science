import array
import numpy as np

arr = array.array('d', [1.5, 2.8, 0.2, 3.1])
numpArr = np.array([2, 5, 34, 67])

# To print 2 element of the array
print(arr[1])

print(f"This is the Second Element:{arr[1]}\nThis is third element:{arr[2]} ")

inputNumber = input("Enter number to replace the value of first element")

arr[0] = float(inputNumber)

print(arr)

for i in range(len(arr)):
    if arr[i] > 2:
        print(arr[i])


x_squared = array.array('d', [])

print(type(x_squared))
for y in range(len(arr)):
    x_squared.append(arr[y]*2)

print(x_squared)


arr.append(5.2)

print(arr)


# Mean of the array
sum = 0
for k in range(len(arr)):
    sum = arr[k]+sum

mean = sum/len(arr)


# Range Start
for i in range(0, 5):
    print(i)

# Looping Through List
fruits = ["Apple", "Cherry", "Banana"]

for fruit in fruits:
    print(fruit)


# Looping through String

for letter in "Python":
    print(letter)


# while loop

count = 1
while count < 5:
    print(count)
    count = count+1


for i in range(5):
    if i == 2:
        continue
    print(i)


print("Pass line of code will run (Pass is the placeholder only")
for i in range(5):
    if i == 3:
        pass
    print(i)


for i in range(3):
    for j in range(2):
        print(i, j)


list = [-5, 7, 8, 'Error', 5]

for j in range(len(list)):
    if list[j] == "Error":
        list[j] = 0
    break

    print(list)


# Dictionary

medals = {}

medals = {
    "USA": 112,
    "Germany": 36,
    "China": 100
}

medals["Italy"] = 40
medals.pop("Germany")
medals.update({"USA": 113})

print(medals)

print("Keys", medals.keys())
print("Values", medals.values())

print(medals)
