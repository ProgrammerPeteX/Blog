# This is my first comment
dj = "\nHello, Django girls!\n"
condition = 0
if condition == 0:
    print(dj)
elif condition > 0:
    print("meh\n")
else:
    print(':(\n')

def areYouBlack(hmm):
    if hmm == "no":
        print("no")
    elif hmm == "nigga":
        print("yes nigga")

areYouBlack("nigga")

list = ['a', 'b', 'c', 'd', 'wtf? you broke the patter']

print("\n")

for thing in list:
    print(thing)

print("\n")

def isBlack(blackList):
    nig = " is black\n"
    not_nig = " is white"
    for name in blackList:
        if name != "Peter":
            print(name + nig)
        else:
            print(name + not_nig)

nameList = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Peter']

isBlack(nameList)

print("\n")
        