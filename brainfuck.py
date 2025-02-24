with open('test001.bf', 'r') as file:
    
    valueArray = [0]
    valuePointer = 0
    loopingArray = []
    
    for line in file:
        
        stripLine = line.strip()
        stripLineArray = list(stripLine)
        
        for cmd in stripLineArray:
            if cmd in (">","<","+","-",".",",","[","]"):
                
                if cmd == ">":
                    valuePointer += 1
                    if len(valueArray) < (valuePointer + 1):
                        valueArray.append(0)
                elif cmd == "<":
                    valuePointer -= 1
                    if len(valueArray) < (valuePointer + 1):
                        valueArray.append(0)

                elif cmd == "+":
                    valueArray[valuePointer] += 1
                elif cmd == "-":
                    valueArray[valuePointer] -= 1
                elif cmd == ".":
                    print(valueArray[valuePointer])

    print(valueArray)
                