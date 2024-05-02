#include<iostream>
using namespace std;

struct Node
{
	int data;
	struct Node *addr;
	
}*start;
void create();
void display();

int main(){
    int n,ch;
    start=NULL;
    do
    {
        cout<<"\n1-Create \n2-Display";
        cout<<"Enter number to insert in linked list: ";
        cin>>n;
        create(n);
        display();
        cout<<"\ndo you WANT TO continue press 1";
        cin>>ch;

    }while(ch==1);
    cout<<"\n------------------------------Thank You--------------------------";

    return 0;
}
void create(int n)
{
    struct Node *newnode,*curr;
    newnode=malloc(sizeof(struct Node));
    newnode->data=n;
    newnode->addr=NULL;
    if(start==NULL)
    {
        start=newnode;
    }
    else
    {
        curr=start;
        while(curr->addr!=NULL)
        {
            curr=curr->addr;
        }
        curr->addr=newnode;
    }
}