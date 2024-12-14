data=input("Enter Your Data: ")
result=""
f="01111110"

i=0
data1=data[8:-8]

while(i<len(data1)):
    if data1[i:i+7]=="0111110":
        result+="011111"
        i+=7
    else:
        result+=data1[i]
        i+=1
print(result)