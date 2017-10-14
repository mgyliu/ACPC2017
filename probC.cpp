#include <iostream>
#include <string>
#include <vector>

int main() {
	int n;
	int m;
	double result;
    while(std::cin>>n){
    	while(std::cin>>m){
    		result = double(n)/double(m);
    		std::cout << result << std::endl;
    		break;
    	}
    }
}