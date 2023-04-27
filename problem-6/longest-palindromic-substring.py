'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''


def show_result(string, low, high):
    result = ''
    for i in range(low, high + 1):
        result += string[i]
    return result


def longest_palindrome(s):
    length = len(s)

    max_length = -float('inf')
    start = 0

    for i in range(length):
        for j in range(i, length):
            flag = 1

            for k in range(0, ((j - i) // 2) + 1):
                if s[i + k] != s[j - k]:
                    flag = 0

            if flag != 0 and (j - i + 1) > max_length:
                start = i
                max_length = j - i + 1

    return show_result(s, start, start + max_length - 1)
