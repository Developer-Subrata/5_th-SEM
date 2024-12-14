# #Bit Stuffing
sender=input("Enter Data You Want To Stuff : ")
flag='01111110'
result=''
i=0
while i<len(sender):
    if sender[i:i+6]=='011111':
        result+='0111110'
        i+=6
    else:
        result+=sender[i]
        i+=1
stresult=flag+result+flag
print("After Stuffing :",stresult)

#Bit-DeStuffing..........
sender=stresult[8:-8]
result=''
i=0
while i<len(sender):
    if sender[i:i+7]=='0111110':
        result+='011111'
        i+=7
    else:
        result+=sender[i]
        i+=1
print("After De-Stuffing :",result)