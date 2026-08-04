#This is a calculator
while True:
    j=int(input("enter first number:"))
    k=int(input("enter the second number:"))
    
    e=input("+,-,*,/:-")
    a="+"
    b="-"
    c="*"
    d="/"
    if e==a:
        print(j+k)
    elif e==b:
        print(j-k)
    elif e==c:
        print(j*k)
    else:
        print(j/k)
    z=input("Do you want to calculate again?")
    if z=="yes" and "Yes" and "YES":
        pass
    elif z=="no" and "NO" and "No":
        print("Thank You for using this calculator")
        break

