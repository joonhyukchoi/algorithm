// 배열을 이용한 구현

#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK_SIZE 100

typedef int element;
typedef struct {
    int top;
    int capacity;
    element *data
} StackType;

// 스택 생성함수
void init_stack(StackType *s)
{
    s->top = -1;
    s->capacity = 1;
    s->data = (element *)malloc(s->capacity * sizeof(element));
}

// 공백 상태 검출 함수
int is_empty(StackType *s)
{
    return (s->top == -1);
}

// 포화 상태 검출 함수
int is_full(StackType *s)
{
    return (s->top == (s->capacity - 1));
}

void push(StackType *s, element item)
{
    if (is_full(s)) {
        s->capacity *= 2;
        s->data = (element *)realloc(s->data, s->capacity * sizeof(element));
    }
    s->data[++(s->top)] = item;
}

element pop(StackType *s)
{
    if (is_empty(s)){
        fprintf(stderr, "스택 공백 에러\n");
        exit(1);
    }
    else return s->data[(s->top)--];
}

// 리스트를 이용한 구현

typedef int element;
typedef struct StackNode {
    element data;
    struct StackNode* link;
} StackNode;

typedef struct {
    StackNode* top;
} LinkedStackType;

// 초기화 함수
void init(LinkedStackType* s)
{
    s->top = NULL;
}

// 공백 상태 검출 함수
int is_empty(LinkedStackType* s)
{
    return (s->top == NULL);
}

// 삽입 함수
void push(LinkedStackType* s, element item)
{
    StackNode* temp = (StackNode*)malloc(sizeof(StackNode));
    temp->data = item;
    temp->link = s->top;
    s->top = temp;
}

// 출력
void print_stack(LinkedStackType* s)
{
    for (StackNode* p = s->top; p != NULL; p = p->link)
        printf("%d->", p->data);
    printf("NULL \n");
}

// 삭제 함수
element pop(LinkedStackType* s)
{
    if (is_empty(s)) {
        fprintf(stderr, "스택이 비어있음\n");
        exit(-1);
    } else {
        StackNode* temp = s->top;
        int data = temp->data;
        s->top = s->top->link;
        free(temp);
        return data;
    }
}

// 피크 함수
element peek(LinkedStackType* s)
{
    if (is_empty(s)) {
        fprintf(stderr, "스택이 비어있음\n");
        exit(1);
    }
    else {
        return s->top->data;
    }
}