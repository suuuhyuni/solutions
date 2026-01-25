
num = int(input())

queue = []
output = []

for _ in range(num) :

    input_func = input().split()

    if input_func[0] == "push" :
        queue.append(input_func[1])
        
    elif input_func[0] == "pop" :
        if len(queue) == 0 :
            output.append('-1')
        else :
            output.append(queue.pop(0))
    
        
    elif input_func[0] == "size" :
        output.append(str(len(queue)))
        
    elif input_func[0] == "empty" :
        output.append('1' if len(queue) == 0 else '0')
        
    elif input_func[0] == "front" :
        output.append(queue[0] if len(queue) != 0 else '-1')
        
    elif input_func[0] == "back" :
        output.append(queue[-1] if len(queue) != 0 else '-1')

print('\n'.join(output))