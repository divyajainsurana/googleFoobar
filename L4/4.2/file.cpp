#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    while(T--){
        int n, x, totodd = 0;
        scanf("%d%d", &n, &x);
        for(int i = 1; i <= n; i++)
        {
            int c;
            scanf("%d", &c);
            if(c % 2 == 1)
                totodd++;
        }
        int toteven = n - totodd;
        bool flag = false;
        for(int i = 1; i <= totodd; i += 2)
        {	
        	
            if(toteven >= x - i && x - i >= 0)
            {
                flag = true;
                break;
            }
        }
        if(flag)printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

