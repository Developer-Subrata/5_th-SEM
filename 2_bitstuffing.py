# Bit Stuffing
sender=input("Enter Your Data : ")
result=''
found=0

print("Sender Side Data Before Stuffing: ",sender)
count=0
for i in sender:
    if i=='0':
        result+=i
        count=0
        found=1
    else:
        if found==1:
            count+=1
            result+=i
            if count==5:
                result+='0'
                count=0
        else:
            result+=i
            found=0

print("Receiver Side Data After Stuffing: ",result)