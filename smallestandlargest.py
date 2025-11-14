nums = [int(input(f"Enter integer {i+1}: ")) for i in range(3)]
total = sum(nums)
average = total / len(nums)
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
smallest = min(nums)
largest = max(nums)

print("\nResults:")
print("Numbers entered:", nums)
print("Sum:", total)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)
