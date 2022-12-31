function solution(n, l, r) {
    function dfs(n, start, end) {
        console.log(n,start,end)
        if (n === 0) {
            return 1;
        }
        
        if (start === 1 && end === 5 ** n) {
            return 4 ** n;
        }
        
        let bound_left = 1, bound_right = 5 ** (n - 1);
        let new_start = start, new_end = end;
        let sum = 0;
        
//         5구간의 바운더리 각각 확인 
        for (let i = 1; i <= 5; i++) {    
            if (start < bound_left) {
                new_start = bound_left;
            } else {
                new_start = start;
            }
            
            if (end > bound_right) {
                new_end = bound_right;
            } else {
                new_end = end;
            }
            
            if (start > bound_right) {
                bound_left += 5 ** (n - 1);
                bound_right += 5 ** (n - 1);
                continue;
            } else {
                bound_left += 5 ** (n - 1);
                bound_right += 5 ** (n - 1);
            }
//             3번째 바운더리는 전부 다 0이므로 합산X
//             호출된 재귀함수의 n값에 맞게 start와 end값을 offset시킴
            if (i !== 3) 
                sum += dfs(n - 1, new_start - 5 ** (n - 1) * (i - 1), 
                           new_end - 5 ** (n - 1) * (i - 1));
            
            if (end < bound_left) 
                break;
        }
        return sum;
    }
    
    return dfs(n, l, r);
}
