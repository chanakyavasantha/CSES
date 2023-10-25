#include <bits/stdc++.h>
using namespace std;
 
int main(){
    long long n;
    cin>>n;
    while( n != 1){
        if(n%2){
            cout<<n<<" ";
            n *= 3;
            n += 1;
        }
        else{
            cout<<n<<" ";
            n /= 2;
        }
    }
    cout<<1<<" ";
}
