function solution(data, col, row_begin, row_end) {
    var answer = 0;
    const copied_data = data.map(v => [...v])
    copied_data.sort((a, b) => {
        if (a[col - 1] != b[col - 1]) return a[col - 1] - b[col - 1]
        if (a[col - 1] == b[col - 1]) return b[0] - a[0]
    })
    answer = copied_data.reduce(
        (acc, cur, idx) => {
            if (idx + 1 < row_begin || idx + 1 > row_end) return acc
            let mod_sum = cur.reduce(
                (in_acc, in_cur) => in_acc + in_cur % (idx + 1)
                , 
                0
            )
            return acc ^ mod_sum
        },
        0
    )
    return answer;
}