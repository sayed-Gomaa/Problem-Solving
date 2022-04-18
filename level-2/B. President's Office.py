#############   codeforce   ##############
# problem link -> https://codeforces.com/contest/6/problem/B
'''

                    B. President's Office
                    time limit per test2 seconds
                    memory limit per test64 megabytes
                    inputstandard input
                    outputstandard output
President of Berland has a very vast office-room, where, apart from him, work his subordinates. Each subordinate, as well as President himself, has his own desk of a unique colour. Each desk is rectangular, and its sides are parallel to the office walls. One day President decided to establish an assembly, of which all his deputies will be members. Unfortunately, he does not remember the exact amount of his deputies, but he remembers that the desk of each his deputy is adjacent to his own desk, that is to say, the two desks (President's and each deputy's) have a common side of a positive length.

The office-room plan can be viewed as a matrix with n rows and m columns. Each cell of this matrix is either empty, or contains a part of a desk. An uppercase Latin letter stands for each desk colour. The «period» character («.») stands for an empty cell.

Input
The first line contains two separated by a space integer numbers n, m (1 ≤ n, m ≤ 100) — the length and the width of the office-room, and c character — the President's desk colour. The following n lines contain m characters each — the office-room description. It is guaranteed that the colour of each desk is unique, and each desk represents a continuous subrectangle of the given matrix. All colours are marked by uppercase Latin letters.

Output
Print the only number — the amount of President's deputies.

'''

################# Code ##########################

# INPUT
n, m, c= input().split()
n=int(n)
m=int(m)
ls=[]
for i in range(n):
    l=input()
    ls.append(l)
deputies=[]
for i in range(n):
    for j in range(m):
        if ls[i][j]==c:
        # horizntal deputies
            # left
            if j>0:
                if ls[i][j-1] !='.' and ls[i][j-1] != c and ls[i][j-1] not in deputies:
                    deputies.append(ls[i][j-1])
            # right
            if j < m-1:
                if ls[i][j + 1] != '.' and ls[i][j + 1] != c and ls[i][j + 1] not in deputies:
                    deputies.append(ls[i][j + 1])
        # vertical deputies
            # left
            if i > 0:
                if ls[i-1][j] != '.' and ls[i-1][j] != c and ls[i-1][j] not in deputies:
                    deputies.append(ls[i-1][j])
            # right
            if i < n-1:
                if ls[i+1][j] != '.' and ls[i+1][j] != c and ls[i+1][j] not in deputies:
                    deputies.append(ls[i+1][j])

print(len(deputies))



