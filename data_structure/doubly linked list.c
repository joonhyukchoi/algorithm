// 이중 연결 리스트는 보통 헤드 노드가 존재하므로 단순 연결 리스트처럼 헤드 포인터가 필요 없다.
#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct DLisNode {
    element data;
    struct DLisNode* llink;
    struct DLisNode* rlink;
} DLisNode;

// 이중 연결 리스트를 초기화
// 참고: 헤드는 값이 없음
void init(DLisNode* phead)
{
    phead->llink = phead;
    phead->rlink = phead;
}

// 이중 연결 리스트의 노드를 출력
void print_dlist(DLisNode* phead)
{
    DLisNode* p;
    // 참고: 마지막 노드가 head 노드를 가리킴
    for (p = phead->rlink; p != phead; p = p->rlink) {
        printf("<-| |%d| |-> ", p->data);
    }
    printf("\n");
}

// 새로운 데이터를 노드 before의 오른쪽에 삽입한다.
// 만약 원하는 위치에 넣고 싶다면 탐색필요. 탐색은 O(n) 시간이 걸리는 것 고려.
void dinsert(DLisNode* before, element data)
{
    DLisNode* newnode = (DLisNode*)malloc(sizeof(DLisNode));
    newnode->data = data;
    newnode->rlink = before->rlink;
    newnode->llink = before;
    before->rlink->llink = newnode;
    before->rlink = newnode;
}

// 노드 removed를 삭제한다.
// 헤드노드의 오른쪽 요소를 삭제한다고 가정
void ddelete(DLisNode* head, DLisNode* removed)
{
    if (removed == head) return;
    // 순서 주의
    removed->rlink->llink = head;
    head->rlink = removed->rlink;
    free(removed);
}

// 이중 연결 리스트 테스트 프로그램
int main(void)
{
    DLisNode* head = (DLisNode *)malloc(sizeof(DLisNode));
    init(head);
    printf("추가 단계\n");
    for (int i = 0; i < 5; i++) {
        // 헤드 노드의 오른쪽에 삽입
        dinsert(head, i);
        print_dlist(head);
    }
    printf("\n삭제 단계\n");
    for (int i = 0; i < 5; i++) {
        print_dlist(head);
        ddelete(head, head->rlink);
    }
    free(head);
    return 0;
}