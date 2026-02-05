def hours_to_seconds(hours):
    return hours * 3600

test_hours = [1, 2, 5, 10]

for h in test_hours:
    print(f"{h} hours is {hours_to_seconds(h)} seconds")

print("\n--- Debugging practice ---\n")

# def divide(a, b):
#     return a / b
#
# numbers = [(10, 2), (5, 0), (8, 4)]
#
# for x, y in numbers:
#     print(divide(x, y))

print("\n--- Chapter 6: Exercise 1 ---")

def exercise_1(numbers):
    total = 0
    count = 0

    for n in numbers:
        total = total + n
        count = count + 1

    return total / count
    
test_numbers_1 = [
    [25, 4, 6],
    [8, 23, 14, 25]
]

for case in test_numbers_1:
    print(exercise_1(case))

print("\n--- Chapter 6: Exercise 2 ---")

def exercise_2(numbers_2):
    total = 0

    for n in numbers_2:
        total = total + n

    return total

test_numbers_2 = [
    [32, 45, 69],
    [9, 6, 15]
]

for case in test_numbers_2:
    print(exercise_2(case))

print("\n--- Chapter 6: Exercise 3 ---")

def exercise_3(numerator, denominator):
    raw_result = numerator / denominator
    rounded_result = round(raw_result, 2)

    print("Raw: ", raw_result)
    print("Rounded: ", rounded_result)

exercise_3(10,3)

print("\n--- Chapter 6: Exercise 4 ---")

def exercise_4(numbers_4):
    largest = numbers_4[0]
    
    for n in numbers_4:
        if n > largest:
            largest = n

    return largest

print(exercise_4([5, -6, 300, 301, -302]))
print(exercise_4([1, 2, 3, 4, 0]))

print("\n--- Chapter 6: Exercise 5 ---")

def exercise_5(numbers_5):
    smallest = numbers_5[0]
    
    for n in numbers_5:
        if n < smallest:
            smallest = n

    return smallest

print(exercise_5([5, -6, 300, 301, -302]))
print(exercise_5([1, 2, 3, 4, 0]))

print("\n--- Chapter 6: Exercise 6 ---")

def exercise_6a(numbers_6a):
    largest = numbers_6a[0]

    for n in numbers_6a:
        if n > largest:
            largest = n

    smallest = numbers_6a[0]

    for n in numbers_6a:
        if n < smallest:
            smallest = n

    return largest - smallest

print(exercise_6a([10, 9, 8, 7, 6, 5]))
print(exercise_6a([10, 4, 3, 2, 1, 0]))

def exercise_6b(numbers_6b):
    largest = exercise_4(numbers_6b)
    smallest = exercise_5(numbers_6b)

    return largest - smallest

print(exercise_6b([10, 9, 8, 7, 6, 5]))
print(exercise_6b([10, 4, 3, 2, 1, 0]))