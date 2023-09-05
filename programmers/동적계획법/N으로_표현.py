# 동적 계획법
# https://school.programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def cal(nums1, nums2):
    final = set()
    for i in nums1:
        for j in nums2:
            final.add(i+j)
            final.add(i-j)
            final.add(i*j)
            if j != 0:
                final.add(i//j)
    return final

def solution(N, number):
    nums = dict()
    nums[1] = set([N])
    if N == number:
        return 1
    for i in range(2, 9):
        temp_list = set([int(str(N)*i)])
        for j in range(1, i):
            temp_list.update(cal(nums[i-j], nums[j]))
        # print(temp_list)
        if number in temp_list or -number in temp_list:
            print(temp_list)
            return i
        nums[i] = temp_list
        # print(nums)
        
    return -1


print(solution(5, 12))