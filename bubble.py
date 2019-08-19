def bubbleSort(arr): 
    n = len(arr) 
  
     
    for i in range(n): 
      Swap=False
  
         
        for j in range(0, n-i-1): 
            
            
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                Swap=True
            if(Swap==False):
                break
  
 
arr=list(map(int,input().split()))  
bubbleSort(arr) 
print(arr)  
