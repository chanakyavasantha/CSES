#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
float Max(float a, float b){ if( a>b) return a;else return b;}
float Min(float a, float b){if(a<b) return a;else return b;}
#define mod 1000000007
void solve() {
    ll n;
    cin>>n;
    ll ans = 1;
    for(int i = 0;i<n;i++){
        ans *= 2;
        ans %= mod;
    }
    cout<<ans<<endl;
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
