def solutionA():
    user_array = [1,3,5,7,2]
    for x in range (min(user_array), max(user_array)):
        if x not in user_array:
            break
        return x
# print(solutionA())

from itertools import count, filterfalse # ifilterfalse on py2

def solution(A): 
    print(next(filterfalse(set(A).__contains__, count(1))))
solution(A=[3,-2,5,7])