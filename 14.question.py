def calculator(number_x, number_y, operation):
    print(number_x + number_y)
    # print(number_x - number_y)
    # print(number_x * number_y )  # number4=number_x / number_y
    # print(number_x/number_y)
    return
    # print(number2)
    # return
    # print(number3)
    # return
    # print(number4)
    # return
calculator(25,20,"add")
# calculator(40, 3, "subtract")
# calculator(10, 4, "multiply")
# calculator(40, 4, "divide")

 
def  list_change (x,y):
    i=0
    j=0
    b=[]
    while i<len(x):
        while j<len(y):
            s=x[i]+y[i]
            b.append(s)
            break
        i=i+1
        j=j+1
    print(b)
p=[5, 10, 50, 20]
q=[2, 20, 3, 5]
list_change(p,q)


