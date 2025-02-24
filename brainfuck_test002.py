with open('test001.bf', 'r') as file:
    
    valueArray = [0]
    valuePointer = 0
    
    for line in file:
        
        stripLine = line.strip()
        stripLineArray = list(stripLine)

        maxC = len(stripLineArray)
        currentC = -1
        
        while currentC < maxC:

            currentC += 1

            try:

                if stripLineArray[currentC] in (">","<","+","-",".",",","[","]"):
                    
                    if stripLineArray[currentC] == ">":
                        valuePointer += 1
                        if len(valueArray) < (valuePointer + 1):
                            valueArray.append(0)
                    elif stripLineArray[currentC] == "<":
                        valuePointer -= 1
                        if len(valueArray) < (valuePointer + 1):
                            valueArray.append(0)

                    elif stripLineArray[currentC] == "+":
                        valueArray[valuePointer] += 1
                    elif stripLineArray[currentC] == "-":
                        valueArray[valuePointer] -= 1
                    elif stripLineArray[currentC] == ".":
                        print(valueArray[valuePointer])

            except:
                break


    print(valueArray)
                