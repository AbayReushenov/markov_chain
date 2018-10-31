#!/usr/bin/env python3

numbers = []
indexes = []
total = 0
lowest = None
highest = None

while True:
    try:
        line = input("enter a number or Enter to finish: ")
        if not line:
            break
        indexes.append(len(numbers))
        print(numbers)
        number = int(line)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError as err:
        print(err)

swapped = True
print("a1")
while swapped:
    print("a2")
    swapped = False
    print("indexes", indexes)
    for index in indexes:
        print("index", index)
        if index + 1 == len(numbers):
            break
        if numbers[index] > numbers[index + 1]:
            print ("numbers[index]", numbers[index], "numbers", numbers)
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
            print("numbers ", numbers) 
            swapped = True

if numbers:
    index = int(len(numbers) / 2)
    median = numbers[index]
    if index and index * 2 == len(numbers):
        median = (median + numbers[index - 1]) / 2

print("numbers:", numbers)
if numbers:
    print("count =", len(numbers), "total =", total,
          "lowest =", lowest, "highest =", highest,
          "mean =", total / len(numbers), "median =", median)
