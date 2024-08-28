def bit_stuffing(data):
    result = ''
    i = 0
    while i < len(data):
        if data[i:i+6] == '0111110':
            result += '011111'
            i += 6
        else:
            result += data[i]
            i += 1
    return result

sender = input("Enter the binary data: ")
data=sender.replace('01111110','')
print("De-Stuffed data:", bit_stuffing(data))