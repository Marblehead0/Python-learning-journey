with open("../../notes/day11.txt","w") as f:
    f.write("Gotta learn fast!\n")

with open("../../notes/day11.txt","r") as f:
    print(f.read())

def writeNameInFile():
    print("What your name?")
    name = str(input())
    with open("../../notes/name.txt","w") as f:
        f.write(name + "\n")
    with open("../../notes/name.txt","r") as f:
        print(f.read())

writeNameInFile()