# Question : 
# Remove Duplicates From Sorted Array
# Solved 
# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# Note:

# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result


class Solution:

    def removeFromMiddle(self,nums:List[int],index):
        for innerIndex in range(index,len(nums)-1):
            nums[innerIndex] = nums[innerIndex+1]
        nums[len(nums)-1]  = 102



    def removeDuplicates(self, nums: List[int]) -> int:

        #Brute Force (Time Complexity = O(n^2) )
        # numDictBruteForce = {}
        # ansBruteForce =0
        # cuurentIndexBruteForce = 0

        # while cuurentIndexBruteForce < len(nums):
        #     if nums[cuurentIndexBruteForce] == 102:
        #         break
        #     if (str(nums[cuurentIndexBruteForce]) in numDictBruteForce) is False:
        #         numDictBruteForce[str(nums[cuurentIndexBruteForce])] = True
        #         ansBruteForce = ansBruteForce +1
        #         cuurentIndexBruteForce = cuurentIndexBruteForce + 1
        #     else:
        #         self.removeFromMiddle(nums,cuurentIndexBruteForce)
        # return ansBruteForce

        ## Better Way ( using set Time Complexity ( O ( n logn )
        #  ( In this question it will o(n)
        #  But if the list was not sorted then it would have been O(n logn)


        # numsDict2 = sorted(set(nums))
        # nums[:len(numsDict2)] = numsDict2
        # return len(numsDict2);

        ## Best Way ( using two pointer Time Complexity O(n))
        ## Only works in sorted arrays 

        pointer1Index = 0
        pointer2Index = 1
        ans3 =1

        for innerIndex in range(1,len(nums)):
            if nums[pointer1Index] != nums[innerIndex]:
                print(nums[innerIndex])
                nums[pointer1Index+1] = nums[innerIndex]
                pointer1Index = pointer1Index+1
                ans3 = ans3+1

        return ans3
