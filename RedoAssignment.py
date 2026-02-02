import array
import numpy as np
import pandas as pd
import requests as req
from bs4 import BeautifulSoup

# Asssignment 1
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

# Array
matrix = [[2, 4, 3], [1, 5, 7]]

print(matrix)

for row in matrix:
    print(row)

# replacing
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 5:
            matrix[i][j] = 0

# Sum of the column
sum_of_first_column = 0

for i in range(len(matrix)):
    sum_of_first_column = sum_of_first_column+matrix[i][0]

print(sum_of_first_column)

# sumo of Row
sum_of_first_row = 0
for i in range(len(matrix[0])):
    sum_of_first_row = sum_of_first_row+matrix[0][i]

print(sum_of_first_row)


# Assignment 2 a

data = {
    'country': ['NOR', 'GER', 'CHN'],
    'Gold': [16, 12, 9],
    'Silver': [8, 10, 4],
    'Bronze': [13, 5, 2]
}

df = pd.DataFrame(data)

print(df)

print(df[['country', 'Silver']])
print(df[df['country'] == 'CHN'])

print(df[df["Gold"] > 10][["country", "Gold"]])
print(df.sort_values(by='Bronze', ascending=False))

# Assignment 2 b
File = pd.read_csv("/Users/user/Downloads/Beijing1.csv", sep=';')

print(File)

File["Total"] = File["Gold"] + File["Silver"] + File["Bronze"]

File.sort_values(by=["Total", "Gold"], ascending=False)
print(File)


# assignment 3  (Need To make changes)

# url = "https://simple.wikipedia.org/w/api.php"

# params = {
#     "action": "parse",
#     "page": "List_of_countries_by_continents",
#     "format": "json"
# }

# response = req.get(url, params=params)
# data = response.json()

# print(data.keys())
