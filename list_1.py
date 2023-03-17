# Write a python function that takes a list of integer nums and an integer target, and returns indices of the two numbers such that they add up to
# the target. Return the indices in a tuple. You may assume that each input would have exactly one solution, and you may not use the same element
# twice.
# The table below shows a list of inputs you should pass to your function and the expected results. If you get anything other than the expected
# result, then your function is not correct and you should correct it

nums = [2, 7, 11, 15]
target = 9


def finding_indices(nums, target):
    # This function 'finding_indices' takes in 2 arguments, list of numbers and target.

    num_indices = dict()
    # Empty dictionary 'num_indices' will store number mapped to its corresponding index

    for i, num in enumerate(nums):
        # The function checks for every index and number in the 'nums' list using the enumerate method

        complement = target - num
        # and finds the complement ( a number you get after substracting the current list member iteration from the list )

        if complement in num_indices:
            # If that complement is in the dictionary

            return (num_indices[complement], i)
            # return the mapped index to the corresponding numbers.

        num_indices[num] = i


# 'findings' holds the calling of the function 'finding_indices'
#  the last statement is for printing 'findings.'

findings = finding_indices([2, 7, 11, 15], 9)
print('Indices that add up to make 9 from [2,7,11,15] are:', findings)
