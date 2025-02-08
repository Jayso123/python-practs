def sort_numbers(numbers, order):
    return sorted(numbers, reverse=(order == "descending"))

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
order = input("Enter 'ascending' or 'descending': ").lower()
print(f"Sorted numbers: {sort_numbers(numbers, order)}")
