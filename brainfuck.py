with open('tests/test004.bf', 'r') as file:
    
    valueArray = [0]
    valuePointer = 0
    loopPositionArray = []
    asciiArray = []
    asciiMode = False
    
    singleLineProg = ""
    for line in file:
        stripLine = line.strip()
        singleLineProg = singleLineProg + stripLine

    stripLineArray = list(singleLineProg)
    currentC = -1
    maxC = len(stripLineArray)

    while currentC < maxC:
        
        currentC += 1
        if currentC >= maxC:
            break

        try:

            if stripLineArray[currentC] in (">","<","+","-",".",",","[","]","¬","?","@"):
                
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
                    if asciiMode:
                        asciiArray.append(valueArray[valuePointer])
                    else:
                        print("Return: ",valueArray[valuePointer])

                elif stripLineArray[currentC] == "[":
                    # Skip forward condition
                    if valueArray[valuePointer] == 0:
                        lookForSkip = True
                        while lookForSkip:
                            currentC += 1
                            if stripLineArray[currentC] == "]":
                                lookForSkip = False
                                print("Skipped to ",currentC)
                    else:
                        loopPositionArray.append(currentC)

                elif stripLineArray[currentC] == "]":
                    if valueArray[valuePointer] == 0:
                        print("Popped to ",currentC)
                        loopPositionArray.pop()
                    else:
                        currentC = loopPositionArray[len(loopPositionArray) - 1]

                elif stripLineArray[currentC] == "¬": # Debug
                    print("valueArray ",valueArray)
                    print("valuePointer ",valuePointer)
                    print("currentC ",currentC)
                    print("loopPositionArray ",loopPositionArray)
                    print("asciiMode ",asciiMode)
                    print("asciiArray ",asciiArray)
                
                elif stripLineArray[currentC] == "?": # Enable / Disable ASCII Prints
                    if asciiMode:
                        asciiMode = False
                    else:
                        asciiMode = True

                elif stripLineArray[currentC] == "@": # Print and Empty ASCII
                    characters = [chr(value) for value in asciiArray]
                    text = ''.join(characters)
                    print(text)
                    asciiArray = []

        except Exception as ex:
            print(ex)
            exit(1)