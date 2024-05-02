#include<iostream>
using namespace std;


int main(){
    int cnt,i,*ptr,sum=0;
    cout<<"How many elements";
    cin>>cnt;
    
    ptr=(int*)malloc(cnt * sizeof(int));
    cout<<"EDnter the elements";
    for(i=0;i<cnt;i++)
    {
        cin>>*(ptr+i);
        sum+=*(ptr+i);
    }
    cout<<"Sum of elements"<<sum;
    free(ptr);
    return 0;
}