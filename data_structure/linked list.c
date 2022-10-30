#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct ListNode { 
    element data;
    struct ListNode *link;
} ListNode;

void error(char *message)
{
    fprintf(stderr, "%s\n", message);
    exit(1);
}

ListNode* insert_first(ListNode* head, int value)
{
    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->data = value;
    p->link = head;
    head = p;
    return head;
}

// 노드 pre 뒤에 새로운 노드 삽입, pre는 따로 search 해줘야 함
ListNode* insert(ListNode *head, ListNode *pre, element value)
{
    ListNode *p = (ListNode *)malloc(sizeof(ListNode));
    p->data = value;
    p->link = pre->link;
    pre->link = p;
    return head;
}

ListNode* delete_first(ListNode *head)
{
    ListNode *removed;
    if (head == NULL) return NULL;
    removed = head;
    head = removed->link;
    free(removed);
    return head;
}

// pre가 가리키는 노드의 다음노드 삭제
ListNode* delete(ListNode *head, ListNode *pre)
{
    ListNode *removed;
    removed = pre->link;
    pre->link = removed->link;
    free(removed);
    return head;
}

void print_list(ListNode *head)
{
    for (ListNode *p = head; p != NULL; p = p->link)
        printf("%d->", p->data);
}

// 이중 포인터 이용
typedef struct {
    int value;
    node_t* next;
} node_t;

void print_list_2(node_t* head)
{
    node_t* now = head;
    while (now != NULL) {
        printf("%d", now->value);
        now = now->next;
    }
}

void destroy(node_t* head)
{
    node_t* now = head;
    while (now != NULL) {
        node_t* next = head->next;
        free(head);
        now = next;
    }
}

void insert_list_2(node_t** p_head, int num)
{
    node_t* now;

    now = (node_t*)malloc(sizeof(node_t));
    now->value = num;

    now->next = *p_head;
    *p_head = now;
}

// 이부분 좀 어려움
int delete(node_t** p_head, int num)
{
    node_t** p_now = p_head;
    while(*p_now != NULL) {
        if ((*p_now)->value == num) {
            node_t* temp = *p_now;
            *p_now = (*p_now)->next;
            free(temp);
            break;
        } 

        p_now = &(*p_now)->next;
    }
}

int main() {
    node_t* head = NULL;
    insert_list_2(head, 2);
    insert_list_2(head, 3);
}