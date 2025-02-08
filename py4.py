def average(numbers):
    return sum(numbers) / len(numbers)

numbers = list(map(float, input("Enter numbers separated by space: ").split()))
print(f"Average: {average(numbers)}")
