# -*- coding: utf-8 -*-

"""
Created on Fri Nov 26 17:47:45 2021

@author: Arpita Nema

@StudentID : 2021pcs1018 


"""


import os
from nltk.tokenize import word_tokenize
import json
from collections import defaultdict

Allwords=[]

def getTokens(D):
    
    global Allwords
    tokens = word_tokenize(D)
    

    Allwords=tokens;
    DocumentVocabulary = sorted(list(set(tokens)))
    
    return DocumentVocabulary




def Create_Inverted_Index_Without_Preprocessing(folder , subfolder):
    folder_content=(os.listdir(folder));
    
    inverted_index = defaultdict(dict)
    folder_content = sorted(list(folder_content))
    
    for file in folder_content:
        
        try:
            file_content = open(folder+"\\" +  file,"r")
            file_text=file_content.read()
            print("File " + file + " processed... ");
        except Exception as e:
            print(e)
            print("Unable to process file " + file );
            continue
        
        WordBag=getTokens(file_text);
       
        for word in WordBag:
                
            inverted_index[word][file]=Allwords.count(word)
    
    

    print("\nInverted Index without any preprocessing constructed successfully..");
    #print(inverted_index['employees']);  
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_without_preprocesing.json'    
    
    with open(IDX_FILE_NAME, 'w') as fp:
        json.dump(inverted_index, fp)
        
    
    
if __name__=="__main__":    
    
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    
    Create_Inverted_Index_Without_Preprocessing(folder , subfolder)
    
    
     
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_without_preprocesing.json'    
    
    with open(IDX_FILE_NAME) as json_file:
        index_read = json.load(json_file)
    
    print(index_read['employees']);  
    
    
    
    
    
    