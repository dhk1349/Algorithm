//
//  main.cpp
//  Algorithm Practice
//
//  Created by 한동훈 on 02/07/2019.
//  Copyright © 2019 한동훈. All rights reserved.
//
void swap(int &a, int &b);
void printarray(int a[], int n);
void Bubble(int a[],int n);
void Counting(int a[],int size, int range);

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int a[10]={10,9,8,7,6,5,4,3,2,1};
    Bubble(a,10);
    
    Counting(a,10,11);
    return 0;
}

void swap(int &a, int &b){
    int temp=a;
    a=b;
    b=temp;
}
void printarray(int a[], int n){
    for(int i=0;i<n;i++){
        cout<<a[i]<<"    ";
    }
}

void Bubble(int a[],int n){
    for(int i=0;i<n-1;i++){ //index
        for(int j=0;j<n-1;j++){
            if(a[j]>a[j+1]) swap(a[j],a[j+1]);
        }
    }
    printarray(a,n);
}

void Merge(int a[], int n){
//   Sort with recursive method
    
}

void Tree(int a[], int n){
    //    Each level starts with 2^(n-1) and n stands for level;
}

void Counting(int a[],int size, int range){
    //    range  from 0 to range-1;
    int *countarr=new int [size]();
    for(int i=0;i<size;i++){
        countarr[a[i]]+=1;
    }
    printarray(countarr, range);
    delete[] countarr ;
}
