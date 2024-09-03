# Byte Stuffing 
sender1=input("Enter Data You Want To Send : ")
sender=sender1[8:-8]
result=''
flag='01111110'
esc='10000001'

i=0
while(i<len(sender)):
  if sender[i:i+8]==esc:
        i+=8
        while i + 8 <= len(sender) and (sender[i:i+8] == flag or sender[i:i+8] == esc):
            result += sender[i:i+8]
            i += 8
  else:
    result+=sender[i]
    i+=1

receiver=result
print("Receiver Side Data After De-Stuffing: ",receiver)