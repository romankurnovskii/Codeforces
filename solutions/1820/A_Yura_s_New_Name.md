Yura wants to change his name to a string consisting of "" and "^" characters. 

However, he wants every character to be part of at least one "^^" or "^^" smiley face, and these smiley faces should be consecutive in the name. 

Task is to find the minimum number of characters to insert into the name to meet Yura's criteria.

### Logic

Iterate through the input string and keep track of the number of '_' characters in between '^' characters. 

Based on this count, determine how many characters need to be added to satisfy Yura's criteria.
