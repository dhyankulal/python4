f1=open("marks.txt","r")
names=[]
subjects=[]
sub1=[]
sub2=[]
total=[]
toppersSub1=[]
toppersSub2=[]
goldmedalist=[]
for i in range(0,26,1):
    s1=f1.readline()
    list1=s1.split(",")
    names.append(list1[0])
    
    list2=list1[3].split(":")
    sub1.append(int(list2[1]))
    subjects.append(list2[0])

    list2=list1[4].split(":")
    sub2.append(int(list2[1]))
    subjects.append(list2[0])

    total.append(sub1[i]+sub2[i])
    
maxSub1=max(sub1)
maxSub2=max(sub2)
#print(names)
#print(sub1)
#print(sub2)
for i in range(0,26,1):
    if sub1[i]==maxSub1:
        toppersSub1.append(names[i])

    if sub2[i]==maxSub2:
        toppersSub2.append(names[i])
print(toppersSub1,"are the toppers in ",subjects[0]," with marks",maxSub1)
print(toppersSub2,"are the toppers in ",subjects[1]," with marks",maxSub2)
print(total)
