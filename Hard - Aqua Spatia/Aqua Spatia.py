def collectedWater(arr,n):
        
    left = [0]*n
    right = [0]*n

    left[0] = arr[0]
    right[n-1] = arr[n-1]
    trap_sum = 0
        
    for i in range (1 , n):
        left[i] = max(left[i-1] , arr[i])
    for i in range(n-2 , -1 , -1):
        right[i] = max(arr[i] , right[i+1])
    for i in range (0 , n):
        trap_sum += min(left[i] , right[i]) - arr[i]
                
    return trap_sum

total_volume = 0

with open("inputs.txt", "r") as input_file:
    
    T = int(input_file.readline().strip())
    
    for i in range(T):

        n_line = input_file.readline().strip()
        
        n = int(n_line)
        
        arr_line = input_file.readline().strip()
        arr = list(map(int, arr_line.split()))
        
        result = collectedWater(arr, n)
        total_volume += result
        
        print(result)
    
    print("A total of " + str(total_volume) + " units of water have been collected.")