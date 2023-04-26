**Logic:**

For a given integer template, the number of integers that match the template depends on the number of question marks and their positions. 

For the first position, if it's a question mark, you can use any digit from 1 to 9; for other positions, if it's a question mark, you can use any digit from 0 to 9.

**Approach:**

Iterate through the given string, checking each character. If the first character is '0', set the result to 0. If the character is a question mark, multiply the result by 9 if it's the first position, otherwise multiply by 10.