


dictionary = open("dictionary.txt").read().split()

passCodes = [0] * 10

bloomTable = [0] * 15

def getAscii():
    for x in range(0, len(dictionary)):
        for y in range(0,len(dictionary[x])):
            passCodes[x] += ord(dictionary[x][y])

def bloom():
    for x in range(0,10):
        modVal = (passCodes[x] % 15) - 1
        bloomTable[modVal] = 1

def userIn():
    compVal = 0
    inp = input("Enter new password: ")
    if inp.isupper() == False:
        print("Only capital letters are allowed.")
        return userIn()
    for x in range(0,len(inp)):
        compVal += ord(inp[x])
    compVal = ((compVal % 15) - 1)
    if bloomTable[compVal] == 1:
        print("Password accepted.")
        
    else:
        print("Invalid password. Try again: ")
        return userIn()


def printInfo():
    for x in range(0,10):
        print(dictionary[x])
        print(passCodes[x])
    print(bloomTable)


getAscii()
bloom()

userIn()