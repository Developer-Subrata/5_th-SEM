# # Bit Stuffing
# sender=input("Enter Your Data : ")
# result=''
# found=0

# print("Sender Side Data Before Stuffing: ",sender)
# count=0
# for i in sender:
#     if i=='0':
#         result+=i
#         count=0
#         found=1
#     else:
#         if found==1:
#             count+=1
#             result+=i
#             if count==5:
#                 result+='0'
#                 count=0
#         else:
#             result+=i
#             found=0
# print("Receiver Side Data After Stuffing: ",result)


def bit_stuffing(data):
    flag='01111110'
    result = ''
    i = 0
    while i < len(data):
        if data[i:i+6] == '011111':
            result += '0111110'
            i += 6
        else:
            result += data[i]
            i += 1
    return flag+result+flag

data = input("Enter the binary data: ")
print("Stuffed data:", bit_stuffing(data))