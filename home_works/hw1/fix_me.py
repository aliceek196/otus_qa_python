"""
My first homework in OTUS QA Python Course
Student: Alisa Kichik
"""


# Calculate function
def calculate_average(nums):
    total = sum(nums)
    count = len(nums)
    return total / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
