#Sender Side
dataword=input("Enter Data : ")
divisor=input("Enter Divisor : ")

dataAgu=dataword + '0' * (len(divisor)-1)
temp=dataAgu

for i in range(len(dataword)):
    if temp[i]=='1':
        for j in range(len(divisor)):
            temp=(temp[:i+j] + ('1' if temp[i+j]!=divisor[j] else '0') + temp[i+j+1:])

crc=temp[(-len(divisor)+1):]
# print(crc)
print("DATA : ",dataword)
print("DIVISOR : ",divisor)
print("CODE_WORD : ",dataword+crc)

#Receiver Side.........
dataword=dataword+crc

dataAgu=dataword + '0' * (len(divisor)-1)
temp=dataAgu

for i in range(len(dataword)):
    if temp[i]=='1':
        for j in range(len(divisor)):
            temp=(temp[:i+j] + ('1' if temp[i+j]!=divisor[j] else '0') + temp[i+j+1:])

crc=temp[(-len(divisor)+1):]
if int(crc)==0:
    print("Correct Data!!")
else:
    print("Wrong Data!!!")