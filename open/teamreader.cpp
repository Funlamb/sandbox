#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[]) {
        ifstream teamFS;
        string teamName;
        int numWins, numLosses;

        teamFS.open("Teams.txt"); //opens file names Teams.txt

        if (!teamFS.is_open()) {
                cout << "Sorry. Could not open file." << endl;
                return 1;
        }

        //read first line
        getline(teamFS, teamName);
        // cout << teamName << endl;
        while (!teamFS.fail()) {
                //attempt to read numWins
                teamFS >> numWins;
                //attempt to read wins
                if (teamFS.fail()) {
                        cout << setw(50) << setfill('.') << teamName << "'s win lose line missing" << endl;
                }
                else {
                        teamFS >> numLosses;
                        cout << setw(15) << setfill('.');
                        if (teamFS.fail()) {
                                cout << left << teamName << right <<"has " << numWins << " wins." << endl;
                        }
                        else {
                                //average the win loses
                                cout << left << teamName
                                     << right << "win average is "
                                     << setprecision(3) << setw (5) << left << setfill('0')
                                     << (double) numWins / (numWins + numLosses) << endl;
                        }
                        teamFS.ignore();
                }
                teamFS.clear();
                getline(teamFS, teamName);
        }
        teamFS.close();
        return 0;
}
