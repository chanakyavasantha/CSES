#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
float Max(float a, float b){ if( a>b) return a;else return b;}
float Min(float a, float b){if(a<b) return a;else return b;}
void solve() {
    ll n;
    cin>>n;
    ll arr[n];
    for(int i = 0;i<n;i++){
        cin>>arr[i];
    }
    ll ans = 0;
    for(int i = 0;i<n-1;i++){
        if(arr[i+1] < arr[i]){
            int k = arr[i]-arr[i+1];
            ans += k;
            arr[i+1] = arr[i];
        }
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