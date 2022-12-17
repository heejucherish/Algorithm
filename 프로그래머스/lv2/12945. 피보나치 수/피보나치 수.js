function solution(n) {
    let answer = 0 
    let t1 = 0 
    let t2 = 1
    for(let i = 2; i <= n; i++){
        answer = (t1+t2) %1234567
        t1 = t2
        t2 = answer 
    }
    return answer%1234567;
}