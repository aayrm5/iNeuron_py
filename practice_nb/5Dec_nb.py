import numpy

lst= [1,2,3,4]
lst1 = []
for i in lst:
    lst1.append(i**2)

print(lst1)

[i**2 for i in lst]

lst = [1,2,3,4,5,6,7,8,9,10]
ls1 = [i for i in lst if i%2==0]
print(ls1)


tup = (1,2,3,4,5, 'RIyaz')

tup[5]

s = 'iNeuron'
s_rev = s[::-1]

count=5
while count < 0:
    print('*')
    count=-1    
     
