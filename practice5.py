# Question 1: Problem Statement 
# Remove Duplicates and Print in Reverse 
# Order 
# Given an array of elements, remove all 
# duplicate elements while preserving the 
# order of their first occurrence. After 
# removing duplicates, print the resulting 
# array in reverse order. 
 
#  Input Format 
# • 
# First line contains an integer n (size of 
# the array)  
# • 
# Second line contains n space-separated 
# integers  
 
#  Output Format 
 
 
# • 
# Print the array after removing 
# duplicates and reversing it  
 
# Example 
# Input 
# 7 
# 1 2 3 2 4 1 5 
# Output 
# 5 4 3 2 1

def remove_duplicates_reverse(n, arr):
    if n<=0 or len(arr)!=n:
        return "Invalid Input"
    
    seen = set()
    unique = []
    
    for i in arr:
        if i not in seen:
            seen.add(i)
            unique.append(i)
            
    unique.reverse()
    return unique

try:
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = remove_duplicates_reverse(n, arr)
    
    if result == "Invalid Input":
        print(result)
    else:
        print(*result)
except:
    print("Invalid Input")