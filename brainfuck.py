with open('test001.bf', 'r') as file:
    
    valueArray = [0]
    valuePointer = 0
    
    for line in file:
        stripLine = line.strip()
        stripLineArray = list(stripLine)
        
        for cmd in stripLineArray:
            if cmd in (">","<","+","-",".",",","[","]"):
                print(cmd)