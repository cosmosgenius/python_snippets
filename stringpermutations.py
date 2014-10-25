print("Enter the string you want to find permutation for")
inputstr = input(">")
def findPermutation(str):
    return permute(list(str))

def permute(list):
    if len(list) == 1 :
        return list

    retlist = []

    for x in list:
        listcopy = list[:]
        listcopy.remove(x)
        for y in permute(listcopy):
            retlist.append(x+y)
    return retlist

        
def tostr(list):
    retstr = ''
    for x in list:
        retstr += x
    return retstr


#for x in findPermutation(inputstr):
#    print(x)
print(len(findPermutation(inputstr)))