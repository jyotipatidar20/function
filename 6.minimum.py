def list():
    list = [8, 6, 4, 8, 4, 50, 2, 7]
    min=list[0]
    for i in list:
         if i<min:
          min=i
    print(min,"minimum number")
list()