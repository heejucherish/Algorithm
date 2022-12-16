function solution(balls, share) {
    var answer = 0;
    
    // n팩토리얼
    const n = balls
    let r = share
    
    let one = 1
    for(let i = n; i>=n-r+1; i--){
        one *= i
    }
    
    
    let three = 1
    for(let i = r; i>=1; i--){
        three *= i
    }
    answer = Math.floor(one/three)
    
    return answer;
}