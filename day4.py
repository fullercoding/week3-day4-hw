#Solve the following question and create test cases with unittest
# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.
a1 = [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]

a2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]
# Output:
# [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

a3 = [4,2,1,0,98,1,0,0,1,4,5,6,12,74]

def zerohunt(list):
    nl = []
    total_zeros = 0
    for num in list:
        if num == 0:
            total_zeros += 1
        else:
            nl.append(num)
    while total_zeros > 0:
        nl.append(0)
        total_zeros -= 1
    return nl

print(zerohunt(a1))
print(zerohunt(a2))
print(zerohunt(a3))