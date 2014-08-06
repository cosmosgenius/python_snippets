def findOperations(inputString) :
    length = len(inputString)
    if(length == 2):
        return abs(ord(inputString[0]) - ord(inputString[1])) 
    if(length == 1):
        return 0

    lengthhalf = length//2 if length % 2 ==0 else length//2 + 1
    total = 0
    for x in range(lengthhalf) :
        diff = abs(ord(inputString[x]) - ord(inputString[length - x - 1]))
        total += diff

    return total

noofinput = list(map(int, input().split()))

outputs = []

for x in range(noofinput[0]) :
    inputStr = input()
    outputs.append(findOperations(inputStr))

for x in outputs:
    print (x)
