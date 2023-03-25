L=[('PEPSI',2.2,20),('STING',1.5,6),('REDBULL',3.4,10),('COCACOLA',2.5,30)]

#cau a
lst_tenNuoc=[]
for i in L:
    lst_tenNuoc.append(i[0].lower())
lst_tenNuoc=sorted(lst_tenNuoc)
print(lst_tenNuoc)