#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
float Max(float a, float b){ if( a>b) return a;else return b;}
float Min(float a, float b){if(a<b) return a;else return b;}
void solve() {
    ll n;
    cin>>n;
    ll arr[n];
    ll add = 0;
    for(int i = 0;i<n-1;i++){
        cin>>arr[i];
        add += arr[i];
    }
    cout<<n*(n+1)/2-add<<endl;
 
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    ll t=1;
    //cin>>t;
    while (t--){
        solve();
    }
}
