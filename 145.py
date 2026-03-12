import random as rd
pwd1=""
s1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s2="abcdefghijklmnopqrstuvwxyz"
d1="0123456789"
upper=list(s1)
lower=list(s2)
digits=list(d1)
full=upper+lower+digits

rd1=rd.randint(0,25)
pwd1=pwd1+upper[rd1]

rd1=rd.randint(0,25)
pwd1=pwd1+lower[rd1]

rd1=rd.randint(0,9)
pwd1=pwd1+digits[rd1]

for i in range(0,5,1):
    rd1=rd.randint(0,61)
    pwd1=pwd1+full[rd1]
list1=list(pwd1)
rd.shuffle(list1)
pwd2="".join(list1)

print(pwd2)
