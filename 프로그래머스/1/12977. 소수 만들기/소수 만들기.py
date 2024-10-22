def solution(nums):
    answer = 0
    for i in range(len(nums)) :
        for j in range(i+1, len(nums)) :
            for k in range(j+1, len(nums)) :
                cnt = 0
                for l in range(2, nums[i] + nums[j] + nums[k] + 1):
                    if (nums[i] + nums[j] + nums[k]) % l == 0 :
                        cnt += 1
                if cnt == 1 :
                    answer += 1           
    return answer