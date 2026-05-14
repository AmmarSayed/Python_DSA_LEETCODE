'''
drop non-dominants

O(n^2 + n) = O(n^2)

'''

# example of O(n^2 + n)
def print_items(n):
    for i in range (n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)


print_items(5)


'''
0 0
0 1
0 2
0 3
0 4
1 0
1 1
1 2
1 3
1 4
2 0
2 1
2 2
2 3
2 4
3 0
3 1
3 2
3 3
3 4
4 0
4 1
4 2
4 3
4 4
0
1
2
3
4

That's a total of 25 lines from the first loop (5 * 5) and 5 lines from the second loop, making it 30 lines in total. The time complexity is O(n^2 + n), which simplifies to O(n^2) since n^2 grows faster than n as n increases. so the last loop is dropped as it is non-dominant, they are just 5 extra operations compared to the dominant O(n^2) term.
'''