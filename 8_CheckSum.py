def func(bSUM):
    if len(bSUM) > 4:
        lmb = bSUM[:len(bSUM) - 4]  
        rmb = bSUM[len(bSUM) - 4:]  
    else:
        lmb = '0'  
        rmb = bSUM 

    lmb = int(lmb, 2)
    rmb = int(rmb, 2)
    return lmb,rmb


data = list(map(int, input("Enter Your Data: ").split()))
SUM = sum(data)
bSUM = bin(SUM)[2:]                 # Converting sum to binary and removing the '0b' prefix
print("Total Sum Is=> ",bSUM)
lmb,rmb=func(bSUM)

wrapped_sum = bin(lmb + rmb)[2:]
if len(wrapped_sum)>4:
    while(len(wrapped_sum)>4):
        lmb,rmb=func(wrapped_sum)
        wrapped_sum = bin(lmb + rmb)[2:]
else:
     wrapped_sum = bin(lmb + rmb)[2:].zfill(4)
    
checksum = ''
for i in wrapped_sum:
        if(i == '1'):
            checksum += '0'
        else:
            checksum += '1'

print(f"WrappedSum : {wrapped_sum}\nFinal checksum: {checksum}")
