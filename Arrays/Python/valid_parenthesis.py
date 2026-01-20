# #You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:

# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

class Solution:
    def isValid(self, s: str) -> bool:

        ## first approach ( two pointers type time complexity O(n))
        symbolsDict = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        charStack = []

        for index in range(len(s)):
            if str(s[index]) in symbolsDict:
                charStack.append(s[index])
            else:
                if len(charStack) ==0:
                    return False
                removedChar =charStack.pop()
                if(symbolsDict[str(removedChar)] != str(s[index])):
                    return False
        return len(charStack)==0
