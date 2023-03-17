x=8
y=2
print(x+y*3)
print((x+y)*3)
print(x**y)
print(x%y)
print(x/12.0)
print(x//6)

x=54.66
print(round(x))
print(int(x))

#kiem tra so nguyen to
import math
def isPrime(n):
    if (n<2):
        return False
    else:
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
    return True
            
# try:
#     n=int(input("Nhap vao so n="))
#     if isPrime(n)==True:
#         print("{} la so nguyen to".format(n))
#     else:
#         print("{} k la so nguyen to".format(n))
# except:
#     print("Dinh dang dau vao k hop le")

def soHoanChinh(n):
    count=0
    if (n<0):
        return False
    else:
        for i in range(1,n):
           if (n%i==0):
                count+=i 
        if (count==n):
            return True
        else:
            return False

# try:
#     n=int(input("Nhap vao so n="))
#     if soHoanChinh(n)==True:
#         print("{} la hoan chinh".format(n))
#     else:
#         print("{} k la so hoan chinh".format(n))
# except:
#     print("Dinh dang dau vao k hop le")

def soDoiXung(n):
    temp=n
    so_dao_nguoc=0
    don_vi=0
    while(temp!=0):
        don_vi=temp%10
        so_dao_nguoc=so_dao_nguoc*10+don_vi
        temp=temp/10
    if (so_dao_nguoc==n):
        return True
    return False

def soChinhPhuong(n):
    temp=int(math.sqrt(n))
    if (temp**2==n):
        return True
    return False

mang_SNT,mang_SDX,mang_SHC,mang_SCP=[],[],[],[]
a=int(input("Nhap a="))
b=int(input("Nhap b="))
for i in range(a,b+1):
    if isPrime(i):
        mang_SNT.append(i)
    elif soHoanChinh(i):
        mang_SHC.append(i)
    elif soDoiXung(i):
        mang_SDX.append(i)
    else:
        mang_SCP.append(i)

print("Mang so nguyen to:",mang_SNT)
print("Mang so hoan chinh:",mang_SHC)
print("Mang so doi xung:",mang_SDX)
print("Mang so chinh phuong:",mang_SCP)

def UCLN(a,b):
    while a!=b:
        if (a>b):
            a=a-b
        else:
            b=b-a
    return a

def UCLN_Rer(a,b):
    if (a==b):
        return a
    elif (a>b):
        return UCLN_Rer(a-b,b)
    else:
        return UCLN_Rer(a,b-a)

def BCNN(a,b):
    result=UCLN(a,b)
    return (a*b)/result

def BCNN_Rer(a,b):
    if (a%b==0):
        return a
    else:
        global i
        a=a/i
        i=i+1
        return BCNN_Rer(a*i,b)

x=int(input("Nhap so x="))
y=int(input("Nhap so y="))
print("UCLN:",UCLN_Rer(x,y))
print("BCNN:",BCNN(a,b))
print("BCNN:",BCNN_Rer(a,b))

# n=int(input("Nhap so luong so nguyen to:"))
# dem=0
# i=2
# while dem<n:
#     if isPrime(i):
#         print(i,end=" ")
#         dem+=1
#     i+=1

def searchNum():
    for i in range(99,1000):
        if i%7==0 and i %5!=0:
            print(i,end=" ")
# searchNum()

def searchNum2(m,n):
    for i in range(m,n+1):
        if i%7==0 and i%9==0:
            return i
    return -1
print(searchNum2(3,200))

def demCacChuSo():
    n=int(input("Nhap so nguyen n="))
    demSo=0
    sum=0
    while(n>0):
        sum=sum+n%10
        n=n//10
        demSo+=1
    print(demSo)
    print("Tong cac chu so la:",sum)
demCacChuSo()

def tinhLuyThua(a,n):
    if (a==0 and n!=0):
        return 0
    if (a!=0 and n==0):
        return 1
    else:
        return tinhLuyThua(a,n-1)*a


def tinhLuyThua_devide(a,n):
    if (a==0 and n!=0):
        return 0
    if (a!=0 and n==0):
        return 1
    else:
        if (n%2==0):
            return tinhLuyThua_devide(a,n/2)* tinhLuyThua_devide(a,n/2)
        else:
            return a*tinhLuyThua_devide(a,(n-1)/2)*tinhLuyThua_devide(a,(n-1)/2)
# print(tinhLuyThua_devide(3,5))

def inTungChuSo():
    lst=[]
    n=int(input("Nhap so nguyen n="))
    while(n>0):
        temp=n%10
        lst.append(temp)
        n=n//10
    lst.reverse()
    print("Cac chu so cua so n la:",lst)
inTungChuSo()

