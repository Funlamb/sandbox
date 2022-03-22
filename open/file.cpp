#include <iostream>
#include <fstream>
using namespace std;

int main(){
        ofstream file;
        file.open("test.txt");
        if(file.is_open()) {
                string myStr;
                cin >> myStr;
                file << myStr << endl;
        }
        else {
                cout << "Sorry, could not open file." << endl;
        }
}
