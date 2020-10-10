#110010011 - FAIL   193 |   110010001   |   00010   |   02
#101001110 - FAIL   14E |   101001010   |   00111   |   07
#011110101 - FAIL   0F5 |   111110101   |   11110   |   1E
#111010101 - FAIL   1D5 |   111110101   |   11110   |   1E
#101110010 - FAIL   172 |   101110000   |   10110   |   16
#010000101 - OK     085 |   010000101   |   01000   |   08
#010010101 - FAIL   095 |   010000101   |   01000   |   08
#001000000 - FAIL   040 |   000000000   |   00000   |   00
#001010000 - FAIL   050 |   001010001   |   00100   |   04
#011011010 - FAIL   0DA |   011011011   |   00101   |   05
        
string="100010010"

bool_array=[]

for i in range(9):
    if (string[i]=='1'):
        bool_array.append(True)
    else:
        bool_array.append(False)

print (bool_array[3],bool_array[6],bool_array[0],bool_array[5])
r1=(bool_array[3]!=bool_array[6])!=(bool_array[0]!=bool_array[5])
print("r1 in array {} \t| calculated {}".format(bool_array[1], r1))

r2=(bool_array[3]!=bool_array[2])!=bool_array[0]
print("r2 in array {} \t| calculated {}".format(bool_array[4], r2))

r3=(bool_array[6]!=bool_array[2])!=bool_array[0]
print("r3 in array {} \t| calculated {}".format(bool_array[8], r3))

r4=bool_array[5]
print("r4 in array {} \t| calculated {}".format(bool_array[7], r4))

print("information")
print(bool_array[3], bool_array[6], bool_array[2], bool_array[0],bool_array[5])