#include <iostream>
using namespace std;

int main()
{ //***************refrence variable***************
    int a = 12;
    int &b = a;
    cout << a << endl;
    cout << b << endl;
    //! b is not the copy of a its the aother name to call variable
    //**************Typecasting in C++*************
    int c = 55;
    float d = 55.78;
    cout << int(c) << endl;
    cout << int(d) << endl; //float d=55.78 but when we typecast d to int it become 55
    cout << float(c) << endl;
    cout << float(d) << endl;
    return 0;
}