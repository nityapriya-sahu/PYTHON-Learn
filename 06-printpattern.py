# # # #
# # # #
# # # #
# # # #
print('Pattern 1')
for i in range(4):
    for j in range(4):
        print('# ', end='')
    print()

print('Pattern 2')

#
# #
# # #
# # # #

for i in range(4):
    for j in range(i+1):
        print('# ', end='')
    print()

print('Pattern 3')

# # # #
# # #
# #
#

for i in range(4):
    for j in range(4-i):
        print('# ', end="")
    print()

# --------------------------------------------------
# ASSIGNMENT
# Print : 1 2 3 4
#         2 3 4
#         3 4
#         4
print('Pattern 4')
for i in range(1,5):
    for j in range(i,5):
        print(j, end=' ')
    print()

# --------------------------------------------------
# Print : A P Q R
#         A B Q R
#         A B C R
#         A B C D

print('Pattern 4')

letters = ['A', 'B', 'C', 'D']
fixed = ['P', 'Q', 'R']

for i in range(1, 5):
    for j in range(1, 5):
        if j <=i:
            print(letters[j-1], end=' ')
        else:
            print(fixed[j-2], end=' ')

    print()
