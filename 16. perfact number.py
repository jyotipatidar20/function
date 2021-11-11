# def perfect():
#     num=int(input("enter the number"))
#     i=1
#     sum=0
#     while i<=num:
#         if num%i==0:
#             sum=sum+i
#         i=i+1
#     if sum==num:
#         print("perfect number")
#     else:
#         print("not perfect")
#     # num=int(input("enter the number"))
# perfect()





def perfect():
    num=int(input("inter the number"))
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i=i+1
    if sum==num:
        print("perfect number")
    else:
        print("not perfect number")
perfect()