#include <iostream>
using namespace std;

int main() {


	int age ;
	cout << "Enter the age of a user :";
	cin >>age;
	if(age >= 18) {
		cout << "you are eligible for voting";
	} else {
		cout << "ypu are not eligible for voting";
	}
	return 0;
}
