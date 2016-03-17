#include<iostream>

using namespace std;

int main() {
	int a,b,c,d;
	int n = 0;
	cin >> a >> b >> c >> d;
	if (d % 3 == 2) {
		for (int i=0;i<d/3;i++) {
			n += i/2;
		}
	}
	for (int i=0;a<b;a++) {
		n += 1;
	}
	while (c>1) {
		n += c;
		c -= 20;
	}
	n += a == b;
	while (c<5) {
		for (int i = 0;d<b;i++) {
			n += b;
			for (int e = 0;a==b;i++) {
				n--;
				b--;
			}
			b--;
			a--;
		}
		c++; //C++ :D
	}
	if (n >= 2689) {n -= 2689;}
	if (a+b+c+d > 50) {n=0;}
	cout << n;
	return 0;
}