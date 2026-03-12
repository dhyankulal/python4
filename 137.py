def quiz1(fname):
    countries=[]
    capitals=[]
    marks=[]
    count=10
    f1=open(fname,"r")
    for i in range(0,count,1):
        s1=f1.readline().strip()
        list1=s1.split(",")
        countries.append(list1[0])
        capitals.append(list1[1])
    for i in range(0,count,1):
        r1=input("What is the capital of"+countries[i])
        if r1==capitals[i]:
            marks.append(10)
        else:
            marks.append(0)
    print(marks)
    print("You have scored",sum(marks),"marks")
    for i in range(0,count,1):
        if marks[i]==0:
            print("The correct answer for question",i+1," is :",capitals[i])
quiz1("gk1.txt")
