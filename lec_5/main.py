def sum_of_elements(numbers, exclude_negative=False):
    if exclude_negative:
        filtered_numbers = [num for num in numbers if num >= 0]
    else:
        filtered_numbers = numbers
    return sum(filtered_numbers)

user_input = input("Enter a list of numbers separated by spaces: ")
user_numbers = [int(num) for num in user_input.split()]

exclude_negative_input = input("Do you want to exclude negative numbers? (yes or no): ").strip().lower()
if exclude_negative_input == "yes":
    exclude_negative = True
else:
    exclude_negative = False

result = sum_of_elements(user_numbers, exclude_negative)

if exclude_negative:
    print("Sum of positive numbers:", result)
else:
    print("Sum of all numbers (including negative):", result)
