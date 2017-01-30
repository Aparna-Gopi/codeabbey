sum = 0

print "input data"
no_val = input("enter amount of values to be added")
input = raw_input("enter the numbers to be sorted separated by ','")
array_inp = [int(val) for val in input.split(",")]
for indx in range(0,no_val):
    sum = sum + array_inp[indx]
print "sum"
print sum
