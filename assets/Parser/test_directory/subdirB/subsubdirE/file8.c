#include "file7.h"
#include <stdlib.h>

Node* 
MakeNode (int data)
{
    Node *myNode = (Node *)malloc(sizeof(Node));
    if (myNode == NULL)
    {
        perror("Failed in allocating memory.");
        exit(EXIT_FAILURE);
    }
    myNode->data = data;
    myNode->prev = NULL;
    myNode->next = NULL;

    return myNode;
}