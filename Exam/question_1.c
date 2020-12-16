#include <stdio.h>
#include <stdlib.h>
#define MAX_STR_LEN 100

struct ListNode {
    int employeeNum, salary, phoneNum; 
    char *name, *department, *designation; 
    struct ListNode *next; 
    struct ListNode *prev;     
}; 

struct ListNode* createNode(int empNum, int sal, int phone, char* name, char* dep, char* designation){
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode)); 
    node->employeeNum = empNum; 
    node->name = name;
    node->salary = sal; 
    node->phoneNum = phone; 
    node->department = dep; 
    node->designation = designation;
    node->next = NULL; 
    node->prev = NULL; 
    return node; 
}

void endInsertion(struct ListNode* tailNode, struct ListNode* curNode) {
    tailNode->next = curNode; 
    curNode->prev = tailNode; 
}

int main() {
    int numEmployees; 
    printf("Enter the number of employees : "); 
    scanf("%d", numEmployees); 

    struct ListNode* headNode; 
    struct ListNode* tailNode; 
    
    for(int i = 0; i < numEmployees; i++) {
        int empNum, phone, salary; 
        char department[MAX_STR_LEN], designation[MAX_STR_LEN], name[MAX_STR_LEN]; 

        //Get the employee information
        printf('Enter the Employee Number : '); 
        scanf("%d", &empNum); 
        printf("\nEnter the Employee Name : "); 
        fgets(name, MAX_STR_LEN, stdin);   
        printf("\nEnter the employee salary : "); 
        scanf("%d", &salary); 
        printf("\nEnter the Employee designation :"); 
        fgets(designation, MAX_STR_LEN, stdin);
        printf("\nEnter the Employee Department : "); 
        fgets(department, MAX_STR_LEN, stdin);
        printf("\nEnter the Employee's phone number : "); 
        scanf("%d", &phone); 

        //Create the employee node
        struct ListNode* employeeNode = createNode(empNum, salary, phone, name, department, designation); 

        //If it's the first employee, this will be the head node and the tail node
        if(i == 0){
            headNode = employeeNode; 
            tailNode = employeeNode; 
            //skip the next lines for the first employee
            continue; 
        }    

        endInsertion(tailNode, employeeNode); 
        tailNode = employeeNode; 
        
    }
      
}

