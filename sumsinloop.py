sum = 0
array_sum = []
print "input data"
no_val = input()
for indx in range(0,no_val):
    input = raw_input()
    array = [int(val) for val in input.split(" ")]
    sum = array[0] + array[1]
    array_sum.append(sum)

length_arr = len(array_sum)
for indx in range(0,length_arr):
    print array_sum[indx],
