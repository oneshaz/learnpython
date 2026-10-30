
#works on gdb 

num1 = int(input("countdown : "))
print(num1)
j = num1 - 1
while( j > 0 ) : 
    i = 0 
    while( i < 10000000) : 
        i += 1 
    print(j)
    j -= 1
