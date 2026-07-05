# String formatting

template = 'hey {} you are good so take this {}$ bag and enjoy'
a = 'yash'
a1 = 10000
b = 'jack'
b1 = 1000
c = 'sanjay'
c1 = 300

s1 = template.format(a,a1)
s2 = template.format(b,b1)
s3 = template.format(c, c1)
print(s3)

print(f"{a} you are good and take this {a1}$ bag")
