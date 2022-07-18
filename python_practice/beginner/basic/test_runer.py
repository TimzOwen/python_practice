# create a list and print only number less than 5 in a list
# Example in a list of [2,3,4,5,11,1,16,7,8,9] -> [2,3,4,1]
nums = [1,2,4,3,2,53,5,4,7,9,44]
x = []
for i in nums:
    if i <= 5:
        x.append(i)
        x.sort()
print(x)

# using lambda gives a one line solution like
print([j for j in nums if j<5])