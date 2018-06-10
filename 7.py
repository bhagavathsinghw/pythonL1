inp=int(raw_input("Enter :"))
ip_mask=[]
def init(ip_mask):
    for i in range(0,32):
        ip_mask.append(0)
    
init(ip_mask)
if inp!=0:
    for i in range(0,inp):
        ip_mask[i]=1
else:
    pass

print ip_mask,len(ip_mask)
a="".join(str(x) for x in ip_mask[:7])
b="".join(str(x) for x in ip_mask[8:16])
c="".join(str(x) for x in ip_mask[17:24])
d="".join(str(x) for x in ip_mask[23:32])

print a,b,c,d





