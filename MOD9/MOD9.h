#ifndef MOD9_H_INCLUDED
#define MOD9_H_INCLUDED
#include <iostream>
using namespace std;

#define Top(S) (S).Top
#define info(S) (S).info
#define nil NULL

typedef int infotype;

struct Stack{
     infotype info[10];
     int Top;
};

void createStack(Stack &S);
bool isEmpty(Stack S);
bool isFull(Stack S);
void push(Stack &S, infotype x);
int pop(Stack &S);
void printInfo(Stack S);
void ascending(Stack &S);
void descending(Stack &S);

#endif // MOD9_H_INCLUDED
