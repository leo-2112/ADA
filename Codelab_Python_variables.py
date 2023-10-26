#We initialize the four primitive types

int_example = 30
float_example = 31.1
string_example = "hello world"
boolean_example = True

#Here we create a new variable called concat_example where we convert all previous values
#to strings and we concatenate them together:
concat_example = str(int_example) + str(float_example) + string_example + str(boolean_example)


'''
Maximum and minimum values for integer and float data types:
Max Int: 9223372036854775807
Min Int: -9223372036854775808
Max Float: 1.7976931348623157e+308
Min Float: 2.2250738585072014e-308

Note:
In Python 3.x, the int data type has unlimited precision, which means it can represent arbitrarily large
or small integers without overflow or underflow errors.
An integer giving the maximum value a variable of type Py_ssize_t can take. 
It’s usually 2**31 - 1 on a 32-bit platform and 2**63 - 1 on a 64-bit platform.
The values provided by sys.maxsize and sys.float_info are specific to the platform and Python version in use.
'''

#We initialize a pairs_sum integer variable to hold the sum of pairs from int_example
pairs_sum = 0

#Sum of pairs formula applied to int_example
for i in range(int_example+1):
    if i % 2 == 0:
        pairs_sum += i

#We print all results from previous exercises
print('Primitive data types in Python: ')
print('Integer: ' + str(int_example))
print('Float: ' + str(float_example))
print('String: ' + string_example)
print('Boolean: ' + str(boolean_example))

print('\nConcatenation of previous data types in Python: ' + concat_example)

print('\nSum of pairs using our int_example: ' + str(pairs_sum))

