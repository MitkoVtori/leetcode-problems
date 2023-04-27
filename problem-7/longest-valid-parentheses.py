'''
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring

Example 1:
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:
Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'
'''


def longest_valid_parentheses(s):
    length = len(s)
    stack = [-1]
    result = 0

    for index in range(length):

        if s[index] == '(':
            stack.append(index)

        else:

            if len(stack) != 0:
                stack.pop()

            if len(stack) != 0:
                result = max(result, index - stack[len(stack) - 1])

            else:
                stack.append(index)

    return result
