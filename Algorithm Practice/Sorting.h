//
//  Sorting.h
//  Algorithm Practice
//
//  Created by 한동훈 on 02/07/2019.
//  Copyright © 2019 한동훈. All rights reserved.
//

#ifndef Sorting_h
#define Sorting_h

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

#endif /* Sorting_h */
