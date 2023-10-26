#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
float Max(float a, float b){ if( a>b) return a;else return b;}
float Min(float a, float b){if(a<b) return a;else return b;}
void solve() {
    string s;
    cin>>s;
    set<char> set1;
    for(char x: s){
        set1.insert(x);
    }
    int ans = 0;
    for(char y : set1){
        int count = 0;
        for(char i : s){
            if(y == i)
                count++;
            else{
                ans = Max(count,ans);
                count = 0;
            }
        }
        ans = Max(count,ans);
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
