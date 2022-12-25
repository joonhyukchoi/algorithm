class MinHeap {
    constructor () {
        this.heap = [ null ]
        this.size = 0
    }
    
    swap(a, b) {
        [ this.heap[a], this.heap[b] ] = [ this.heap[b], this.heap[a] ];
    }
    
    heappush(value) {
        this.heap.push(value);
        let curIdx = this.heap.length - 1;
        let parIdx = (curIdx / 2) >> 0;
        
        while(curIdx > 1 && this.heap[parIdx] > this.heap[curIdx]) {
            this.swap(parIdx, curIdx)
            curIdx = parIdx;
            parIdx = (curIdx / 2) >> 0;
        }
    }
    
    heappop() {
        const min = this.heap[1];	
        if(this.heap.length <= 2) this.heap = [ null ];
        else this.heap[1] = this.heap.pop();   
        
        let curIdx = 1;
        let leftIdx = curIdx * 2;
        let rightIdx = curIdx * 2 + 1; 
        
        if(!this.heap[leftIdx]) return min;
        if(!this.heap[rightIdx]) {
            if(this.heap[leftIdx] < this.heap[curIdx]) {
                this.swap(leftIdx, curIdx);
            }
            return min;
        }

        while(this.heap[leftIdx] < this.heap[curIdx] || this.heap[rightIdx] < this.heap[curIdx]) {
            const minIdx = this.heap[leftIdx] > this.heap[rightIdx] ? rightIdx : leftIdx;
            this.swap(minIdx, curIdx);
            curIdx = minIdx;
            leftIdx = curIdx * 2;
            rightIdx = curIdx * 2 + 1;
        }

        return min;
    }
    
    peek () {
        return this.heap[1] ? this.heap[1] : null;
    }
    
    empty () {
        if (this.heap.length === 0) {
            return true
        }
        return false
    }
}

function solution(jobs) {
    const heap1 = new MinHeap()
    const heap2 = new MinHeap()
    jobs.forEach(element => heap1.heappush(element))
    let last = 0
    let sum = 0
    
    while (!heap1.empty()) {
        while(!heap1.empty() && heap1.peek()[0] <= last) {
            const temp_min_element = heap1.heappop()
            heap1.heappush([temp_min_element[1], temp_min_element[0]])
        }
        
        if (!heap2.empty()) {
            const min_element = heap2.heappop()
            last = last + min_element[0]
            sum += last - min_element[1]
        } else {
            last += 1
        }
        
        while (!heap2.empty()) {
            const temp = heap2.heappop()
            heap.heappush([temp[1], temp[0]])
        }
    }
    return sum
}