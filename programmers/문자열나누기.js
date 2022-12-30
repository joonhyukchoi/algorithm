function solution(s) {
    let answer = 0, index = 0, cnt1 = 0, cnt2 = 0;
    while (true) {
        let temp = s[index];
        let start_word = temp;
        cnt1 = 1;
        cnt2 = 0;
        while (index++ < s.length && cnt1 !== cnt2) {
            if (s[index] === start_word) {
                cnt1++
            } else {
                cnt2++
            }
            temp += s[index];
        }
        answer++;
        if (index >= s.length) {
            break;
        }
    }
    return answer;
}
