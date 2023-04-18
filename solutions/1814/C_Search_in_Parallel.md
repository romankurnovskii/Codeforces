You have n boxes with balls of different colors and two robots to retrieve balls for you. You need to assign the boxes to two lists (a and b), one for each robot. When you request a ball of color x, the robots search the boxes in their list one by one. The first robot takes s1 seconds to analyze a box, and the second robot takes s2 seconds. You have to assign the boxes to the lists in such a way that the total search time for all requests is minimized.

1. Sort the boxes in decreasing order of the number of requests for their corresponding color.
1. Iterate through the sorted list of boxes.
1. Assign each box to the robot that will minimize the total search time.
1. Print the lists a and b.
