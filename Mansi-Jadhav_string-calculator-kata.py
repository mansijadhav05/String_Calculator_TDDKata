def test():
    #Empty String
    assert(add("")==0),"Empty String doesn't return 0"
    # 1 Number
    assert(add("1")==1),"String \"1\"doesn't return 1"
    assert(add("2")==2),"String \"2\"doesn't return 2"
    

    #2Number
    assert(add("1,2")==3),"String \"1,2\"doesn't return 3"
    assert(add("2,3")==5),"String \"2,3\"doesn't return 5"

    #3 Numbers
    assert(add("1,2,3")==6),"String \"1,2,3\"doesn't return 6"
    assert(add("2,3,6")==11),"String \"2,3,6\"doesn't return 11"

    #4 Numbers
    assert(add("1,2,3,4")==10),"String \"1,2,3,4\"doesn't return 10"
    assert(add("1,4,5,6")==16),"String \"1,2\"doesn't return 16"
   

   
    #Add method to Handle New line
    assert(add("1\n2")==3),"String \"1\n2\"doesn't return 3"
    assert(add("3\n4")==7),"String \"3\n4\"doesn't return 7"

    #Handle Different Delimeter
    assert(add("//;\n1,2,3")==6),"String \"//;\n1,2,3\"doesn't return 6"

    print ("Passed All Tests")

def add(numbersString):
    if len(numbersString)==0:
        return 0
    elif len(numbersString)==1:
        return int(numbersString)
    elif numbersString[0]=="/":
        return 0
    delimstart=2
    global delimstart
    delim=numbersString[delimstart]
    while numbersString[(delimstart+1)] !="\\":
        delim=delim+numbersString[delimStart]
        delimStart += 1
    numbers=numbersString.split("\n")[1].split(delim)
    return multipleNumbers(numbers)

    else:
        return 0
        delim=","
        if numbersString[1] !=",":
            delim="\n"
            #numbers=numbersString.split(delim)
            #for num in numbers:
                #result += int(num)
            return multipleNumbers(numbersString,delim)

    

def multipleNumbers(numbersString,delim):
    result = 0
    numbers=numbersString.split(denim)
    for num in numbers:
        result += int(num)
        return result

test()
