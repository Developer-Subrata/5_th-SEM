# Byte Stuffing
sender=input("Enter Data You Want To Send : ")
result=''
flag='0111110'

print("Sender Side Data Before Stuffing: ",sender)
for i in sender:
    if i=='F':
        result+='EF'
    elif i=='E':
        result+='EE'
    else:
        result+=i

receiver=flag+result+flag
print("Receiver Side Data After Stuffing: ",receiver)