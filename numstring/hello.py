import copy
hello = int(input("please neter "))
apple = [1,2,3,4,5,6,7,8]
banana = copy.copy(apple)
for _ in range(hello):
    print (banana)
