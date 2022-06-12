# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 17:38:23 2021

@author: Aarna
"""

import sys
 
 
class MAX_HEAP: 
    
    def __init__(self, MAXSIZE):
        
        self.MAXSIZE = MAXSIZE
        self.heap_size = 0
        
        self.Key = [0]*(self.MAXSIZE + 1)
        self.Key[0] = sys.maxsize
        
        self.DocID = [0]*(self.MAXSIZE + 1)
        self.DocID[0] = sys.maxsize
        
        self.root = 1
 
 
    
    def interchange_node(self, node1, node2):
        self.Key[node1], self.Key[node2] = self.Key[node2], self.Key[node1]
        self.DocID[node1], self.DocID[node2] = self.DocID[node2], self.DocID[node1]
  
    
    def max_heap_adjust(self, i):
        if not (i >= (self.heap_size//2) and i <= self.heap_size):
            if (self.Key[i] < self.Key[2 * i]  or  self.Key[i] < self.Key[(2 * i) + 1]): 
                if self.Key[2 * i] > self.Key[(2 * i) + 1]:     
                    self.interchange_node(i, 2 * i)
                    self.max_heap_adjust(2 * i)
  
                else:
                    self.interchange_node(i, (2 * i) + 1)
                    self.max_heap_adjust((2 * i) + 1)
  
 
 
    def insertMaxHeap(self, element, docID):
        if self.heap_size >= self.MAXSIZE :
            return
        self.heap_size+= 1
        
        self.Key[self.heap_size] = element 
        self.DocID[self.heap_size]= docID
        
        current = self.heap_size
        while self.Key[current] > self.Key[current//2]:
            self.interchange_node(current, current//2)
            current = current//2
  
  
    def extractMax(self):
        
        max_ele = self.Key[self.root]
        docID = self.DocID[self.root]
        
        self.Key[self.root] = self.Key[self.heap_size]
        self.DocID[self.root] = self.DocID[self.heap_size]
                
        self.heap_size -= 1
        
        self.max_heap_adjust(self.root)
        
        return docID, max_ele 
  
  
    def build_heap(self): 
        for i in range(self.heap_size//2, 0, -1):
            self.max_heap_adjust(i)
  
  
    def print_heap(self):
        for i in range(1, (self.heap_size//2)+1):
            print("Parent : "+ str(self.Key[i])+\
                "\nLeft Child : "+ str(self.Key[2 * i]) + \
                "\nRight Child : "+ str(self.Key[2 * i + 1]));
  

    
    def printKtop(self):
        for i in range(1, self.heap_size):
            print(self.extractMax());


def getTopK(DocumentScoreList, K):
    
    MaxHeap = MAX_HEAP(len(DocumentScoreList)+1)
    
    for i in range(0, len(DocumentScoreList)):
        MaxHeap.insertMaxHeap(float(DocumentScoreList[i][1]),int(DocumentScoreList[i][0]) );
    
    
    TopKDocs=[];
    
    #Retrieve top K from heap  
    for i in range(0, K):
        dID, score = MaxHeap.extractMax();
        TopKDocs.append([dID, score]);
        
    return TopKDocs;
    


  
if __name__=="__main__":     
    
    MH = MAX_HEAP(10+1)
    
    MH.insertMaxHeap(15.54 , 1)
    MH.insertMaxHeap(7.454 , 2 )
    MH.insertMaxHeap(0.9, 3)
    MH.insertMaxHeap(4.6 , 4)
    MH.insertMaxHeap(1.3, 5)
    MH.insertMaxHeap(1.5 , 6)
    MH.insertMaxHeap(0.27 , 7 )
    MH.insertMaxHeap(0.9, 8)
    MH.insertMaxHeap(4.0, 9)
    MH.insertMaxHeap(4.656 , 10)
    
    MH.printKtop();
    
    
    
    MH.print_heap()
    
    print(MH.heap_size)
    


