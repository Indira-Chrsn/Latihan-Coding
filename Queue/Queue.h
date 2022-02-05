#ifndef QUEUE_H_INCLUDED
#define QUEUE_H_INCLUDED
#include <iostream>
using namespace std;

#define info(Q) (Q)->info
#define next(Q) (Q)->next
#define head(Q) (Q).head
#define tail(Q) (Q).tail
#define nil NULL

typedef string data_transaksi;
typedef struct elm *adr;

struct elm{
    data_transaksi info;
    adr next;
};

struct Queue{
    adr head;
    adr tail;
};

void createQueue(Queue &Q);
adr createElm(data_transaksi x);
void masukkan_transaksi(Queue &Q, string s);
void Proses_transaksi(Queue &Q);
void printQueue(Queue Q);
#endif // QUEUE_H_INCLUDED
