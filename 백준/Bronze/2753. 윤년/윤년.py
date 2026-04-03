year = int(input())

#윤년 : 4의 배수 and (100의 배수 or 400의 배수)

if year % 4 == 0 :
    if year % 100 != 0 or year % 400 == 0 :
        print("1")
    else :
        print("0")
else :
    print("0")
