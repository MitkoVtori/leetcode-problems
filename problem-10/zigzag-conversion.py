'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''


def convert_to_zigzag(string, number_of_rows):

    if number_of_rows == 1:
        return string

    length = len(string)

    zigzag = [""] * length

    row = 0

    for i in range(length):

        zigzag[row] += string[i]

        if row == number_of_rows - 1:
            down = False

        elif row == 0:
            down = True

        if down:
            row += 1

        else:
            row -= 1

    new_string = ''
    for i in range(len(zigzag)):
        if zigzag[i]:
            new_string += zigzag[i]

    return new_string
