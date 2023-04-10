Ian and Mary are frogs living on a grid (Cartesian coordinate plane) with integer coordinates. Ian starts at point (0,0), and Mary is at point (a, b). 

Ian wants to reach Mary in at most two jumps. Ian can only jump from one point with integer coordinates to another point with integer coordinates without landing on any other integer-coordinate point in between.

1. Ian can always reach Mary in two jumps.
1. The first jump can either be to a point on the same diagonal as Mary's position or to a point with the same x or y coordinate.
1. In this solution, Ian jumps to the point (a - 1, 1) if a > 0 or to the point (1, 1) if a = 0. This guarantees that no other integer-coordinate points are on the line segment between the starting point and the first jump point.
1. In the second jump, Ian jumps directly to Mary's position (a, b).

