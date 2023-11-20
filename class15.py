

n = "hamza"
y = 15

try:
    print(n / y)

except  TypeError as error:

    n = 0 
    try:
        print( y / n)

    except Exception as error: 

        n = 3

        print(y / n)  

else:
    print("code god")  

