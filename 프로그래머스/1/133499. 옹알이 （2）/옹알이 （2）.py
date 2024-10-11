def solution(babbling):
    possible_sounds = ["aya", "ye", "woo", "ma"]
    count = 0
    for word in babbling:
        temp = word
        for sound in possible_sounds:
            if sound * 2 not in temp:
                temp = temp.replace(sound, " ")
        
        if temp.strip() == "":
            count += 1
            
    return count
