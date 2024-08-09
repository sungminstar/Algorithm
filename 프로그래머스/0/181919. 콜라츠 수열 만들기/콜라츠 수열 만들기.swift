import Foundation

func solution(_ n: Int) -> [Int] {
    var result: [Int] = []  
    var current = n 
    
    while current != 1 {  
        result.append(current)  
        
        if current % 2 == 0 {  
            current /= 2 
        } else {  
            current = current * 3 + 1  
        }
    }
    
    result.append(1)  
    return result  
}
