target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]

def selection_sort(target):
    l = len(target)
    for i in range(0, l - 1):
        min = i
        for j in range(i + 1, l):
            if target[j] < target[min]:
                min = j
        target[i], target[min] = target[min], target[i]

selection_sort(target)
target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]

def insertion_sort(target):
    l = len(target)
    for i in range(1, l):
        temp = i
        for j in range(i - 1, -1, -1):
            if target[temp] < target[j]:
                target[temp], target[j] = target[j], target[temp]
                temp = j
            else:
                break
insertion_sort(target)

target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]
def bubble_sort(target):
    l = len(target)
    for i in range(l - 1, 0, -1):
        for j in range(1, i + 1):
            if target[j - 1] > target[j]:
                target[j], target[j - 1] = target[j - 1], target[j]
bubble_sort(target)

target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]

def quick_sort(left, right):
    if right - left < 1:
        return

    pivot = target[left]

    lptr, rptr = left + 1, right

    while lptr <= rptr:
        if pivot < target[lptr] and target[rptr] < pivot:
            target[lptr], target[rptr] = target[rptr], target[lptr]
            lptr, rptr = left + 1, right

        if target[lptr] <= pivot:
            lptr += 1

        if pivot <= target[rptr]:
            rptr -= 1

    target[left], target[rptr] = target[rptr], target[left]

    quick_sort(left, rptr - 1)
    quick_sort(lptr, right)

print('before:\t', target)
quick_sort(0, len(target) - 1)
print('after:\t', target)

target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]
sorted_list = [0 for _ in range(len(target))]


def merge(left, mid, right):
    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if target[i] <= target[j]:
            sorted_list[k] = target[i]
            i += 1
        else:
            sorted_list[k] = target[j]
            j += 1
        k += 1

    if mid < i:
        for t in range(j, right + 1):
            sorted_list[k] = target[t]
            k += 1
    else:
        for t in range(i, mid + 1):
            sorted_list[k] = target[t]
            k += 1

    for idx in range(left, right + 1):
        target[idx] = sorted_list[idx]


def merge_sort(left, right):
    if left != right:
        mid = (left + right) // 2
        merge_sort(left, mid)
        merge_sort(mid + 1, right)
        merge(left, mid, right)


print('before:\t', target)
merge_sort(0, len(target) - 1)
print('after:\t', target)

import heapq

target = [3, 5, 1, 2, 7, 8, 4, 6, 9, 10]


def heap_sort():
    heapq.heapify(target)

    answer = []
    while target:
        answer.append(heapq.heappop(target))

    return answer


print('before:\t', target)
target = heap_sort()
print('after:\t', target)