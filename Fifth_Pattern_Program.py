# Fifth pattern program 

# * * * * *
#   * * * 
#     *
#Logic 
# i     j                    
# 1     1,2,3,4,5                j>=1 and j<=5
# 2     2,3,4                    j>=2 and j<=4                 j>=i and j<=6-i
# 3     3                        j>=3 and j<=3

#Code 
for i in range(1,4):
    for j in range(1,6):
        if j>=i and j<=6-i: 
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()