def x():
    x = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
    i=0
    for i in range(0,10):
        for j in range(0,9):
            if x[j] > x[j+1]:
                y=x[j]
                x[j]=x[j+1]
                x[j+1]=y
            j=j+1
        i=i+1
    print(x)
x()
