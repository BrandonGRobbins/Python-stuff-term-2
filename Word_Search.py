attempts=0

print("Python terms")
puzzle= ("fjvfloatdyyopxedninsmspfycnnalxeaeeukgeislufryprlcabeeiagco"+
         "ibuclqttbongojlivxobgadmyahgerjstringwvrs")
def display_puzzle():
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:])
    print()

print()

#display the puzzle
display_puzzle()
print("word list")
word_list="float, while, if, boolean, double, operators, string, slicing, index"
print(word_list)
print()

#getting the lengths of the words
word1_length=len("float")
word2_length=len("while")
word3_length=len("if")
word4_length=len("boolean")
word5_length=len("double")
word6_length=len("operators")
word7_length=len("string")
word8_length=len("slicing")
word9_length=len("index")
#getting players answer
x=0
while x==0:
    word1=input("enter the index positions of float")
    attempts+=1
    i=0
    foundword=""
    while i<word1_length:
        index=word1[i]
        index=int(index)
        foundword=foundword+puzzle[index]
        i+=1
    if foundword=="float":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that was not correct try again")

x=0
while x==0:
    word1=input("enter the positions of while")
    attempts+=1
    i=0
    foundword=""
    while i<word2_length*2:
        index=word1[i:i+2]
        index=int(index)
        foundword=foundword+puzzle[index]
        i+=2
    if foundword=="while":
        print(foundword)
        print("great job")
        x=1
    else:
        print("that was not correct try again")
