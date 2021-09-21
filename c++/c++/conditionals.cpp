#include <iostream>

using namespace std;

int main()
{
    int age;
    cout << "Tell me your age" << endl;
    cin >> age;

    // 1. Selection control structure: If else-if else ladder
    if ((age < 18) && (age > 0))
    {
        cout << "hello" << endl;
    }
    else if (age < 1)
    {
        cout << "You are not yet born" << endl;
    }
    else
    {
        cout << "hello 2" << endl;
    }

    // 2. Selection control structure: Switch Case statements
    switch (age)
    {
    case 18:
        cout << "You are 18" << endl;
        break;
    case 22:
        cout << "You are 22" << endl;
        break;
    case 2:
        cout << "You are 2" << endl;
        break;

    default:
        cout << "No special cases" << endl;
        break;
    }

    cout << "Done with switch case";
    return 0;
}
