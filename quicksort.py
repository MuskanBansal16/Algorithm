def pivott(arr,low,high):
    i=low
    j=high
    pivot=arr[low]
    while(i<j):
        
        while True:
            i=i+1 
            if(arr[i]>=pivot):
                break
        while True:
            j=j-1
            if(arr[j]<=pivot):
                break
        if(i<j):
            arr[i],arr[j]=ar[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return(j)
    
def quicksort(arr,low,high):
    if(low<high):
        j=pivott(arr,low,high)
        quicksort(arr,low,j)
        quicksort(arr,j+1,high)
        
        
arr=[1,5,2,4,7,8,9]

low=0
high=len(arr)-1
quicksort(arr,low,high)
print(arr)
