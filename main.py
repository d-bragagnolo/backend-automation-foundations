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