import math
p=int(input("Enter 1st Prime Number : "))
q=int(input("Enter 2nd Prime Number : "))
n=p*q
phin=(p-1)*(q-1)
d=e=2

while(e<phin):
    if (math.gcd(e,phin)==1):
        break
    else:
        e+=1

while(d<n):
    # if(math.fmod((d*e),phin)==1 and d!=e):
    if(((d*e)%phin)==1 and d!=e):
        break
    else:
        d+=1

print("Public Key=> ",e)
print("Private Key=> ",d)
m=int(input("Enter Message=> "))
# cipher=math.fmod((m**e),n)
cipher=(m**e)%n
# decrypt=math.fmod((cipher**d),n)
decrypt=(cipher**d)%n
print("Cipher Text => ",cipher)
print("Original Data => ",decrypt)