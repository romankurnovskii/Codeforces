You are given a tree with 'n' nodes, where each node has a value of either `0` or `1` at time `t=0`. 

At every subsequent time step, the value of a node becomes the **bitwise XOR** of the values of its children at the previous time step. 

The goal is to find the sum of the values of all nodes at every time step until `t=10^100` for all `2^n` possible initial configurations of the tree. 

The final answer should be the sum of these values `modulo 10^9+7`.

**Logic:**

The XOR operation propagates the values in the tree from the leaves **towards the root**. 

The maximum number of time steps required to propagate the values to the root is the **depth of the tree**. 

We can:
1. compute the depth of each node using depth-first search ([DFS](http://romankurnovskii.com/en/tracks/algorithms-101/algorithms/#depth-first-search-dfs))
2. calculate the sum of the depths
3. finally multiply the sum by 2^(n-1) to account for all possible configurations.

**Naive approach:**

A naive approach would be to iterate over all possible initial configurations of `0s` and `1s` and perform the XOR operation on the tree for every time step, up to a large number (e.g., 10^100), and sum the values of all nodes.
