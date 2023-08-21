# https://www.acmicpc.net/problem/10431

n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))

    now_list = []
    foot = 0
    for i in range(1, len(nums)):
        if len(now_list) == 0:
            now_list.append(nums[i])
        elif nums[i] >= now_list[-1]:
            now_list.append(nums[i])
        else:
            for j in range(len((now_list))):
                if now_list[j] > nums[i]:
                    now_list.insert(j, nums[i])
                    foot += len(now_list) - j - 1
                    break
    print(nums[0], foot)
