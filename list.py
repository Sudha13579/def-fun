#############################list inside list#######################################
'''l1=[1,2,3,4,5,[2,4,7,8,9,80]]
for i in range(len(l1)):
    if i==5:
        for j in range(len(l1[i])):
            print(l1[i][j],end=" ")
    print(l1[i],end=" ")'''
######################################################list inside dictionary############################
'''l1=[{"name":"sudha","rollno":32,"average":30.0},{"name":"ravi","rollno":34,"average":40}]
for i in range(len(l1)):
    print(l1[0])#"name":"sudha","rollno":32,"average":30.0}
    print(l1[1])#{"name":"ravi","rollno":34,"average":40}
    print(l1)#[{'name': 'sudha', 'rollno': 32, 'average': 30.0},{"name":"ravi","rollno":34,"average":40}]
    print(type(l1))#list
    print(type(l1[0]))#dict
    l1[0]={"name":"anu","rollno":23,"average":67}
    print(l1)#[{'name': 'anu', 'rollno': 23, 'average': 67}, {'name': 'ravi', 'rollno': 34, 'average': 40}]'''
###############################################list inside tuple###################################
'''l1=[(10,20,30,40),(21.1,34,"sri"),("hello","hi","isina")]
for i in range(len(l1)):
    print(l1[i],end=" ")#(10, 20, 30, 40) (21.1, 34, 'sri') ('hello', 'hi', 'isina') 
print(l1[0])#(10, 20, 30, 40)
print(l1[1])#(21.1, 34, 'sri')
print(l1[2])#('hello', 'hi', 'isina')
l1[0]=(50,60,70,80,90)
print(len(l1[0]))#5
for i in range(len(l1[0])):
    print(l1[0][i],end=" ")#50 60 70 80 90
l1[0][0]=3
print(l1[0])#TypeError: 'tuple' object does not support item assignment'''
#######################list inside set#################################################
'''l1=[{10,20,30},{40,50,60},{70,80,90},{100,110,120},{1,2.3,"anu",True,200}]
for i in range(len(l1)):
    print(l1[i],end=" ")#{10, 20, 30} {40, 50, 60} {80, 90, 70} {120, 100, 110} {200, 1, 2.3, 'anu'} 
#another examples
l1[0]={"ammu","arjun","arya"}
print(l1)#[{'ammu', 'arya', 'arjun'}, {40, 50, 60}, {80, 90, 70}, {120, 100, 110}, {200, 1, 2.3, 'anu'}]
#for i in range(len(l1[0])):
    #print(l1[0][i],end=" ")#TypeError: 'set' object is not subscriptable
for i in l1[0]:
    print(i)#rjun ammu ary'''
''' in set we can't acess the values by useing index we can acess the values by using for loop only without useing range function in for loop'''
#############################some of the examples of the list ###############################
#sum of the list of the elements'''
'''l=[1,23,45,67,89]
sum=0
for i in l:
    sum+=i
print(sum)
#multiply items in list
l=[1,23,45,67,89]
mul=1
for i in l:
    mul*=i
print(mul)
# get alrgest number in alist
l=[1,23,45,67,89]
lar=l[0]
for i in range(1,len(l),1):
    if l[i]>lar:
        lar=l[i]
print(lar)
# Get Smallest Number in List
l=[1,23,45,67,89]
small=l[0]
for i in range(1,len(l),1):
    if l[i]<lar:
        small=l[i]
print(small)
# Count Strings with Same Start and End
l=["anu","aba","nan","pop"]
n=len(l)-1
count=0
for i in l:
    if i[0]==i[len(i)-1]:
        count+=1
print(count)'''
#11. Check Common Member Between Two Lists
'''l1=[1,2,3,4,5]
l2=[10,20,30,40,5]
for i in l1:
    if  i in l2:
        print(i,end=" ")#5 '''
# Remove Specific Elements from List
'''
l1=["amma","nanna","anna","akka","friends","anotherperson"]
target="anotherperson"
for i in l1:
    if i==target:
        l1.remove(target)
print(l1)
#remove even number from the list
l2=[1,2,3,4,5,6,7,8,9,10]
for i in l2:
    if i%2==0:
        print(i,end=" ")'''
##################list inside #########################3
'''l1=[(1,2,3,4,5),{"name":"sudha","roll no":45},{1,2,3,4,5},["ammu",6,7,8]]
for i in range(len(l1)):
    print(l1[i],end=" ") #(1, 2, 3, 4, 5) {'name': 'sudha', 'roll no': 45} {1, 2, 3, 4, 5} ['ammu', 6, 7, 8] 
    l1[0]=(0,9,8)
    print(l1[i],end=" ")'''
#################find the second largest element in the list############################
'''l=[1,2,3,8,9]
val=l[0]
for i in range(1,len(l),1):
    if l[i]>val:
        res=l[i] 
l.remove(res)   
print(max(l))'''
#####################################
'''A="siri"
print(A.upper())'''
########################################################
'''n=[1,2,3,4,[5,6,7,8]]
sum=0
for i in n:
    for j in i:
        sum+=j
print(j,end=" ")'''
##############################
'''isinstance(object, classinfo):- object: The variable or value you want to check.
- classinfo: The type (or tuple of types) you want to check against.
x = 5
print(isinstance(x, int))        # True
y = "hello"
print(isinstance(y, str))        # True
z = [1, 2, 3]
print(isinstance(z, list))       # True
print(isinstance(z, (list, tuple)))  # True — checks if z is either list or tuple
############## i am adding list in list elements#######################
n = [1, 2, 3, 4, [5, 6, 7, 8]]
total = 0
for i in n:
    if isinstance(i, list):
        for j in i:
            total += j
            print(j, end=" ")
    else:
        total += i
        print(i, end=" ")

print("\nTotal sum:", total)'''
#####################################################
'''Write a Python program to find both the second smallest and second largest numbers within a specified index range in a list.
n=int(input("enter the range of the list"))
l=list(map(int, input().split()))
small=l[0]
great=l[0]
for i in l:
    if i>=small:
        great=i
    else:
        small=small
l.remove(small)
l.remove(great)
print(l[0],l[-1])
##############################3
l1=[1,3,5,7,9]
l2=[2,4,6,8,10]
l3=[]
#l3=[1,2,3,4,56,7,8,9,10]
for i,j in zip(l1,l2):
    l3.append(i)
    l3.append(j)
print(l3)
#################################internally implementation
def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            yield tuple(next(it) for it in iterators)
        except StopIteration:
            return
            - *iterables: Accepts any number of iterable arguments.
- iter(it): Converts each iterable into an iterator so we can call next() on them.
- yield tuple(...): Returns a tuple of the next items from each iterator.
- StopIteration: If any iterator is exhausted, the function exits — just like the built-in zip().
help(zip)
print(zip.__doc__)
t=(10,20,30)
t1=t
print(id(t))#2608230524800
print(id(t1))#2608230524800
l1=[10,20,30]
l2=l1
print(id(l1))#1443004571840
print(id(l2))#1443004571840
l1=[10,20,30]
l3=l1.copy()
l1=[10,20,30]
print(id(l3))#2361380938752
print(id(l1))#236
a=b=c=10
print(a)
print(b)
print(c)'''
print(10 and 20)
print(20 and 10)