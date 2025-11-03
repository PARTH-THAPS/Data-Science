import array

# create an array
arr = array.array('d', [1.5, 2.8, 0.2, 3.1])

# printing Second element of the array
output1 = arr[1]
print(output1)

# printing second and third element of the array
output2 = arr[1:3]
print(output2)


# changing the first element of the array
arr[0] = 1.9
print(arr)

# printing all the element of the array

for i in range(len(arr)):
    if arr[i] > 2:
        print(arr[i])


# Multiplying all element by 2

x_squared = []
for y in range(len(arr)):
    x_squared.append(arr[y] * 2)
print(x_squared)

# Adding a new number in the array
arr.append(5.2)

print(arr)

# mean of the array
sum = 0
for j in range(len(arr)):
    sum = sum+arr[j]

mean = sum/len(arr)

print(mean)


# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Difference between array and list , list is used to store different data type but in case of array it is not possible
#  ⚙️ 3. Performance Lists are flexible but slower for mathematical operations. Arrays (NumPy) are faster and more memory efficient for large numerical data because they use C-based implementations.

# List Assignment

list = [-5, 7, 8, "Error", 5]

for j in range(len(list)):
    print(type(list[j]))


list.append(3)
list.append(5)

print(list)

for k in range(len(list)):
    if list[k] == "Error":
        list[k] = 0
        break

print(list)


# Dictionary
medals = {}

medals = {
    "Germany": 36,
    "China": 100,
    "Usa": 112
}

medals["Italy"] = 40
medals.update({"India": 4})
del medals["China"]
medals.update({"Usa": 113})


print("Keys:", medals.keys())
print("Values:", medals.values())

print(medals)


# Matrix
# 1. Save the matrix
matrix = [
    [2, 4, 3],
    [1, 5, 7]
]

# 2. Print it in the form of a matrix
print("Matrix:")
for row in matrix:
    print(row)

# 3. Access element with value 5 and replace it with 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 5:
            matrix[i][j] = 0

print("\nMatrix after replacing 5 with 0:")
for row in matrix:
    print(row)

# 4. Sum of the values in the first row
sum_of_first_row = 0

for i in range(len(matrix[0])):
    sum_of_first_row = sum_of_first_row + matrix[0][i]

print(sum_of_first_row)
