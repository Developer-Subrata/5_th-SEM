# # Byte Stuffing     011111101000000110000001100000010111111001111110
# sender1=input("Enter Data You Want To Send : ")
# result=''
# flag='01111110'
# esc='10000001'
# sender=sender1[8:-8]

# print("Sender Side Data Before De-Stuffing: ",sender1)
# i=0
# while(i<len(sender)):
#     if sender[i:i+16]==esc+esc:
#         result+=esc
#         i+=16
#     elif sender[i:i+16]==esc+flag:
#         result+=flag
#         i+=16
#     else:
#         result+=sender[i]
#         i+=1

# print("Receiver Side Data After De-Stuffing: ",result)
sender1 = input("Enter Data You Want To Send: ")
result = ''
flag = '01111110'
esc = '10000001'
sender = sender1[8:-8]  # Removing the starting and ending flag

print("Sender Side Data Before De-Stuffing: ", sender1)
i = 0
while i < len(sender):
    if sender[i:i+8] == esc:
        # If 'esc' is found, check the next 8 bits
        next_seq = sender[i+8:i+16]
        
        if next_seq == flag or next_seq == esc:
            result += next_seq  # Add the next sequence (flag or esc)
            i += 16  # Skip both the esc and the next sequence
        else:
            result += sender[i:i+8]  # Add the current esc (if it's not followed by flag or esc)
            i += 8
    else:
        result += sender[i]
        i += 1

print("Receiver Side Data After De-Stuffing: ", result)
