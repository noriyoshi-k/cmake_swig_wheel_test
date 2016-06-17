#include "test.hpp"

void multiply(short* buf,int n)
{
    for(int i=0;i<n;i++){
        buf[i]/=2.;
    }
}
