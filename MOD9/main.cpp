#include <iostream>
#include "MOD9.h"
using namespace std;

int main()
{
//    cout << "Hello world!" << endl;

    Stack S;

    createStack(S);
    push(S, 2);
    push(S, 3);
    push(S, 4);
    push(S, 5);
/*    push(S, 6);
    push(S, 7);
    push(S, 8);
    push(S, 9);
    push(S, 10);
    push(S, 11); */

//    bool x = isFull(S);
//    cout << x << endl;
    printInfo(S);

/*    cout << endl;
    cout << "Top(S) = " << Top(S);
*/
    cout << endl << endl;

    ascending(S);
    printInfo(S);
    cout << endl << endl;

    descending(S);
    printInfo(S);
    cout << endl << endl;

    pop(S);
/*    infotype a = pop(S);
    cout << "a: " << a << endl;
*/
    printInfo(S);

    return 0;
}
