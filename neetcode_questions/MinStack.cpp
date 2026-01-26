/*
Minimum Stack

Design a stack class that supports the push, pop, top, and getMin operations.

- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.

Example 1:
Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top",
"getMin"] Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

Constraints:
-2^31 <= val <= 2^31 - 1.
pop, top and getMin will always be called on non-empty stacks.
*/

#include <algorithm>
#include <iostream>
#include <stack>


using namespace std;

class MinStack {
public:
  stack<int> minStack;
  stack<int> rStk;

  MinStack() {}

  void push(int val) {
    rStk.push(val);
    val = min(val, minStack.empty() ? val : minStack.top());
    minStack.push(val);
  }

  void pop() {
    minStack.pop();
    rStk.pop();
  }

  int top() { return rStk.top(); }

  int getMin() { return minStack.top(); }
};

int main() {
  MinStack *minStack = new MinStack();

  cout << "pushing 1, 2, 0" << endl;
  minStack->push(1);
  minStack->push(2);
  minStack->push(0);

  cout << "getMin(): " << minStack->getMin() << " (Expected: 0)" << endl;

  minStack->pop();
  cout << "After pop()..." << endl;

  cout << "top(): " << minStack->top() << " (Expected: 2)" << endl;
  cout << "getMin(): " << minStack->getMin() << " (Expected: 1)" << endl;

  delete minStack;
  return 0;
}
