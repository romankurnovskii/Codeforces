Cirno_9baka has a paper tape with n cells in a row. He wants to paint these cells with m different colors. Each color has to be used exactly $a_i$ times. 

There is a constraint that for every k consecutive cells, their colors have to be distinct. 

You have to determine if there is a way to paint the cells according to these conditions.

Solution Logic:

1. First, we need to check if the maximum possible color repetitions exceed the number of cells divided by k. If it does, there is no way to color the cells satisfying the conditions.
1. If the above condition is not met, we need to check if the remaining cells after applying the most frequent color can be colored with the other colors while satisfying the k consecutive cells constraint.