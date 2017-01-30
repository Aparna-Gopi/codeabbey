sum = 0
array_min = []
print "input data"
no_val = input()
for indx in range(0,no_val):
    [a, b] = input.split(' ')
    if a < b:
        array_min.append(a)
    else:
        array_min.append(b)

length_arr = len(array_min)
for indx in range(0,length_arr):
    print array_min[indx],
