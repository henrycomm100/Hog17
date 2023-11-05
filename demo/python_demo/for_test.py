

# break 跳出 for和while循环体。任何对应的循环else块将不再执行
for i in range(1, 10):    
    print("i:",i)
    if i == 5:
        for x in range(6):
            if x == 3:
                print("x: ",x)
                break
            
    print("after break str")

print("outside top level for loop")
