#include<stdio.h>
#include<stdlib.h>
struct node
{
int info;
struct node *link;
};
struct node* start=NULL;
void traverse()
{
struct node* temp;
if(start==NULL)
printf("\n List is empty\n");
else
{
temp=start;
printf("The list is:\n");
while(temp!=NULL)
{
printf("%d->",temp->info);
temp=temp->link;
}
}
}
void insertAtFront()
{
int data;
struct node* temp;
temp=malloc(sizeof(struct node));
printf("\n Enter number to be inserted:");
scanf("%d",&data);
temp->info=data;
temp->link=start;
start=temp;
}
void insertAtPosition()
{
struct node *temp,*newnode;
int pos,data,i=1;
newnode=malloc(sizeof(struct node));
printf("\nEnter postion and data:");
scanf("%d%d",&pos,&data);
temp=start;
newnode->info=data;
newnode->link=0;
while(i<pos-1)
{
temp=temp->link;
i++;
}
newnode->link=temp->link;
temp->link=newnode;
}
void insertAtEnd()
{
int data;
struct node *temp,*head;
temp=malloc(sizeof(struct node));
printf("\nEnter number to be inserted:");
scanf("%d",&data);
temp->link=0;
temp->info=data;
head=start;
while(head->link!=NULL)
{
head=head->link;
}
head->link=temp;
}
void deleteFirst()
{
struct node *temp;
if(start==NULL)
printf("\nList is empty");
else
{
temp=start;
start=start->link;
free(temp);
}
}
void deleteEnd()
{
struct node *temp,*prevnode;
if(start==NULL)
printf("\nList is empty");
else
{
temp=start;
while(temp->link!=0)
{
prevnode=temp;
temp=temp->link;
}
free(temp);
prevnode->link=0;
}
}
void deleteposition()
{
struct node *temp,*position;
int i=1,pos;
if(start==NULL)
printf("\nList is empty");
else
{
printf("\nEnter the position:");
scanf("%d",&pos);
position=malloc(sizeof(struct node));
temp=start;
while(i<pos-1)
{
temp=temp->link;
i++;
}
position=temp->link;
temp->link=position->link;
free(position);
}
}
int main()
{
int choice;
while(1)
{
printf("\n\t1.To see List\n");
printf("\t2.For insertion at starting\n");
printf("\t3.For insertion at postion\n");
printf("\t4.For insertion at end\n");
printf("\t5.For deletion at start\n");
printf("\t6.For deletion at end\n");
printf("\t7.For deletion at position\n");
printf("\tTo Exit\n");
printf("\nEnter your choice:\n");
scanf("%d",&choice);
switch(choice)
{
case 1:
traverse();
break;

case 2:
insertAtFront();
break;

case 3:
insertAtPosition();
break;

case 4:
insertAtEnd();
break;

case 5:
deleteFirst();
break;

case 6:
deleteEnd();
break;

case 7:
deleteposition();
break;

case 8:
exit(1);
break;

default:
printf("Incorrect Choice\n");
}
}
return 0;
}
