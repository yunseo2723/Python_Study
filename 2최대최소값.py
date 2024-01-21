def solution(s):
    answer = ''
    s = s.split()
    a = int(s[0])
    b = int(s[0])
    
    for i in range(0,len(s),1):
        if int(s[i]) > a :
            a = int(s[i])
    
    for i in range(1,len(s), 1):
        if int(s[i]) < b :
            b = int(s[i])
    
    answer = f"{b} {a}"
    
    return answer