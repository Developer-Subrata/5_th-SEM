import math
p=int(input("Enter 1st Prime No: "))
q=int(input("Enter 2nd Prime No: "))
m=int(input("Enter Data : "))
n=p*q
phin=(p-1)*(q-1)
d=e=2
while(e<phin):
    if(math.gcd(e,phin)==1):
        break
    else:
        e+=1
while(d<n):
    if(math.fmod((d*e),phin))==1:
        break
    else:
        d+=1        

print("Public Key=> ",e)
print("Private Key=> ",d)
c=math.fmod((m**e),n)
print("Encrypted Data: => ",c)
om=math.fmod((c**d),n)
print("De-crypted Data: => ",om)