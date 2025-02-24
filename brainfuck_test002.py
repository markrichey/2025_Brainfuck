with open('test002.bf', 'r') as file:
    
    valueArray = [0]
    valuePointer = 0
    loopPositionArray = []
    
    singleLineProg = ""
    for line in file:
        stripLine = line.strip()
        singleLineProg = singleLineProg + stripLine

    stripLineArray = list(singleLineProg)
    currentC = -1
    maxC = len(stripLineArray)
    print("Max C:",maxC)

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
                elif stripLineArray[currentC] == "[":
                    loopPositionArray.append(currentC)
                    print(loopPositionArray)
                elif stripLineArray[currentC] == "]":
                    if valueArray[valuePointer] == 0:
                        loopPositionArray.pop()
                        print(loopPositionArray)
                    else:
                        print("Set currentC to ",loopPositionArray[len(loopPositionArray) - 1])
                        currentC = loopPositionArray[len(loopPositionArray) - 1]

        except:
            break
        
    print(valueArray)
                