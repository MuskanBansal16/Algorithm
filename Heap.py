def heapyfy(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2
    if(left<n and arr[largest]<arr[left]):
        largest=left
    if(right<n and arr[largest]<arr[right]):
        largest=right
    
    if(largest!=i):
        arr[i],arr[largest]=arr[largest],arr[i]
        heapyfy(arr,n,largest)

def heapsort(arr,n):
    for i in range(n,-1,-1):
        heapyfy(arr,n,i)
    
    for i in range(n-1,-1,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapyfy(arr,i,0)

arr=list(map(int,input().split()))
n=len(arr)
heapsort(arr,n)
print(arr)
