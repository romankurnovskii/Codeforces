1. Initialize the minimum and maximum range with the given limits.
1. Iterate through each query and perform the operations.
   1. For type 1 operation:
      1. Calculate the current minimum and maximum values using the given integers 'a', 'b', and 'n'.
      2. Update the overall minimum and maximum range by taking the intersection of the current range with the overall range.
      3. Append the result (0 or 1) based on whether the updated range is valid or not.
   2. For type 2 operation:
      1. Calculate the minimum value of 'n' that satisfies the condition based on the current range and given integers 'a' and 'b'.
      2. Append the result (-1 or minimum 'n').
