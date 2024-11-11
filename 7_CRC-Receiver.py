# Input data and generator
data = input("Enter Data : ")
divisor = input("Divisor :") 

remainder = data

# Perform the CRC division
for i in range(len(data)):
    if remainder[i] == '1':  # Only divide if the bit is '1'
        # XOR operation
        for j in range(len(divisor)):
            remainder = (remainder[:i+j] + ('1' if remainder[i+j] != divisor[j] else '0') + remainder[i+j+1:])

# Get the last bits as CRC
crc = remainder[-(len(divisor) - 1):]

if crc=='000':
    transmitted_data = crc
    # Output results
    print("\nDataWord: ", data)
    print("Divisor : ", divisor)
    print("Transmitted Data: ", transmitted_data)
    print("Data Is Correctly Received !!!")
else:
    print("Invalid Data!")