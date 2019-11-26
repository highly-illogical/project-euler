/*Add together every even-valued Fibonacci number upto a given
value (n).*/

#include <iostream>

using namespace std;

int fibseries(long int n) {
	long int f[1000] = {1, 2}, i = 2, s = 0;
	while (f[i-2] <= n) {
		f[i] = f[i-1] + f[i-2];
		if(!(i%3)) { s = s + f[i-2]; }	//every 3rd term starting from 2 is even
		i++;
	}
	return s;
}

int main() {
	cout<<fibseries(4000000);
}