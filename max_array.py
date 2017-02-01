min, max = 0, 0
array_inp = map(int,raw_input().split())
length_arr = len(array_inp)
for indx in range(0,length_arr):
    if min>array_inp[indx]:
        min = array_inp[indx]
    if max<array_inp[indx]:
        max = array_inp[indx]
print max, min
