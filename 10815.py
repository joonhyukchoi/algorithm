import sys

inp = sys.stdin.readline

n = int(inp())
myCard = list(map(int, inp().split()))
myCard.sort()
m = int(inp())
yourCard = list(map(int, inp().split()))
# yourCard.sort()

# print(myCard, yourCard)
def binarySearch(left, right, number, cards):
    if left > right:
        return False
    mid = left + (right - left) // 2
    if number == cards[mid]:
        return number
    elif number > cards[mid]:
        return binarySearch(mid + 1, right, number, cards)
    else:
        return binarySearch(left, mid - 1, number, cards)
solution = []
for i in range(m):
    if binarySearch(0, n - 1, yourCard[i], myCard):
        solution.append(1)
    else:
        solution.append(0)
for el in solution:
    print(el, end = ' ')


