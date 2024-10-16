#include <stdio.h>
void push();
void pop();
void display();

int stack[10],i,j,n,choice=0,top=-1;
void main()
{
printf("enter the number of elements in stack:");
scanf("%d",&n);
printf("**** stack operation using array ****");
printf("\n     \n");
while (choice!=4)
{
printf("choice one from the bellow options \n");
printf("\n1.push \n2.pop \n3.display \n4.exist");
printf("\n enter your choice:");
scanf("%d",&choice);
switch(choice)
{
case 1:
push();
break;
case 2:
pop();
break;
case 3:
display();
break;
case 4:
printf("exiting    ");
break;
default:
printf("please enter valid choice:");
}
}
}
void push()
{ int val;
if(top==n){
printf("\n overflow");}
else{
printf("enter the value:");
scanf("%d",&val);
top=top+1;
stack[top]=val;
}
}
void pop()
{
if(top==-1){
printf("underflow");}
else{
top=top-1;
}
}
void display()
{
for(i=top;i>=0;i--)
{printf("%d",stack[i]);
nclude <stdio.h>
void push();
void pop();
void display();

int stack[10],i,j,n,choice=0,top=-1;
void main()
{
printf("enter the number of elements in stack:");
scanf("%d",&n);
printf("**** stack operation using array ****");
printf("\n     \n");
while (choice!=4)
{
printf("choice one from the bellow options \n");
printf("\n1.push \n2.pop \n3.display \n4.exist");
printf("\n enter your choice:");
scanf("%d",&choice);
switch(choice)
{
case 1:
push();
break;
case 2:
pop();
break;
case 3:
display();
break;
case 4:
printf("exiting    ");
break;
default:
printf("please enter valid choice:");
}
}
if(top==-1){
printf("stack is empty");
}
}

