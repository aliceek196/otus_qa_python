"""
My first homework in OTUS QA Python Course
Student: Alisa Kichik
"""


# Calculate function
def calculate_average(nums):
    # Initial data
    nums = [10, 15, 20]
    # Calculations
    total = sum(nums)
    count = len(nums)
    average = total / count
    result = average(nums)
    # Output result
    print("The average is:", result)
