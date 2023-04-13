The main idea of the solution is to iterate through the array, making the difference between consecutive pairs alternate between positive and negative. To do this, we can perform the following algorithm:

1. Iterate through the array with a step of 2 (i.e., process every other element).
1. For each element, check if it is the last element or the second-last element.
   1. If it's the last element, the answer is "YES" because we can always make the array non-decreasing by adding or subtracting the same value from every other element.
   2. If it's the second-last element, the answer is "YES" if the current element is less than or equal to the next element, otherwise, it's "NO".
1. If the current element is not the last or second-last element, update the next *next* element by subtracting the difference between the current element and the next element. This ensures that the difference between consecutive pairs alternates between positive and negative.
