from operator import le


def solution(A):
    max_num = A[0]
    n = len(A)
    even_list = []
    for x in range(1,n):
        if A[x] %4 == 0:
            even_list.append(A[x])
    print(even_list)
    return max(even_list)
        
    
print(solution(A=[2,-8,50,101,4,7,-3,89,84, 48,44,11]))


