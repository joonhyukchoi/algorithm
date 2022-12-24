class Queue {
    constructor () {
        this.queue = []
        this.front = 0
        this.rear = -1
    }
    
    enqueue (val) {
        this.rear++
        this.queue[this.rear] = val
    }
    
    dequeue () {
        if (this.rear === -1 || this.front > this.rear) return NaN
        const now = this.queue[this.front]
        this.front++
        return now
    }
    
    size () {
        return this.rear - this.front + 1
    }
    
    peek () {
        if (this.rear === -1 || this.front > this.rear) return NaN 
        return this.queue[this.front]
    }
}


function solution(bridge_length, weight, truck_weights) {
    var answer = 0
    const q = new Queue()
    for (let i = 0; i < truck_weights.length; i++) {
        q.enqueue(truck_weights[i])
    }
    const bridge = new Queue()
    let now_weight = 0
    let now_time = 0
    while (bridge.size() !== 0 || q.size() !== 0) {
        now_time++
        
        if (bridge.peek()[0] + bridge_length === now_time) {
            now_weight -= (bridge.dequeue())[1]
        }
        
        if (q.size() > 0 && now_weight + q.peek() <= weight) {
            const dequeued_value = q.dequeue()
            now_weight += dequeued_value
            bridge.enqueue([now_time, dequeued_value])
        }
        
        // console.log(now_time, bridge.queue, bridge.peek()[0], bridge_length)
    }
    answer = now_time
    return answer
}