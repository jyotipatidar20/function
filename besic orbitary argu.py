def name():
    a=input("enter the number")
    b=input("enter the number")
    c=len(a)
    d=len(b)
    if c>d:
        print(a)
    if d>c:
        print(b)
    if c==d:
        print(a)
        print(b)
name()