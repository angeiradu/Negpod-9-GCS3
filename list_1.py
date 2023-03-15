# Write a python function that takes a list of integer nums and an integer target, and returns indices of the two numbers such that they add up to
# the target. Return the indices in a tuple. You may assume that each input would have exactly one solution, and you may not use the same element
# twice.
# The table below shows a list of inputs you should pass to your function and the expected results. If you get anything other than the expected
# result, then your function is not correct and you should correct it

nums = [2, 7, 11, 15]
target = 9

count = -1

substract = 0

for iteration in nums:
    substract = target - iteration
    for iteration in nums:
        if substract == iteration:
            print(F'Substract is {substract}')
            print(F'iteration was {iteration}')
            break
