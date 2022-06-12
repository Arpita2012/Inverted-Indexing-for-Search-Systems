# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 15:52:14 2021

@author: Aarna
"""

import time
import json
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


from RankedRetrieval_Create_Inverted_Index_without_preprocessing \
import Create_Inverted_Index_Without_Preprocessing

from RankedRetrieval_Create_Inverted_Index_with_preprocessing_wordnetlemmatization_without_postag \
import Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization

from RankedRetrieval_Create_Inverted_Index_with_preprocessing_wordnetlemmatization_with_postag \
import Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization_With_POStag

from RankedRetrieval_Create_Inverted_Index_with_preprocessing_lemmatization_spacy \
import Create_Inverted_Index_With_Preprocessing_lemmatization_spacy

from prettytable import PrettyTable
from collections import defaultdict


def create_document_frequency_dictionary(inverted_index):
    
    
    document_frequency= defaultdict(int);
    
    for term in inverted_index.keys():
        document_frequency[term] = len(inverted_index[term])

    return document_frequency


if __name__=="__main__":    
   
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    ST=[]
    ET=[]
    
    ST.append(time.time()) 
    Create_Inverted_Index_Without_Preprocessing(folder ,subfolder)
    ET.append(time.time())
    print("\n------------------------------------------------------\n")
    
    ST.append(time.time()) 
    Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization(folder ,subfolder)
    ET.append(time.time())
    print("\n------------------------------------------------------\n")
    
    ST.append(time.time()) 
    Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization_With_POStag(folder ,subfolder)
    ET.append(time.time())
    print("\n------------------------------------------------------\n")

    
    ST.append(time.time()) 
    Create_Inverted_Index_With_Preprocessing_lemmatization_spacy(folder ,subfolder)
    ET.append(time.time())
    print("\n------------------------------------------------------\n")

    
    
    
    IndexSize=[];
    
    
    ###----Without Preprocessing----------------------------------------------------------------------------
    IDX_FILE_NAME__without_preprocess =subfolder.replace(".", "_")+'_inverted_index_without_preprocesing.json'    
    
      
    with open(IDX_FILE_NAME__without_preprocess) as json_file1:
        inverted_index_without_preprocess = json.load(json_file1)
    
    IndexSize.append(len(inverted_index_without_preprocess))    
    
    #--Document Freq.---
    doc_freq_inverted_index_without_preprocess=create_document_frequency_dictionary(inverted_index_without_preprocess);
    
    doc_freq_FILE_NAME = subfolder.replace(".", "_")+'_doc_freq_inverted_index_without_preprocess.json'    
    
    with open(doc_freq_FILE_NAME, 'w') as fp:
        json.dump(doc_freq_inverted_index_without_preprocess, fp)
        
    ##---------WithPreprocessing--WordNetLemmatization---without POSTags----------------
    
    IDX_FILE_NAME_with_wordnetlemmatizer_without_pos=subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_without_postag.json'    
   
      
    with open(IDX_FILE_NAME_with_wordnetlemmatizer_without_pos) as json_file2:
        inverted_index_wordnetlemmatizer_without_POStags = json.load(json_file2)    
    
    IndexSize.append(len(inverted_index_wordnetlemmatizer_without_POStags))   
    
    
    #--Document Freq.---
    doc_freq_inverted_index_wordnetlemmatizer_without_POStags=create_document_frequency_dictionary(inverted_index_wordnetlemmatizer_without_POStags);
    
    doc_freq_FILE_NAME = subfolder.replace(".", "_")+'_doc_freq_inverted_index_wordnetlemmatizer_without_POStags.json'    
    
    with open(doc_freq_FILE_NAME, 'w') as fp:
        json.dump(doc_freq_inverted_index_wordnetlemmatizer_without_POStags, fp)
        
       
    
    
     ##---------WithPreprocessing--WordNetLemmatization---with POStags----------------
    
    IDX_FILE_NAME_with_wordnetlemmatizer_with_pos =subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_with_postag.json'    
   
    
    with open(IDX_FILE_NAME_with_wordnetlemmatizer_with_pos) as json_file3:
        inverted_index_wordnetlemmatizer_with_POStags = json.load(json_file3)
    
    IndexSize.append(len(inverted_index_wordnetlemmatizer_with_POStags))  
    
    #--Document Freq.---
    doc_freq_inverted_index_wordnetlemmatizer_with_POStags=create_document_frequency_dictionary(inverted_index_wordnetlemmatizer_with_POStags);
    
    doc_freq_FILE_NAME = subfolder.replace(".", "_")+'_doc_freq_inverted_index_wordnetlemmatizer_with_POStags.json'    
    
    with open(doc_freq_FILE_NAME, 'w') as fp:
        json.dump(doc_freq_inverted_index_wordnetlemmatizer_with_POStags, fp)
        
    
    
    
    
    ##---------WithPreprocessing--Lemmatization---SPACY----------------
    
    IDX_FILE_NAME_with_lemmatizer_spacy =subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_lemmatization_spacy.json'    
   
   
    with open(IDX_FILE_NAME_with_lemmatizer_spacy) as json_file4:
        inverted_index_lemmatizer_spacy = json.load(json_file4)
    
    IndexSize.append(len(inverted_index_lemmatizer_spacy))  

    
    #--Document Freq.---
    doc_freq_inverted_index_lemmatizer_spacy=create_document_frequency_dictionary(inverted_index_lemmatizer_spacy);
    
    doc_freq_FILE_NAME = subfolder.replace(".", "_")+'_doc_freq_inverted_index_lemmatizer_spacy.json'    
    
    with open(doc_freq_FILE_NAME, 'w') as fp:
        json.dump(doc_freq_inverted_index_lemmatizer_spacy, fp)
        
    

    ##--------------------------------------------------------------------------------------------
    
    InvertedIndexName = [ 'I.I. without preprocessing', \
                         'I.I. with WordNet Lemmatization', \
                         'I.I. with WordNet Lemmatization with POS Tags', \
                         'I.I. with lemmatization from spacy' \
                         ]
    
    IndexConstructionTime = []
    zip_object = zip(ET, ST)
    for a, b in zip_object:
        IndexConstructionTime.append(a-b) 
    
    #print(IndexConstructionTime)
    
    
    t = PrettyTable(['Inverted Index Type', 'Index Size', 'Construction Time (seconds)'])
    
    for i in range (0,len(InvertedIndexName)) :
        t.add_row([InvertedIndexName[i], IndexSize[i], IndexConstructionTime[i]] )      
    
    

    print(t)
        
    
    
    
    
    fig, ax = plt.subplots()
    ax.plot_date(InvertedIndexName, IndexConstructionTime, color='red', linestyle='dashed', linewidth = 2,
     marker='o', markerfacecolor='blue', markersize=10 )
    
    plt.ylabel('Index Construction Time (seconds)')
    plt.xlabel('Inverted Index Type')  
    plt.grid(linestyle = '--', linewidth = 0.6)              
    plt.title('Inverted Index Construction Time ')  
    fig.autofmt_xdate()        
    plt.savefig('Inverted Index Construction Time')
    plt.show()
    


    fig, ax = plt.subplots()
    ax.plot_date(InvertedIndexName, IndexSize, color='red', linestyle='dashed', linewidth = 2,
     marker='o', markerfacecolor='blue', markersize=10 )
    
    plt.ylabel('Index Size (No. of terms in dictionary) ')
    plt.xlabel('Inverted Index Type')  
    plt.grid(linestyle = '--', linewidth = 0.6)              
    plt.title('Inverted Index Size ')  
    fig.autofmt_xdate()        
    plt.savefig('Inverted Index Size')
    plt.show()            
    
    
    
    