function solution(hp) {
    let cnt = 0;
    let arr = [5,3,1]
    let idx = 0 
    while (idx < arr.length) {
        let item = arr[idx]
        if(hp >= item){
            cnt += Math.floor(hp/item)
            hp -= Math.floor(hp/item)*item
        }
        idx += 1
    }
    return cnt;
}