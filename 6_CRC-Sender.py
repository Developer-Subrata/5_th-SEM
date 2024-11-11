# Input data and generator
data = input("Enter Data : ")#"11010011101100"  # Input data (binary string)
divisor = input("Divisor :") #"1101"      # Generator polynomial (binary string)

# Append zeros to the data (length of generator - 1)
withAguData = data + '0' * (len(divisor) - 1)
remainder = withAguData

# Perform the CRC division
for i in range(len(data)):
    if remainder[i] == '1':  # Only divide if the bit is '1'
        # XOR operation
        for j in range(len(divisor)):
            remainder = (remainder[:i+j] + ('1' if remainder[i+j] != divisor[j] else '0') + remainder[i+j+1:])

# Get the last bits as CRC
crc = remainder[-(len(divisor) - 1):]

# Append CRC to the original data
transmitted_data = data + crc

# Output results
print("DataWord: ", data)
print("Divisor : ", divisor)
print("CRC: ", crc)
print("Transmitted Data: ", transmitted_data)