#include <iostream>
using namespace std;

// Array is a collection of similar data types
int main() {
  // Array indexing ( Time complexity O(1) )
  cout << "Array Indexing" << endl;
  int myArray[] = {1, 2, 3, 4, 5};
  cout << myArray[0] << endl;
  int n = sizeof(myArray) / sizeof(myArray[0]);

  // Traversing the array ( Time complexity O(n) )
  cout << "Traversing the array For Loop" << endl;
  for (int i = 0; i < n; i++) {
    cout << myArray[i] << endl;
  }
  cout << "Travesring the array while loop" << endl;
  int i = 0;
  while (i < n) {
    cout << myArray[i] << endl;
    i++;
  }
  cout << "End Of Array Traversing" << endl;

  // Deleting an element from the end of array ( Time complexity O(1) )
  cout << "Deleting an element from the end of array" << endl;
  myArray[4] = 0;
  cout << myArray[4] << endl;

  // Deleting an element from start of array ( Time complexity O(n) )
  cout << "Deleting an element from start of array" << endl;
  for (int i = 0; i < 4; i++) {
    myArray[i] = myArray[i + 1];
  }
  cout << myArray[0] << endl;
}