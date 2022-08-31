import sys
inp = sys.stdin.readline
n = int(inp())

def postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(inorder) == 0:
        return
    idx = inorder.index(preorder[0])
    postorder(preorder[1:idx + 1], inorder[0:idx])
    postorder(preorder[idx + 1:], inorder[idx + 1:])
    print(preorder[0], end = ' ')

for _ in range(n):
    nsize = int(inp())
    prlist = list(map(int, inp().split()))
    inlist = list(map(int, inp().split()))
    postorder(prlist, inlist)
    print()

# nums = [1, 2, 3, 4, 5]
# print(nums[1:60])