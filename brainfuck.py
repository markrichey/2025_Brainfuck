
import sys

with open(sys.argv[1], 'r') as file:
    
    valueArray = [0]
    valuePointer = 0
    loopPositionArray = []
    asciiArray = []
    asciiMode = False
    argumentNumber = 1
    
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
                        loopPositionArray.append(currentC)
                        while lookForSkip:
                            currentC += 1
                            if stripLineArray[currentC] == "]":
                                loopPositionArray.pop()
                                if len(loopPositionArray) == 0:
                                    lookForSkip = False
                            elif stripLineArray[currentC] == "[":
                                loopPositionArray.append(currentC)
                    else:
                        loopPositionArray.append(currentC)

                elif stripLineArray[currentC] == "]":
                    if valueArray[valuePointer] == 0:
                        loopPositionArray.pop()
                    else:
                        currentC = loopPositionArray[len(loopPositionArray) - 1]

                elif stripLineArray[currentC] == ",":
                    argumentNumber += 1
                    valueArray[valuePointer] = int(sys.argv[argumentNumber])

                elif stripLineArray[currentC] == "¬": # Debug
                    print("valueArray ",valueArray)
                    print("valuePointer ",valuePointer)
                    print("currentC ",currentC)
                    print("loopPositionArray ",loopPositionArray)
                    print("asciiMode ",asciiMode)
                    print("asciiArray ",asciiArray)
                    print("argumentNumber ",argumentNumber)
                
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
            print("valueArray ",valueArray)
            print("valuePointer ",valuePointer)
            print("currentC ",currentC)
            print("loopPositionArray ",loopPositionArray)
            print("asciiMode ",asciiMode)
            print("asciiArray ",asciiArray)
            print("argumentNumber ",argumentNumber)
            exit(1)