inp=int(raw_input("Enter Prefix:"))
if inp==32:
    ip_mask=[1]*32
elif inp>32:
    print "Prefix not valid"
    exit()
else:
    ip_mask=[0]*32
    for i in range(0,31):
        if i<inp:
            ip_mask[i]=1
        else:
            ip_mask[i]=0
a=int("".join(str(x) for x in ip_mask[0:8]),2)
b=int("".join(str(x) for x in ip_mask[8:16]),2)
c=int("".join(str(x) for x in ip_mask[16:24]),2)
d=int("".join(str(x) for x in ip_mask[24:32]),2)
print "NetMask is : %d.%d.%d.%d" %(a,b,c,d)
