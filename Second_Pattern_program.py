##-- Second program in python 
# * * * * *
# * * * *
# * * *
# * *
# *
# condition
# i  j
# 1   5
# 2   4        j<6-i
# 3   3
# 4   2
# 5   1

for i in range (1,6):
    for j in range (1,6):
        if j <=6-i :
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
    


