import math
def travel(arraylength, arrayheight):
    current = ''
    options =["e", "s"]

    for i in range(arraylength+arrayheight-1):
        oldoptions = options
        options = []
        for path in oldoptions:
            options.append(path+"e")
            options.append(path+"s")

    return(trim(arraylength, arrayheight, options))

def trim(arraylength, arrayheight, options):
    valid = []
    for path in options:
        e_count = 0
        s_count = 0
        for i in range(len(path)):
            if path[i] == "e": e_count +=1
            elif path[i] == "s": s_count += 1
        if e_count == arraylength and s_count == arrayheight: valid.append(path)
    return(valid)

def main():
    length = int(input("how far do you have to travel horizontally? "))
    height = int(input("how far do you have to travel vertically? "))
    paths = int(math.factorial(length+height)/(math.factorial(length)*math.factorial(height)))
    print ("There are",paths,"ways to travel.")
    choice = input("Would you like to see them? (Yes or No): ").lower()
    if choice == "yes":
        result = travel(length, height)
        print(result)
        print("there are ",len(result),"ways to travel")
    elif choice == "no":
        print("ok!")
    else:
        print("error")

main()
