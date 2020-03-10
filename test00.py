from __future__ import division
from __future__ import print_function

 
# else:
        # num = 1 + n ** 2 + 1
        # print(num) #2

        # num = 1 + n ** 2 + n ** 2 + 1
        # print(num) #3

        # num = 1 + n ** 2 + ((n-1)*2) ** 2 + n ** 2 + 1
        # print(num) #4

        # num = 1 + n ** 2 + ((n-1) + (n-2)*2) ** 2 *2 + n ** 2 + 1
        # print(num) #5

        # num = 1 + n ** 2 + ((n-1) + (n-2)+(n-3)*2)**2 +(((n-2)+(n-3)*2)*2)**2 + ((n-1) + (n-2)+(n-3)*2)**2 + n ** 2 + 1
        # print(num) #6


# # T[2][0] = [1]
    # # T[2][1] = [1][0] + [1][1]  #2: 1 3 1
    # # T[3][1] = [2][0] + [2][1] #3: 1 3 3 1
    # # T[3][2] = [2][1] + [2][2]
    # # line[3][1] = [i-1][j-1] + [i-1][j] 
    # for i in range(2, n + 1):
    #     for j in range(1, n + 1):
    #         T[i][j] = T[i-1][j-1] + T[i-1][j]

    #         print(T[i][j])
    #     # T[2][2] = [1]


lst = []
n = 4
num = 11**n
print(str(num))

squared_sum = 0
for i in str(num):
    squared_sum += int(i)**2
print(squared_sum)










# Questions:
# - Input?
# - Output?
# - Use real examples.
# - Requirements?

# def calculate_tip(amount, rating):
    # Use dict: ratings(in lower case)->tipspercent, for random ratings.
    # coding here...

    # Convert rating to lower case, same as dict's key.
    # coding here...

    # Check if rating is in dict, calculate tips based on tips percent.
    # coding here...