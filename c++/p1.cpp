/* Find the sum of all multiples of a certain number
or set of (m) numbers below a given value (n). */

#include <iostream>

using namespace std;

int loop(int n, int m, int a[]) {
	int s = 0; bool f = false;
	
	/*For each i, set flag to true if i is a multiple
	of any of the given numbers.*/
	
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			if(i%a[j] == 0) { f = true; }
		}
		if(f) { 
			s = s+i;
			f = false;
		}
	}
	return s;
}

int main() {
	int n = 1000, m = 2, a[] = {3, 5};
	cout<<loop(n, m, a);
}