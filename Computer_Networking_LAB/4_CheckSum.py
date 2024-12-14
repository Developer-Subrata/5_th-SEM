def func(bSUM):
    if len(bSUM)>4:
        lmb=bSUM[:len(bSUM)-4]
        rmb=bSUM[len(bSUM)-4:]
    else:
        lmb=0
        rmb=bSUM
    return int(lmb,2), int(rmb,2)

data=list(map(int,input("Enter Your Data Set : ").split()))
data3=data.copy()
SUM=sum(data)
bSUM=bin(SUM)[2:]

lmb,rmb=func(bSUM)
wrapped_sum=bin(lmb+rmb)[2:]

if len(wrapped_sum)>4:
    while len(wrapped_sum)>4:
        lmb,rmb=func(wrapped_sum)
        wrapped_sum=bin(lmb+rmb)[2:]
else:
    wrapped_sum=bin(lmb+rmb)[2:].zfill(4)

checkSum=''
for i in wrapped_sum:
    if i=='1':
        checkSum+='0'
    else:
        checkSum+='1'

cs=int(checkSum,2)

data.append(cs)
print("Genarated CheckSum Is : ",cs)
print("The Sender Send Data As: ", data)

#ddddddddddddddddddddddddddddd
def func(bSUM):
    if len(bSUM)>4:
        lmb=bSUM[:len(bSUM)-4]
        rmb=bSUM[len(bSUM)-4:]
    else:
        lmb=0
        rmb=bSUM
    return int(lmb,2), int(rmb,2)

data2=list(map(int,input("\nEnter Your Received Data Set : ").split()))
SUM=sum(data2)
bSUM=bin(SUM)[2:]

lmb,rmb=func(bSUM)
wrapped_sum=bin(lmb+rmb)[2:]

if len(wrapped_sum)>4:
    while len(wrapped_sum)>4:
        lmb,rmb=func(wrapped_sum)
        wrapped_sum=bin(lmb+rmb)[2:]
else:
    wrapped_sum=bin(lmb+rmb)[2:].zfill(4)

checkSum=''
for i in wrapped_sum:
    if i=='1':
        checkSum+='0'
    else:
        checkSum+='1'

cs=int(checkSum,2)
if cs==0:
    print(f"Receiver CheckSum Is : {cs} So, There  Is No Error !!! ")
    print("The Receiver Data Is: ",data3)
else:
    print(f"Receiver CheckSum Is : {cs} \tSo, There  Is Error !!! ")
    print("The Wrong Data Is: ",data2)