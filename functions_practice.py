# 1

def hello(): 
    print("Hello, user!")

#2

def pack(a,b,c):
    return[a,b,c]

#3

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i ==0:
                print(f"first I eat {my_list[0]}")
            else:
                print(f"next I eat {my_list[i]}")
hello()
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])