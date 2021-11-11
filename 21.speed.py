def a(speed):
    # i=0 
    # b=0
    if speed<=70:
        print("ok")
    elif 70<speed:
        b=speed-70
        point=b/5
        print(point,"point")
        if point>12:
            print("licence suspend")
speed =int(input("enter the speed"))
a(speed)