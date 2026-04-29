# Q2)  Problem: Arrange the King’s Army 
# A king wants to arrange his army in a line 
# following strict rules. 
# You are given: 
# • 
# N → total number of soldiers in the 
# arrangement  
# • 
# R → soldiers are numbered from 1 to R  
 
 
# • 
# end → the last soldier in the 
# arrangement must be this number  
#  Rules: 
# 1.The arrangement must start with 
# soldier 1  
# 2.The arrangement must end with soldier 
# end  
# 3.No two adjacent soldiers can have the 
# same number  
# 4.You can use any soldier number from 1 
# to R multiple times  
 
# Task: 
# Find the total number of valid 
# arrangements of length N that satisfy all the 
# above conditions. 
 
#  Input Format: 
# • 
# Three integers:  
# N R end 
 
 
#  Output Format: 
# • 
# A single integer → number of valid 
# arrangements  
#  Sample Test Cases: 
#  Test Case 1: 
# Input: 
# 4 4 3 
# Output: 
# 7 
 
#    Test Case 2: 
# Input: 
# 3 3 2 
# Output: 
# 2 
# Explanation: 
# Valid sequences: 
# • 
# 1 2 2   (invalid, same adjacent)  
 
 
# • 
# 1 3 2    
# • 
# 1 2 3  (wrong end)  
# • 
# 1 2 1  (wrong end)  
# So answer = 2 
 
#  Approach (Dynamic Programming) 
# Let: 
# • 
# dp[i][j] = number of ways to form a 
# sequence of length i ending with soldier 
# j  
# Transition: 
# For each position: 
# dp[i][j] += dp[i-1][k]   where k ≠ j 
# Initialization: 
# dp[1][1] = 1   (must start with 1) 
# Final Answer: 
# dp[N][end] 
 
 
 
# rute Force Idea 
# We will generate all possible sequences of 
# length N using numbers from 1 to R, and 
# then: 
#  Check conditions: 
# 1. First element must be 1  
# 2. Last element must be end  
# 3. No two adjacent elements are equal  
#  Approach: 
# • 
# Use recursion (backtracking)  
# • 
# Build sequence step by step  
# • 
# At each step:  
# o 
# Try all values from 1 to R  
# o 
# Skip if same as previous (to avoid 
# adjacent duplicates)  
# • 
# Count valid sequences  
 
 
 
#  Complexity: 
# • 
# Time: O(R^N) (very slow, only for small 
# N)  
# • 
# Space: O(N)  