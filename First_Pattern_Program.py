## First Pattern Program 
# *                                    
# * *
# * * *
# * * * *

# logic design
# i    j
# 1   1
# 2   2             condition j<=1
# 3   3
# 4   4

#program
for i in range (1,5):
    for j in range (1,5):
        if j<=i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()