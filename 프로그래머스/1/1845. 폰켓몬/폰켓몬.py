def solution(nums):
    # 해시 자료구조 활용 => 딕셔너리 활용
    # 주어진 포켓몬 nums 정리 => "1(1번))" : 1, "2(2번)" : 1, "3(3번)" : 2
        # 굳이 정리해야하나...? 그냥 중복 원소 제거하고 배열을 새로 만들어야 겠다!
    # if len(nums) / 2 <= 딕셔너리의 키의 개수 :
        # return len(nums) / 2
    # else :
        # return 딕셔너리의 키의 개수
        
    kind_array = []
    for i in range(len(nums)) :
        if nums[i] not in kind_array :
            kind_array.append(nums[i])
    if len(nums) // 2 <= len(kind_array) :
        return len(nums) // 2
    else : 
        return len(kind_array)
    
