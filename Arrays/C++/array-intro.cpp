#include <iostream>
using namespace std;

// Function to insert an element at a specific index
void insertAtIndex(int arr[], int &size, int capacity, int index, int value) {
  if (size >= capacity) {
    cout << "Array is full, cannot insert." << endl;
    return;
  }
  if (index < 0 || index > size) {
    cout << "Invalid index." << endl;
    return;
  }

  // Shift elements to the right to make space for the new element
  for (int i = size; i > index; i--) {
    arr[i] = arr[i - 1];
  }

  // Insert the value at the specified index
  arr[index] = value;
  size++;
}

// Function to remove an element at a specific index
void removeAtIndex(int arr[], int &size, int index) {
  if (size <= 0) {
    cout << "Array is empty, cannot remove." << endl;
    return;
  }
  if (index < 0 || index >= size) {
    cout << "Invalid index." << endl;
    return;
  }

  // Shift elements to the left to fill the gap
  for (int i = index; i < size - 1; i++) {
    arr[i] = arr[i + 1];
  }

  size--;
}

// Function to print the array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

int main() {
  // Array is a collection of similar data types
  // We define an array with extra capacity to allow insertions
  int capacity = 10;
  int myArray[10] = {1, 2, 3, 4, 5};
  int n = 5; // Current number of elements

  cout << "Original array: ";
  printArray(myArray, n);

  // Adding at index 2 (Time complexity O(n))
  cout << "Adding 10 at index 2:" << endl;
  insertAtIndex(myArray, n, capacity, 2, 10);
  printArray(myArray, n);

  // Removing at index 3 (Time complexity O(n))
  cout << "Removing element at index 3:" << endl;
  removeAtIndex(myArray, n, 3);
  printArray(myArray, n);

  // Initial introductory examples
  cout << "\n--- Introductory Examples ---" << endl;

  // Array indexing ( Time complexity O(1) )
  cout << "Array Indexing: myArray[0] = " << myArray[0] << endl;

  // Traversing the array ( Time complexity O(n) )
  cout << "Traversing the array For Loop:" << endl;
  for (int i = 0; i < n; i++) {
    cout << myArray[i] << " ";
  }
  cout << endl;

  return 0;
}
