def solve():
    s = input()
    min_operations = float('inf')

    for i in range(26):
        current_char = chr(97 + i)
        substrings = s.split(current_char)

        max_operations_for_char = 0
        for substring in substrings:
            length = len(substring)
            operations = 0

            # smallest power of 2 that is greater than or equal to the len of substr
            while length > 0:
                length //= 2
                operations += 1

            max_operations_for_char = max(max_operations_for_char, operations)

        min_operations = min(min_operations, max_operations_for_char)

    print(min_operations)


for _ in range(int(input())):
    solve()
