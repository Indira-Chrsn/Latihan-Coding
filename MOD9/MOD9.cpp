#include "MOD9.h"

void createStack(Stack &S){
    Top(S) = 0;
}

bool isEmpty(Stack S){
    if (Top(S) == 0){
        return true;
    }else{
        return false;
    }
}

bool isFull(Stack S){
    if (Top(S) == 10){
        return true;
    }else{
        return false;
    }
}

void push(Stack &S, infotype x){
    if (isFull(S) == false){
        Top(S) = Top(S) + 1;
        info(S)[Top(S)] = x;
    }
}

int pop(Stack &S){
    infotype x;

    x = info(S)[Top(S)];
    Top(S) = Top(S) - 1;

    return x;
}

void printInfo(Stack S){
    int i = Top(S);

    while (i >= 1){
        cout << info(S)[i] << " ";
        i--;
    }
}

void ascending(Stack &S){
    infotype temp = 0;
    infotype i = Top(S);
    int Min = info(S)[i];

    while (i >=1){
        if (Min > info(S)[i-1]){
            temp = Min;
            Min = info(S)[i-1];
            info(S)[i-1] = temp;
        }
        i--;
    }
}

void descending(Stack &S){
    int temp = 0;
    int i = Top(S);
    int Max = info(S)[i];

    while (i >=1){
        if (Max < info(S)[i-1]){
            temp = Max;
            Max = info(S)[i-1];
            info(S)[i-1] = temp;
        }else{

        }
        i--;
    }
}
