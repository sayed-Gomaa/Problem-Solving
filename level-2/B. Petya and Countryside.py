n= int(input())
ls=list(map(int,input().split()))

max=0
counter=0
for i in range(n):
        l=r=i
        counter=0
        flag=True
        # compare left
        while flag:
            l -= 1
            if l>=0:
                if ls[l+1]>=ls[l]:
                     counter+=1
                else: flag=False
            else: flag=False

        # compare right
        flag=True
        while flag:
            r += 1
            if r< n:
                if ls[r-1] >= ls[r]:

                        counter += 1
                else:
                    flag=False
            else:
                flag = False
        if counter>max:
             max=counter
print(max+1)