# Byte Stuffing     011111101000000110000001100000010111111001111110
sender1=input("Enter Data You Want To Send : ")
result=''
flag='01111110'
esc='10000001'
sender=sender1[8:-8]

print("Sender Side Data Before De-Stuffing: ",sender1)
i=0
while(i<len(sender)):
    if sender[i:i+16]==esc+esc:
        result+=esc
        i+=16
    elif sender[i:i+16]==esc+flag:
        result+=flag
        i+=16
    else:
        result+=sender[i]
        i+=1

print("Receiver Side Data After De-Stuffing: ",result)