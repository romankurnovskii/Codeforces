t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    reserved_binaries = {}
    binary_values = []

    for c in s:
        val = reserved_binaries.get(c, None)

        if not binary_values:
            binary_values.append(1)

        if val == binary_values[-1]:
            print("NO")
            break

        if not val:
            val = 1 if binary_values[-1] == 0 else 0
        reserved_binaries[c] = val

        binary_values.append(val)
    else:
        print("YES")
