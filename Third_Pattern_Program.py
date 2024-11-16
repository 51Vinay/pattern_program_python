# Third Pattern Program 
#           *
#         * *
#       * * * 
#     * * * *  
#   * * * * *        
#  conditions 
# i   j   
# 1   5
# 2   4,5
# 3   3,4,5                 j>=6-i
# 4   2,3,4,5
# 5   1,2,3,4,5

#Program
for i in range (1,6):
    for j in range (1,6):
        if j>=6-i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()