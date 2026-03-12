'''
Andaman  Prisoner  Problem
There are 100 prison cells in a row. All cells are locked. Jailer is given permission by the Prime Minister of India to release any number of prisoners. 
In Round 1, Jailer opens all the doors.   
In Round 2, he closes every alternate door (2, 4, 6...).  
In Round 3, every third door (3, 6, 9,....) if Door is Open,, he closes it.   If Door is Closed, he opens it.  
In Round 4, every fourth door (4, 8, 12..), if Door is open, he closes it.  If Door is Closed, he opens it.  
He does this for 100 Rounds.  At the end, who are the lucky prisoners ?  
'''
count=100
prison=["C"]*count
lucky=[]
for i in range(0,count,1):
    prison[i]="O"
for i in range(1,count,2):
    prison[i]="C"
for j in range(2,count,1):   
    for i in range(j,count,j+1):
        if prison[i]=="C":
            prison[i]="O"
        else:
            prison[i]="C"
for i in range(0,count,1):
    if prison[i]=="O":
        lucky.append(i+1)
print(lucky,"are the lucky prisoners")
