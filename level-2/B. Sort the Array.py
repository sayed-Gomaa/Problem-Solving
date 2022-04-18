n=int(input())
ls=list(map(int,input().split()))
srt=sorted(ls)
l=r=0
for i in range(n):
    if ls[i]!=srt[i]:
        l=i
        break
for i in range(n-1,-1,-1):
    if ls[i]!=srt[i]:
        r=i
        break
rv=ls[l:r+1][::-1]
if l==r:
    print('yes')
    print(1,1)
elif srt[l:r+1]==rv:
    print('yes')
    print(l+1,i+1)
else:
    print('no')