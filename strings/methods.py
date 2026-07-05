name = "omgajera1234" # strings are immutable
a = len(name)
print(a)

print(name.upper())
print(name.lower())
print(name.capitalize())


text = '  hello world  and python is fun'
print(text.strip()) 
print(text.lstrip())
print(text.rstrip())

print(text.find("is"))
print(text.replace("fun", "awesome"))


text1 = 'Apples,Banana,Pinaple'
print(text1.split(","))