def solution(arr):
    answer = 0
    result = 0
    
    for i in range(0, len(arr), 1):
        result += arr[i]
        
    answer = result / len(arr)
    
    return answer

def solution2(arr):
    answer = 0
    
    answer = sum(arr)/len(arr)
    
    return answer