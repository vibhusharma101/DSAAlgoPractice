/*
Concatenation of Array
Solved
Easy

You are given an integer array nums of length n. Create an array ans of length
2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

Example 1:
Input: nums = [1,4,1,2]
Output: [1,4,1,2,1,4,1,2]

Example 2:
Input: nums = [22,21,20,1]
Output: [22,21,20,1,22,21,20,1]

Constraints:
1 <= nums.length <= 1000.
1 <= nums[i] <= 1000.
*/

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> getConcatenation(vector<int> &nums) {
    int n = nums.size();
    vector<int> cNum(2 * n);
    for (int i = 0; i < n; i++) {
      cNum[i] = cNum[i + n] = nums[i];
    }
    return cNum;
  }
};

int main() {
  Solution solution;

  // Test Case 1
  vector<int> nums1 = {1, 4, 1, 2};
  vector<int> res1 = solution.getConcatenation(nums1);
  cout << "Test Case 1: ";
  for (int num : res1)
    cout << num << " ";
  cout << endl;

  // Test Case 2
  vector<int> nums2 = {22, 21, 20, 1};
  vector<int> res2 = solution.getConcatenation(nums2);
  cout << "Test Case 2: ";
  for (int num : res2)
    cout << num << " ";
  cout << endl;

  return 0;
}
