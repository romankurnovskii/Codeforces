There are `n` players in a game with temperature values ranging from `1` to `n`. 

- The game has `n-1` environments, each of which is either type `0` or type `1`. 
- If an environment is type `0`, the player with a lower temperature value wins, and if it's type `1`, the player with a higher temperature value **wins**. 
- The game is played in a tournament format, with players battling until only one player remains.

For each `x` from `2` to `n`, you need to determine how many players have a chance to win if all players with temperature values not exceeding `x` participate in the game.

Solution Logic:

1. Initialize a counter and a result list.
1. Loop through the range from `1` to `n-1`.
1. If the current environment type is the same as the previous one, increment the counter.
1. If the environment type is different, reset the counter to `1`.
1. Append the current `index + 2 - counter` to the result list.
1. Print the result list.