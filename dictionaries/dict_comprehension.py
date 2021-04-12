# Write a function that returns a dictionaryh with keys being the first 100 natural numbers and for values, those numbrs but pow 3 


import math 


def cubeItList():
    return [math.pow(i,3) for i in range(1,101)]

def cubeItDict():
    return {i: math.pow(i,3) for i in range(1,101)}

def run():
    print(f"{cubeItList()}\n")
    print(f"{cubeItDict()}\n")




if __name__ == "__main__":
    run()
