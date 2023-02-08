# Name: Peter Orndoff
# Class: CS 325 - Analysis of Algorithms.
# Description: Given a list and a target integer, returns a list of combinations.

def amount(amount_values, target_sum, start=0):
    """
    :param amount_values: Passed Collection values
    :param target_sum: Passed Sum values
    :return: Returns a list of combinations
    """

    resultant = []  # Resultant combinations
    combinations = []  # Stores Combinations
    starting_index = 0  # Starting index for recursive helper function

    amount_helper(amount_values, starting_index, target_sum, resultant, combinations)
    return resultant


def amount_helper(amount_values, starting_index, remainder, resultant, combinations):
    if remainder == 0:  # Checks if Base case has been met

        if combinations in resultant:  # Checks duplicate
            return

        else:

            resultant.append([])
            for i in combinations:
                resultant[len(resultant) - 1].append(i)

            return

    elif remainder < 0:  # If remainder is greater than the target sum:
        return

    if starting_index > 0:

        if combinations[len(combinations) - 1] is amount_values[starting_index]:  # Checks if value has been used before
            starting_index += 1  # Increments index by 1

    if starting_index == 0 and len(combinations) > 0:

        if combinations[0] is amount_values[starting_index]:
            starting_index += 1

    for i in range(starting_index, len(amount_values)):  # For loop that iterates through values

        combinations.append(amount_values[i])
        amount_helper(amount_values, i, remainder - amount_values[i], resultant, combinations)
        combinations.pop()


"""
Test Failed: Lists differ: [[2, 7], [1, 1, 7], [2, 2, 5], [1, 1, 2, 5]] != [[2, 7], [1, 1, 7]]

First list contains 2 additional elements.
First extra element 2:
[2, 2, 5]

- [[2, 7], [1, 1, 7], [2, 2, 5], [1, 1, 2, 5]]
+ [[2, 7], [1, 1, 7]] : 
Expected Maximum Sum value: [[2, 7], [1, 1, 7], [2, 2, 5], [1, 1, 2, 5]] 
Maximum Sum value from your code: [[2, 7], [1, 1, 7]]




PSEUDOCODE:

Example: A = [11,1,3,2,6,1,5]; Target Sum = 8
Result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]

def amount(values, target_sum):
    combinations = [] # Stores previous combinations
    result = [] # Stores results

    amount_helper(values, starting_index, result, combinations)


def amount_helper(values, remainder, start_index, result, combinations)

    if remainder == 0: 
        append combination to results

    if remainder < 0:
        return 

    otherwise:

    for i in range(start_index, len(values): Iterate over passed list
        append combinations: combinations.append(values[i]

        recursive call: amount_helper(values, remainder - start_index[1], i, 
            result, combinations) 

        #BACKTRACK BITCH
        combinations.pop()


IMPLEMENTATION:

Input: Amount of Values, Target Sum. 
I need to find all unique combinations in A where the values sum up to Target Sum.
Output: Returns ALL unique combinations in the form of a list.

Caveats:

No Duplicate Combinations
Each Amount Value may be used once PER occurrence in list.
Return an Empty list if no possible solution exists.

EXAMPLE ARGUMENTS:

Example: A = [11,1,3,2,6,1,5]; Target Sum = 8
Result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]
"""

"""1. Implement a backtracking algorithm
Given a collection of amount values (A) and a target sum (S), find all unique combinations in
A where the amount values sum up to S. Return these combinations in the form of a list.
Each amount value may be used only the number of times it occurs in list A. The solution set
should not contain duplicate combinations. Amounts will be positive numbers.
Return an empty list if no possible solution exists.

Example: A = [11,1,3,2,6,1,5]; Target Sum = 8
Result = [[3, 5], [2, 6], [1, 2, 5], [1, 1, 6]]

a. Describe a backtracking algorithm to solve this problem.
b. Implement the solution in a function amount(A, S). Name your file Amount.py
c. What is the time complexity of your implementation, you may find time complexity in
detailed or state whether it is linear/polynomial/exponential. etc.?

"""