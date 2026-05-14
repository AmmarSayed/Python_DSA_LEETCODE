def print_items(n):
    for i in range (n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

print_items(4)

# The time complexity of this function is O(n^3) because there are three nested loops, each iterating n times. The total number of iterations is n * n * n = n^3.
''' 
sample output:
n^3 = 4^3 = 64

print_items(4) will print 64 lines, each line containing a combination of i, j, and k values from 0 to 3. The output will look like this:

    0 0 0
    0 0 1
    0 0 2
    0 1 0
    0 1 1
    0 1 2
    0 2 0
    0 2 1
    0 2 2
    1 0 0
    1 0 1
    1 0 2
    1 1 0
    1 1 1
    1 1 2
    1 2 0
    1 2 1
    1 2 2
    2 0 0
    2 0 1
    2 0 2
    2 1 0
    2 1 1
    2 1 2
    2 2 0
    2 2 1
    2 2 2
    3 0 0
    3 0 1
    3 0 2
    3 1 0
    3 1 1
    3 1 2
    3 2 0
    3 2 1
    3 2 2
    3 3 0
    3 3 1
    3 3 2
    3 3 3
    
'''