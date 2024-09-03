# Byte Stuffing     011111101000000110000001100000010111111001111110
sender=input("Enter Data You Want To Send : ")
result=''
flag='01111110'
esc='10000001'

print("Sender Side Data Before Stuffing: ",sender)
i=0
while(i<len(sender)):
    if sender[i:i+8]==flag or sender[i:i+8]==esc:
        result+=esc+sender[i:i+8]
        i+=8
        while i + 8 <= len(sender) and (sender[i:i+8] == flag or sender[i:i+8] == esc):
            result += sender[i:i+8]
            i += 8
    else:
        result+=sender[i]
        i+=1

receiver=flag+result+flag
print("Receiver Side Data After Stuffing: ",receiver)