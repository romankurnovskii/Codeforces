Mushroom Filippov is having lunch and wants to watch a video on TubeTube. He has a specific amount of time for lunch, and he wants to make the best use of it by watching the most entertaining video that fits into his lunch break.

Given a list of videos, each with its duration and entertainment value, your task is to help Mushroom Filippov choose the best video to watch. He can only watch one video, and the video must not exceed his lunch break time. 

If there are multiple videos that fit into his lunch time, choose the one with the highest entertainment value.

### Logic

Iteratee through the list of videos and checking if the video duration is less than or equal to the lunch time. If it is, you then check if the entertainment value of that video is higher than the current highest entertainment value. If it is, update the highest entertainment value and remember the index of that video. After going through all the videos, you will have the index of the most entertaining video that fits into the lunch break time.
