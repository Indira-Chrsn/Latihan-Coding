#include "Queue.h"

void createQueue(Queue &Q){
    head(Q) = nil;
    tail(Q) = nil;
}

adr createElm(data_transaksi x){
    adr p = new elm;

    info(p) = x;
    next(p) = nil;

    return p;
}

void masukkan_transaksi(Queue &Q, string s){
    adr x = createElm(s);

    if (head(Q) == nil){
        head(Q) = x;
        tail(Q) = x;
    }else{
        next(x) = head(Q);
        head(Q) = x;
    }
}
void Proses_transaksi(Queue &Q){
//    adr r = head(Q);

    if (tail(Q) != nil){
        if (tail(Q) == head(Q)){
            tail(Q) = nil;
            head(Q) = nil;
        }else{
            adr q = head(Q);
            while (next(q) != tail(Q)){
                q = next(q);
            }
            tail(Q) = q;
            next(q) = nil;
        }
    }
}

void printQueue(Queue Q){
    adr q = head(Q);
    while (q != tail(Q)){
        cout << info(q) << endl;
        q = next(q);
    }
    cout << info(q) << endl;
}
