#############   codeforce   ##############
# problem link -> https://codeforces.com/contest/680/problem/B
'''
                                            B. Bear and Finding Criminals
                                            time limit per test2 seconds
                                            memory limit per test256 megabytes
                                            inputstandard input
                                            outputstandard output
There are n cities in Bearland, numbered 1 through n. Cities are arranged in one long row. The distance between cities i and j is equal to |i - j|.

Limak is a police officer. He lives in a city a. His job is to catch criminals. It's hard because he doesn't know in which cities criminals are. Though, he knows that there is at most one criminal in each city.

Limak is going to use a BCD (Bear Criminal Detector). The BCD will tell Limak how many criminals there are for every distance from a city a. After that, Limak can catch a criminal in each city for which he is sure that there must be a criminal.

You know in which cities criminals are. Count the number of criminals Limak will catch, after he uses the BCD.

Input
The first line of the input contains two integers n and a (1 ≤ a ≤ n ≤ 100) — the number of cities and the index of city where Limak lives.

The second line contains n integers t1, t2, ..., tn (0 ≤ ti ≤ 1). There are ti criminals in the i-th city.

Output
Print the number of criminals Limak will catch.
'''

################# Code ##########################

# INPUT
n,a = map(int,input().split())
ls=list(map(int,input().split()))

l=r=a-1
counter=0
# frist check if there are criminal in city that he live
if ls[a-1]==1:
    counter+=1

while l>=0 or r<n:
    l-=1
    r+=1
    # if there are cities in left and right
    if l>=0 and r<n:
        if ls[l]==1 and ls[r]==1 :
            counter +=2
    # if there are cities in left only
    elif l>=0:
        if ls[l]==1:
            counter+=1
    # if there are cities in right only
    elif r<n:
        if ls[r]==1:
            counter +=1

# output
print(counter)



