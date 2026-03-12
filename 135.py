def diamond3(s1):
    len1=len(s1)
    len2=len1//2
    for i in range(0,len2+1,1):
        print(" "*(len2-i)+s1[0:1+2*i])
    for i in range(1,len2+1,1):
        print(" "*i+s1[0:(len1-i)-i])
diamond3("FunwithProgrammings")
