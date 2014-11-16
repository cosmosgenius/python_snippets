print("Enter the string you want to find permutation for")
inputstr = input(">")

numtime = 0


def findPermutation(str):
    global numtime
    numtime = 0
    return permute(list(str), {})


def permute(list, memo):
    global numtime
    numtime += 1
    if(tostr(list) in memo):
        return memo[tostr(list)]

    if len(list) == 1:
        return list

    retlist = []

    for x in list:
        listcopy = list[:]
        listcopy.remove(x)
        for y in permute(listcopy, memo):
            retlist.append(x+y)
    memo[tostr(list)] = retlist
    return retlist


def tostr(list):
    retstr = ''
    for x in list:
        retstr += x
    return retstr


# for x in findPermutation(inputstr):
#     print(x)
print(len(findPermutation(inputstr)))
print (numtime)
