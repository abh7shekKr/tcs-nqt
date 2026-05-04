# Q1)  
# Problem: Discount Calculator 
# You are given a purchase amount. Based on 
# the amount, a discount is applied as follows: 
# • 
# • 
# • 
# Discount Rules: 
# If amount < 1000 → 5% discount  
# If amount ≥ 1000 and < 5000 → 10% 
# discount  
# If amount ≥ 5000 → 15% discount  
# Task: 
# Calculate the final payable amount after 
# applying the discount. 
 
 
#      Input Format: 
# • 
# A single integer amount representing the 
# total purchase value.  
#      Output Format: 
# • 
# Print the final amount after discount, 
# rounded to 2 decimal places.  
 
#       Sample Test Cases: 
#    Test Case 1: 
# Input: 
# 800 
# Output: 
# 760.00 
# Explanation: 
# 5% of 800 = 40 → Final = 800 - 40 = 760 
 
# Test Case 2: 
# Input: 
 
 
# 2000 
# Output: 
# 1800.00 
# Explanation: 
# 10% of 2000 = 200 → Final = 1800 
 
#  Test Case 3: 
# Input: 
# 6000 
# Output: 
# 5100.00 
# Explanation: 
# 15% of 6000 = 900 → Final = 5100

amount = int(input())

if amount < 1000:
    discount = 5
elif amount < 5000:
    discount = 10
else:
    discount = 15

final_amount = amount - (amount * discount) / 100

print(f"{final_amount:.2f}")