#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * Definition for singly-linked list.
 * */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (NULL == head)
        return NULL;

    struct ListNode *next=head->next, *prev = head;

    while(NULL != next){
        if (prev->val == next->val){
            prev->next = next->next;
        }else{
            prev = next;
        }
        next = next->next;
    }

    return head;
}
