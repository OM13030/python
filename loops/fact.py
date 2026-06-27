n = int(input("tyoe the numbher you want the factorial of : "))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("factorial : ", fact)