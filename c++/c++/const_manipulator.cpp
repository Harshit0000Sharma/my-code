#include <iostream>
#include <iomanip> //from iomanip we can use setw manipulator
using namespace std;
int main()
{
    //*************constant*************
    const int a = 55;
    const int b = 1;
    //int a = 99; //!here the value of a can't be changed again
    //int b = 9; //!here the value of b can't be changed again
    cout << a + b << endl;
    //************manipulator***********
    int value;
    cout << "enter the value" << endl;
    cin >> value;
    cout << setw(4) << value << endl;
    return 0;
}