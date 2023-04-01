Hateehc is a Martian blogger who wants to buy a starship with the luckiest number. The luckiness of a number is the difference between its largest and smallest digits. 

For example, the luckiness of the number `142857` is `8 - 1 = 7`, and the luckiness of the number `111` is `0` because all its digits are the same.

In a store, there are starships with numbers from `𝑙` to `𝑟`. You need to help Hateehc find the starship with the luckiest number.

Logic to solve the problem:

1. Iterate through the range of starship numbers `[𝑙, 𝑟]`.
1. For each number in the range, find the luckiness (the difference between the largest and smallest digits).
1. Keep track of the maximum luckiness found so far and the corresponding starship number.
1. Stop the iteration if the maximum luckiness is equal to 9, as this is the highest possible luckiness.
1. Return the starship number with the highest luckiness.
