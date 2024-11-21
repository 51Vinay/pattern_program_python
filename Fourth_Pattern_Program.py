###-------Fourth pattern code ----
    #        *
    #      * * * 
    #    * * * * *
    #  * * * * * * *
# logic
# i      j
# 1      4                 j>=4 and j<=4
# 2      3,4,5              j>=3 and j<=5
# 3      2,3,4,5,6          j>=2 and j<=6     j>=5-i  and j<=3+i
# 4      1,2,3,4,5,6        j>=1 and j<=7

##program
for i in range (1,5):
    for j in range (1,8):
        if j>=5-i and j<=3+i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
