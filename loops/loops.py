# The provided code stub reads and integer, , from STDIN. For all non-negative integers i < n , print i.

# Example
# n = 3

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4

n = int(input())

for i in range(0, n):
    if i < n :
        print(f"{i**2}")