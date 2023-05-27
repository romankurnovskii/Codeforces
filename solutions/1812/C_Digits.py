pi = "314159265358979323846264338327950288419716939937510"

for i in range(int(input())):
    res = 1
    for _ in range(int(pi[i])):
        res *= int(input())
    print(res)
