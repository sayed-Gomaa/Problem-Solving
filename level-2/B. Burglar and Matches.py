#############   codeforce   ##############
# problem link -> https://codeforces.com/contest/16/problem/B
'''
                                           B. Burglar and Matches
time limit per test0.5 second
memory limit per test64 megabytes
inputstandard input
outputstandard output
A burglar got into a matches warehouse and wants to steal as many matches as possible. In the warehouse there are m containers, in the i-th container there are ai matchboxes, and each matchbox contains bi matches. All the matchboxes are of the same size. The burglar's rucksack can hold n matchboxes exactly. Your task is to find out the maximum amount of matches that a burglar can carry away. He has no time to rearrange matches in the matchboxes, that's why he just chooses not more than n matchboxes so that the total amount of matches in them is maximal.

Input
The first line of the input contains integer n (1 ≤ n ≤ 2·108) and integer m (1 ≤ m ≤ 20). The i + 1-th line contains a pair of numbers ai and bi (1 ≤ ai ≤ 108, 1 ≤ bi ≤ 10). All the input numbers are integer.

Output
Output the only number — answer to the problem.
'''

################# Code ##########################

# INPUT
n,m = map(int , input().split())
ls=[]
for i in range(m):
    a,b=map(int ,input().split())
    ls.append([a,b])

ls.sort(key = lambda x: x[1],reverse=True)
flag=True
i=0
matches=0
while flag:
    if n >= ls[i][0]:
        matches+=ls[i][0]*ls[i][1]
        n-=ls[i][0]
    else:
        matches += n * ls[i][1]
        n = 0
        break
    i+=1
    if n<1 or i>=m:
        flag=False
 # output
print(matches)

