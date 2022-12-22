function solution(t, p) {
    let answer = 0;
    for (let i = 0; i < t.length && i + p.length <= t.length; i++) {
        if (Number(t.substring(i, i + p.length)) <= Number(p)) answer++
    }
    return answer;
}