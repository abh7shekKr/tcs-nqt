# Question 2: Group Formation Based on Efficiency 
# Problem Statement 
# You are given efficiencies of n people. You need to form 
# groups of size t. 
# If some people are left (i.e., n is not divisible by t), those 
# extra people are removed. 
# For each group: 
 
# • Find the difference between the highest and lowest 
# efficiency.  
# Task 
# Return the maximum difference among all groups. 
 
# Input Explanation 
# 1. Integer n → number of people  
# 2. Array of n integers → efficiencies  
# 3. Integer t → size of each group  
 
# Output Explanation 
# • Form groups of size t after sorting the array.  
# • For each group, compute: 
# difference = max element - min element 
# • Print the maximum difference among all groups.  
# • If input is invalid, print "Invalid Input".  
 
# Example 
# Input 
# 6 
# 1 3 4 9 10 12 
# 2 
# Explanation 
 
 
# • Sorted array: [1, 3, 4, 9, 10, 12]  
# • Groups:  
#  (1, 3) → difference = 2  
#  (4, 9) → difference = 5  
#  (10, 12) → difference = 2  
# • Maximum difference = 5  
# Output 
# 5


def max_group_difference(n, efficiencies, t):
    if n<0 or t<0 or len(efficiencies)!=n:
        print("Invalid Input")
        
    efficiencies.sort()
    max_diff = 0
    for i in range(0, n - (n%t), t):
        group = efficiencies[i:i+t]
        diff = group[-1] - group[0]
        max_diff = max(max_diff, diff)
        
    return max_diff

try:
    n = int(input()) #number of people
    efficiencies = list(map(int, input().split())) #array of n integers
    t = int(input()) #size of each group
    
    result = max_group_difference(n, efficiencies, t)
    print(result)
except:
    print("Invalid Input")
    