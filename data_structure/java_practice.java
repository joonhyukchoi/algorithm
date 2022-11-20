// 자바 연습

// mergesort
void mergesort(int[] array, int low, int high) {
    if (low < high) {
        int mid = low + high / 2;
        mergesort(array, low, mid);
        mergesort(array, mid + 1, high);
        merge(array, low, mid, high);
    }
}

void merge(int[] array, int low, int mid, int high) {
    int[] helper = new int[array.length];

    for (int i = low; i <= high; i++) {
        helper[i] = array[i];
    }

    int helperLeft = low;
    int helperRight = mid + 1;
    int current = low;

    while (helperLeft <= mid && helperRight <= high) {
        if (helper[helperLeft] <= helper[helperRight]) {
            array[current] = helper[helperLeft];
            helperLeft++;
        } else {
            array[current] = helper[helperRight];
            helperRight++;
        }
        current++;
    }
    // 최적화: 오른쪽에 있는 큰 값은 어차피 그자리에 있어도 되기 때문에 신경쓸필요 없음.
    int remaining = mid - helperLeft;
    for (int i = 0; i <= remaining; i++) {
        array[current + i] = helper[helperLeft + i];
    }
}

// quicksort
void quicksort(int arr[], int left, int right) {
    int index = partition(arr, left, right);
    if (left < index - 1) {
        quicksort(arr, left, index - 1);
    }
    if (index < right) {
        quicksort(arr, index, right);
    }
}

int partition(int arr[], int left, int right) {
    int pivot = arr[(left + right) / 2];
    while (left <= right) {
        while (arr[left] < pivot) left++;
        while (arr[right] > pivot) right--;
        if (left <= right) {
            swap(arr, left, right);
            left++;
            right--;
        }
    }
}