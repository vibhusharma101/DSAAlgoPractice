

# Guess Number Higher Or Lower
# Solved 
# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# 0: your guess is equal to the number I picked (i.e. num == pick).
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# Return the number that I picked.




# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number

#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:








class Solution:
    def guessNumber(self, n: int) -> int:
        ans = 0
        startNumber = 1
        endNumber = n

        while startNumber <= endNumber:
            guessedNumber  = (startNumber+endNumber)//2
            if guess(guessedNumber) ==0:
                return guessedNumber
            elif guess(guessedNumber)==-1:
                endNumber = guessedNumber - 1
            else:
                startNumber = guessedNumber + 1
        
        return ans
        