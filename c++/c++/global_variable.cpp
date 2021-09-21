#include <iostream>
using namespace std;
//declaring global variable👇
int a = 10;
int b = 12;

int main()
{
    //local variable👇
    int a = 11;
    int b = 13;
    cout << "The value of local variable a+b is " << a + b << endl;
    cout << "The value of glocal variable a+b is " << ::a + ::b << endl;
    //in line 13 :: means global variable
    return 0;
}