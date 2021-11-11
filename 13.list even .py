def check_numbers_list(a,b) :
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both list are divisible")
        else:
            print("not divisible")
        i=i+1
check_numbers_list([2, 6, 18, 10, 3, 75] , [6, 19, 24, 12, 3, 87])
