a=[50, 61, 83, 59, 3, 92, 25, 84, 28, 88]
b=[100, 53, 64, 92, 8, 24, 15, 49, 11, 28]
c=[29, 11, 57, 90, 57, 26, 31, 2, 20, 75]
max_list=[]
min_list=[]
for x in [a,b,c]:
    max_list.append(sorted(x)[-1])
    max_list.append(sorted(x)[-2])
    min_list.append(sorted(x)[0])
    min_list.append(sorted(x)[1])
avg_max=sum(max_list)/len(max_list)
avg_min=sum(min_list)/len(min_list)
print "Average of Maxlist : %d \nAverage of Min list : %d \n" %(avg_max,avg_min)



    

