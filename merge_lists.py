#merging two list with n & m number of elements
A=list(map(int,input().split()))
B=list(map(int,input().split()))
n=len(A)
m=len(B)
C=[None]*(n+m)
i=0
j=0
k=0
while(i<n and j<m):
    if(A[i]>B[j]):
        C[k]=B[j]
        k+=1
        j+=1
    else:
        C[k]=A[i]
        k+=1
        i+=1
while(i<n):
    C[k]=A[i]
    k+=1
    i+=1
while(j<m):
    C[k]=B[j]
    k+=1
    j+=1

print(C)


# merge any number of list by following different combination of matrics
      A B C D are four matrices merge them as :
                      A B C D      A B C   D
                      \ / \ /      \ / /   /
                       X   Y        X /   /
                        \ /         \/   /
                         Z           Y  /
                                      \/
                                       Z
