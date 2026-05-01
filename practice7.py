# Question 1:  
# Highest Frequency Element 
# Problem Statement: 
# Given an array of integers, count the frequency 
# of each element and return the element that has 
# the highest frequency. 
# If multiple elements have the same highest 
# frequency, return the smallest element among 
# them. 
# Input Format: 
# First line: Integer n (size of array)  
# • 
# • 
# Second line: n space-separated integers  
# Output Format: 
# • 
# Single integer → element with highest 
# frequency (smallest if tie)  
# Example: 
# Input: 
 
 
# 6 
# 1 3 2 3 4 1 
# Output: 
# 1 
# Explanation: 
# Frequency: 
# 1 → 2 
# 3 → 2 
# 2 → 1 
# 4 → 1 
# Both 1 and 3 have same frequency (2), smallest is 
# 1. 

n = int(input())
arr = list(map(int, input().split()))

freq = {}
for i in arr:
    freq[i] = freq.get(i, 0) + 1
max_freq = max(freq.values())

print(freq)
result = min([num for num in freq if freq[num] == max_freq ])
print(result)