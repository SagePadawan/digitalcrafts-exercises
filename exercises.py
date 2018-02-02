#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  sum numbers

# def sum(a): 
#     result = 0
#     for number in a: 
#         result += number
    
#     return result

# print (sum([3,4,5,6]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def largest(numbers):
#     largest = numbers[0]
#     for number in numbers:
#         if number > largest: 
#             largest = number

#     return largest
# print (largest([3,4,5,6,7,8,9]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def smallest(numbers):
#     smallest = numbers[0]
#     for number in numbers:
#         if number < smallest:
#             smallest = number
        
#     return smallest
# print(smallest([6, 7, 8, 13, 24, 32, 56]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def even(numbers):
#     for number in numbers: 
#         if number % 2 == 0:
#             return numbers
# print(even([6, 7, 8, 13, 24, 33, 56, 21]))


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Multiply a list

# def multiply(numbers, factor):
#     multiplied = []
#     for number in numbers:
#         multiplied.append(number * factor)
#     return multiplied
# print (multiply([4, -7, -8, 56, 73, -6, -13, 21],3))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Multiply Vecotrs
# What even are vecotrs?

# def vectorply(vector1, vector2):
#     multiplied = []
#     for i in range(len(vector1)):
#         multiplied.append(vector1[i] * vector2[i])
#     return multiplied
# print (vectorply([4, -7, -10, 5, 14],[2, 3, -3, -5, 11]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Matrix Addition
# A list of lists
# Given a 2 dimensional list  of sixe 2x2, calculate the result
#of adding the two matrices
#example: 
# 1 3
# 2 4
# and

# 5 2
# 1 0
# results in

# 6 5
# 3 4

def matrix(Matrix_1,Matrix_2):
    height = len(Matrix_1)
    width = len(Matrix_1[0])

    result = []

    for i in range(0, height):
        result.append([])
        for j in range(0, width):
            result[i].append(None)

    for i in range(0, height):
        for j in range(0, width): 
            cell1 = Matrix_1[i][j]
            cell2 = Matrix_2[i][j]

            result[i][j] = cell1 + cell2
    return result
print (matrix([[2, -2],[5, 3]],[[4, 3],[-3, 1]])) 

Matrix_1 = [
    [2, -2],
    [5, 3]
]
Matrix_2 = [
    [4, 3],
    [-3, 1]
]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DeDup
# def dedup(things):
#     deduped = []

#     for thing in things:
#         if thing not in deduped:
#             deduped.append(thing)
#     return deduped
# print (dedup(['apple', 'cheese', 'bread', 'cheese', 'milk', 'rice', 'books', 'coffee']))
# # things = ['apple', 'cheese', 'bread', 'cheese', 'milk', 'rice', 'books', 'coffee']
