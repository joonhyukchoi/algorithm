def solution(n):
    answer = []
    def hanoi(n, frm, to):
        if n > 1:
            hanoi(n - 1, frm, 6 - to - frm)
        answer.append([frm, to])
        if n > 1:
            hanoi(n - 1, 6 - to - frm, to)
    hanoi(n, 1, 3)
        
    return answer