# maximum subarray - kadane's algorithm (return maximum subarray sum and the subarray itself.)

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = arr[0]
curr_sum = arr[0]
start = 0
end = 0
temp_start = 0

for i in range(1, len(arr)):
    if arr[i] > curr_sum + arr[i]:
        curr_sum = arr[i]
        temp_start = i
    else:
        curr_sum = curr_sum + arr[i]
        
    if curr_sum > max_sum:
        max_sum = curr_sum
        start = temp_start
        end = i
        
max_subarray = arr[start:end + 1]
print("Maximum Sum:", max_sum)
print("Subarray:", max_subarray)