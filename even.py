def evenisodd(n):
    if (n^1==n+1):
        return True
    else:
        return False
number=int(input("Enter a number: "))
if evenisodd(number):
    print("number97 is even")
else:
    print("number is odd")