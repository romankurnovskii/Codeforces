You need to form a team from a group of students with different smartness levels such that the team is proficient in all given topics. 

A student is proficient in a topic if their smartness is divisible by the topic number. 

The goal is to minimize the maximum difference in smartness between any two students in the team.

**Logic:**

1. Precompute divisors for all numbers up to a maximum value
1. Sort the students by their smartness levels
1. Use the sliding window approach with two pointers (left and right) to maintain a window of students
1. Iterate through the students, updating the count of students proficient in each topic using the precomputed divisors
1. Adjust the window size to minimize the maximum difference in smartness levels between any two students in the window
