#define SWAP(x, y, t) ( (t) = (x), (x) = (y), (y) = (t) )

// 선택정렬
void selection_sort(int list[], int n)
{
    int i, j, least, temp;
    for (i = 0; i < n - 1; i++) {
        least = i;
        for (j = i + 1; j < n; j++) {
            if (list[j] < list[least]) least = j;
        SWAP(list[i], list[least], temp);
        }
    }
}

// 삽입정렬
void insertion_sort(int list[], int n)
{
    int i, j, key;
    for (i = 1; i < n; i++) {
        key = list[i];
        for (j = i - 1; j >= 0 && list[j] > key; j--)
            list[j + 1] = list[j];
        list[j + 1] = key;
    }
}

// 버블정렬
void bubble_sort(int list[], int n)
{
    int i, j, temp;
    for (i = n - 1; i > 0; i--) {
        for (j = 0; j < i; j++) {
            if (list[j] > list[j + 1])
                SWAP(list[j], list[j + 1], temp);
        }
    }
}

// 퀵정렬
#define MAX_SIZE 10
int list[MAX_SIZE];
int n;

int partition(int list[], int left, int right)
{
    int pivot, temp;
    int low, high;
    // 첫번쨰 요소는 비교에서 제외시키니까 + 1 안함
    low = left;
    // 첫번째 요소 포함시키려면 + 1 해야됨
    high = right + 1;
    pivot = list[left];
    do {
        do
        {
            low++;
        } while (list[low] < pivot);
        do
        {
            high--;
        } while (list[high] > pivot);
        if (low < high) SWAP(list[low], list[high], temp);
    } while (low < high);

    SWAP(list[left], list[high], temp);
    return high;
}

void quick_sort(int list[], int left, int right)
{
    if (left < right)
    {
        int q = partition(list, left, right);
        quick_sort(list, left, q - 1);
        quick_sort(list, q + 1, right);
    }
}

// 병합 정렬
int sorted[MAX_SIZE]; /*병합 정렬은 추가공간 필요*/

/* i는 정렬된 왼쪽 리스트에 대한 인덱스
    j는 정렬된 오른쪽 리스트에 대한 인덱스
    k는 정렬될 리스트에 대한 인덱스
*/
void merge(int list[], int left, int mid, int right)
{
    int i, j, k, l;
    i = left; j = mid + 1, k = left;

    /* 분할 정렬된 리스트의 병합*/
    while (i <= mid && j <= right) {
        if (list[i] <= list[j])
            sorted[k++] = list[i++];
        else
            sorted[k++] = list[j++];
    }
    /* 남아있는 레코드 일괄 복사 */
    if (i > mid)
        for (l = j; l <= right; l++)
            sorted[k++] = list[l];
    else
        for (l = i; l <= mid; l++)
            sorted[k++] = list[l];
    /* 임시 배열에서 list로 재복사 */
    for (l = left; l <= right; l++)
        list[l] = sorted[l];
}

void merge_sort(int list[], int left, int right)
{
    int mid;
    if (left < right) {
        mid = (left + right) / 2;
        merge_sort(list, left, mid);
        merge_sort(list, mid + 1, right);
        merge(list, left, mid, right);
    }
}