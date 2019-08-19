#recurvsive algo



def Merge(arr,low,mid,high):
    temp=[None]*(high-low+1)
    i=low
    j=mid+1 
    k=0
    while(i<=mid and j<=high):
        if(arr[i]<arr[j]):
            temp[k]=arr[i]
            k=k+1 
            i=i+1 
        else:
            temp[k]=arr[j]
            k=k+1 
            j=j+1 
    while(i<=mid):
        temp[k]=arr[i]
        k=k+1 
        i=i+1
    while(j<=high):
        temp[k]=arr[j]
        k=k+1 
        j=j+1 
    
    for i in range(low,high+1):
        arr[i] = temp[i-low]
        
def MergeSort(arr,low,high):
    if(low<high):
        mid = int((low+high)/2)
        MergeSort(arr,low,mid)
        MergeSort(arr,mid+1,high)
        Merge(arr,low,mid,high)
    
        
        
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
MergeSort(arr,low,high)
print(arr)
