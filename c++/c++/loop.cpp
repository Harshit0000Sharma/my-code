#include <iostream>

using namespace std;
int main()
{
    /*Loops in C++:
    There are three types of loops in C++:
        1. For loop
        2. While Loop
        3. do-While Loop
    */

    //!For loop in C++

    for (int i = 1; i <= 40; i++)
    {
        cout << i << endl;
    }
    //! while loops in python
    int i = 41;
    while (i <= 100)
    {
        cout << i << endl;
        i++;
    }
    //! do while loop in C++
    do
    {
        int i = 100;
        cout << i << endl;
    } while (i < 100);
    //! break
    for (int i = 0; i < 40; i++)
    {
        /* code */
        if (i == 2)
        {
            break;
        }
        cout << i << endl;
    }
    //! continue
    for (int i = 0; i < 40; i++)
    {
        /* code */
        if (i == 2)
        {
            continue;
        }
        cout << i << endl;
    }
}