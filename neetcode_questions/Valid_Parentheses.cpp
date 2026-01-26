/*
Valid Parentheses

You are given a string s consisting of the following characters: '(', ')', '{',
'}', '[' and ']'.

The input string s is valid if and only if:
1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
*/

#include <iostream>
#include <map>
#include <string>
#include <vector>


using namespace std;

class Solution {
public:
  bool isValid(string s) {
    map<char, char> rMap = {{'(', ')'}, {'[', ']'}, {'{', '}'}};

    vector<char> rStack;
    for (char ch : s) {
      if (ch == '(' || ch == '[' || ch == '{') {
        rStack.push_back(ch);
      } else {
        if (rStack.size() > 0 && rMap[rStack.at(rStack.size() - 1)] == ch) {
          rStack.pop_back();
        } else {
          return false;
        }
      }
    }
    return rStack.size() == 0;
  }
};

int main() {
  Solution solution;

  // Test cases
  string s1 = "[]";
  string s2 = "([{}])";
  string s3 = "[(])";

  cout << "Test 1 ([]): " << (solution.isValid(s1) ? "true" : "false") << endl;
  cout << "Test 2 (([{}])): " << (solution.isValid(s2) ? "true" : "false")
       << endl;
  cout << "Test 3 ([(])): " << (solution.isValid(s3) ? "true" : "false")
       << endl;

  return 0;
}
