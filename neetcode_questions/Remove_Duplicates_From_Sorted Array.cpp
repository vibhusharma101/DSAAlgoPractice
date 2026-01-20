/*
You are given an integer array nums sorted in non-decreasing order. Your task is
to remove duplicates from nums in-place so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as
k, such that the first k elements of nums contain the unique elements.

Note:
The order of the unique elements should remain the same as in the original
array. It is not necessary to consider elements beyond the first k positions of
the array. To be accepted, the first k elements of nums must contain all the
unique elements. Return k as the final result.

Example 1:

Input: nums = [1,1,2,3,4]

Output: [1,2,3,4]
Explanation: You should return k = 4 as we have four unique elements.

Example 2:

Input: nums = [2,10,10,30,30,30]

Output: [2,10,30]
Explanation: You should return k = 3 as we have three unique elements.

Constraints:

1 <= nums.length <= 30,000
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int removeDuplicates(vector<int> &nums) {
    int p1 = 0;
    int p2 = 1;
    while (p2 < nums.size()) {
      if (nums[p1] != nums[p2]) {
        nums[p1 + 1] = nums[p2];
        p1++;
        p2++;
      } else {
        while (p2 < nums.size() && nums[p1] == nums[p2]) {
          p2++;
        }
      }
    }
    return p1 + 1;
  }
};

int main() {
  // Basic test case
  Solution solution;
  vector<int> nums = {1, 1, 2};

  cout << "Original array: ";
  for (int num : nums)
    cout << num << " ";
  cout << endl;

  int k = solution.removeDuplicates(nums);

  cout << "Number of unique elements: " << k << endl;
  cout << "Modified array (first k elements): ";
  for (int i = 0; i < k; i++) {
    cout << nums[i] << " ";
  }
  cout << endl;

  return 0;
}