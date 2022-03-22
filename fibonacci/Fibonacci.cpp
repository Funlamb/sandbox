/*console app that print on the nth fibonacci number */

#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;

int main (){
        //input:
        //get user to input the fibonacci number that they want
        cout << "Type the nth Fibonacci number that you want: ";
        int userNum = 0;

        cin >> userNum;
        cout << "You chose: " << userNum << endl;
        userNum++;

        //process:
        //find the number that they want
        float Phi = (1 + sqrt(5)) / 2;
        float phi = (1 - sqrt(5)) / 2;
        long long output = (pow(Phi, userNum) - pow(phi,userNum)) / sqrt(5);
        //output:
        //show use the numebr
        cout << "Your Fibonacci number is " << output << endl;
}
