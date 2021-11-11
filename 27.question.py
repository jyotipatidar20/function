name =input("enter the number")
i=0
while i<len(name):
    print(name.upper()[i],end=" ")
    if i!=len(name):
        print("_",end=" ")
    print(name.lower()[i],end=" ")
    print()
    i=i+1