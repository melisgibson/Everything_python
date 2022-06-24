# binary numbers
a = 0b1001
b = 0b1100

# prints the decimal equivalent
print(a)

# prints the binary 
print(bin(a)) 

# bitwise OR operator, prints a "1" when there is "1" in either position
print(bin(a | b))

# bitwise AND operator, prints a "1" when there is a "1" in both positions
print(bin(a & b))

# bitwise XOR operator, prints "1" if only one of the bits is "1", but will be "0" if both are "0" or both are "1"
print(bin(a ^ b))

# shift operator right shift
print(bin(a >> 2))

#shift operator left shift
print(bin(a << 4))