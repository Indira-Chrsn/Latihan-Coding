#include <iostream>
#include "Queue.h"
using namespace std;

int main()
{
    cout << "Hello world!" << endl;

    Queue Q;

    createQueue(Q);
    masukkan_transaksi(Q, "Andi transfer Doni 50.000");
    masukkan_transaksi(Q, "Doni transfer Saras 20.000");

    printQueue(Q);

    Proses_transaksi(Q);

    printQueue(Q);
    return 0;
}
