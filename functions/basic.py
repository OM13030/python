def avg(a,b,c):
    d = (a+b+c)/3
    print(d)

avg(1,2,3)

#arguements in python functions

def add(a,b,plus = 0):
    x = a + b + plus
    return x

c = add(2,3,4) 
# 4 will override the default value of    plus which is zero
print(c)

#key word arguements
c1 = add(b = 5 , a = 6)
# since i have mentioned i can pass in any order