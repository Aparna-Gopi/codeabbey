sum = 0
array_min = []
print "input data"
no_val = input()
for indx in range(0,no_val):
    array_inp = map(int,raw_input().split())
    if array_inp[0] < array_inp[1] and array_inp[0] < array_inp[2]:
        array_min.append(array_inp[0])
    elif array_inp[1] < array_inp[2]:
        array_min.append(array_inp[1])
    else :
        array_min.append(array_inp[2])


length_arr = len(array_min)
for indx in range(0,length_arr):
    print array_min[indx],
