# A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.
#
# Example
#
# The string contains all letters in the English alphabet, so return pangram.
#
# Function Description
#
# Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.
#
# pangrams has the following parameter(s):
#
# string s: a string to test
# Returns
#
# string: either pangram or not pangram
# Input Format
#
# A single line with string .
#
# Constraints
#
#
# Each character of ,
#
# Sample Input
#
# Sample Input 0
#
# We promptly judged antique ivory buckles for the next prize
#
# Sample Output 0
#
# pangram
#
# Sample Explanation 0
#
# All of the letters of the alphabet are present in the string.
#
# Sample Input 1
#
# We promptly judged antique ivory buckles for the prize
#
# Sample Output 1
#
# not pangram
#
# Sample Explanation 0
#
# The string lacks an x.

def pangrams(s):
    # Write your code here
    apl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    al = []
    for i in range(0, len(s)):
        if s[i] not in al:
            al.append(s[i].lower())

    for j in range(0, len(apl)):
        if apl[j] in al:
            al.remove(apl[j])
        else:
            return "not pangram"
    return "pangram"



print(pangrams("We promptly judged antique ivory buckles for the next prize"))