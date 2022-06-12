# -*- coding: utf-8 -*-

"""
Created on Fri Nov 26 17:47:45 2021

@author: Arpita Nema

@StudentID : 2021pcs1018 


"""


import os
import time
import json
import sys
import math
from collections import defaultdict

from Heap import getTopK
from prettytable import PrettyTable

from RankedRetrieval_Create_Inverted_Index_with_preprocessing_wordnetlemmatization_without_postag \
import preprocessWordnetLemma

from RankedRetrieval_Create_Inverted_Index_with_preprocessing_wordnetlemmatization_with_postag \
import preprocessWordnetLemmaPOSTag

from RankedRetrieval_Create_Inverted_Index_with_preprocessing_lemmatization_spacy \
import preprocessSpacyLemma


from RankedRetrieval_Create_Inverted_Index_without_preprocessing import getTokens


def idf_weight(term,document_frequency):
    
    if term in document_frequency.keys():
        return math.log(N / document_frequency[term], 10)
    else:
        return 0.0


def log_term_frequency_weight(term, doc_id, inverted_index):
   
    if doc_id in inverted_index[term]:
        return 1.0 + math.log(inverted_index[term][doc_id], 10)
    else:
        return 0.0



def cosine_similarity(query, doc_id, inverted_index, document_frequency, document_length):
    
    cosine_similarity = 0.0

    for term in query:

        if term in document_frequency.keys():
           
            cosine_similarity += log_term_frequency_weight(term, doc_id, inverted_index) * idf_weight(term,document_frequency)

    cosine_similarity = cosine_similarity / document_length[doc_id]

    return cosine_similarity

def compute_docs_length(document_names, document_frequecy,inverted_index):
    
    document_length=defaultdict(float)
    for doc_id in document_names:
        l = 0
        for term in document_frequecy.keys():
            l += log_term_frequency_weight(term, doc_id,inverted_index) ** 2
        document_length[doc_id] = math.sqrt(l)

    return document_length


def load_inverted_index(file_name):
    with open(file_name) as json_file1:
        inverted_index = json.load(json_file1)
    return inverted_index
        
def load_terms_document_freq(file_name):
    with open(file_name) as jf:
        terms_document_freq = json.load(jf)
    return terms_document_freq    
        

def getTopKScores(K, preprocessed_query, document_length, inverted_index ,doc_freq  ):
  
    Results=[]
    
    for doc_id in document_names:
        cos = cosine_similarity(preprocessed_query, doc_id, inverted_index , doc_freq,\
                                         document_length)
        
        """ 
        Efficient Retrieval - 
        Top K will be chosen from documents where cosine similarity is greater than 0
        """
        if(cos>0):
            Results.append((doc_id ,cos ));
    
    # When our no. of documents is less than users requirement 
    if len(Results) < K:
        K=len(Results);
    
    
    TopKResults = getTopK(Results, K );

    
    #print(TopKResults)
    #print(len(TopKResults))
    
    return TopKResults

def printScores(DocumentScoresList):
    t = PrettyTable(['Document ID', 'Score'])
    
    for i in range (0,len(DocumentScoresList)) :
        t.add_row([DocumentScoresList[i][0], DocumentScoresList[i][1]] )      
    
    

    print(t)
        
def printRetrievalSpeed(ST, ET, InvertedIndexName):
 
    retrievalSpeed = []
    zip_object = zip(ET, ST)
    for a, b in zip_object:
        retrievalSpeed.append(a-b) 
    
    #print(retrievalSpeed)
    
    
    t = PrettyTable(['Inverted Index Type',  'Retrieval Speed (seconds)'])
    
    for i in range (0,len(InvertedIndexName)) :
        #print(InvertedIndexName[i])
        t.add_row([InvertedIndexName[i],  retrievalSpeed[i]] )      
    
    

    print(t)

    return retrievalSpeed
    
    
if __name__=="__main__":    
    
    global N
    
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    
    #Load Document Names
    
    document_names=(os.listdir(folder));
    N=len(document_names);
    print("Loading Document Names....")
    
    
    #Load inverted_index
    
    ###----Without Preprocessing----------------------------------------------------------------------------
    
    print("Loading inverted_index_without_preprocesing....")
    IDX_FILE_NAME__without_preprocess =\
    subfolder.replace(".", "_")+'_inverted_index_without_preprocesing.json' 
    
    without_preprocess_doc_freq_FILE_NAME = \
    subfolder.replace(".", "_")+'_doc_freq_inverted_index_without_preprocess.json'    
 
    inverted_index_without_preprocess=\
    load_inverted_index(IDX_FILE_NAME__without_preprocess)
    
    doc_freq_inverted_index_without_preprocess=\
    load_terms_document_freq(without_preprocess_doc_freq_FILE_NAME);
    
    document_length_without_preprocess = compute_docs_length(document_names, \
                                          doc_freq_inverted_index_without_preprocess,\
                                           inverted_index_without_preprocess )   
    
    
    
    
    ##---------WithPreprocessing--WordNetLemmatization---without POSTags----------------
    
    print("Loading inverted_index_with_preprocesing_wordnetlemmatization_without_POS_tag....")
    
    IDX_FILE_NAME_with_wordnetlemmatizer_without_pos =\
    subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_without_postag.json'    
    
    doc_freq_wordnetlemmatizer_without_POStags_FILE_NAME = \
    subfolder.replace(".", "_")+'_doc_freq_inverted_index_wordnetlemmatizer_without_POStags.json'    
 
    inverted_index_wordnetlemmatizer_without_POStags=\
    load_inverted_index(IDX_FILE_NAME_with_wordnetlemmatizer_without_pos)
    
    doc_freq_inverted_index_wordnetlemmatizer_without_POStags=\
    load_terms_document_freq(doc_freq_wordnetlemmatizer_without_POStags_FILE_NAME);
    
    document_length_wordnetlemmatizer_without_pos = compute_docs_length(document_names, \
                                          doc_freq_inverted_index_wordnetlemmatizer_without_POStags,\
                                          inverted_index_wordnetlemmatizer_without_POStags )   
    
    
    ##---------WithPreprocessing--WordNetLemmatization---with POSTags----------------
    
    print("Loading inverted_index_with_preprocesing_wordnetlemmatization_with_POS_tag....")
    
    
    IDX_FILE_NAME_with_wordnetlemmatizer_with_pos =\
    subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_with_postag.json'    
       
    doc_freq_wordnetlemmatizer_with_POStags_FILE_NAME = \
    subfolder.replace(".", "_")+'_doc_freq_inverted_index_wordnetlemmatizer_with_POStags.json'    
 
    inverted_index_wordnetlemmatizer_with_POStags=\
    load_inverted_index(IDX_FILE_NAME_with_wordnetlemmatizer_with_pos)
    
    doc_freq_inverted_index_wordnetlemmatizer_with_POStags=\
    load_terms_document_freq(doc_freq_wordnetlemmatizer_with_POStags_FILE_NAME);
    
    document_length_wordnetlemmatizer_with_pos = compute_docs_length(document_names, \
                                          doc_freq_inverted_index_wordnetlemmatizer_with_POStags,\
                                          inverted_index_wordnetlemmatizer_with_POStags )   
    
    
    
    ##---------WithPreprocessing--Lemmatization---SPACY----------------
    
    print("Loading inverted_index_lemmatizer_spacy....")
    
    
    IDX_FILE_NAME_with_lemmatizer_spacy =\
    subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_lemmatization_spacy.json'    
   
    doc_freq_with_lemmatizer_spacy_FILE_NAME = \
    subfolder.replace(".", "_")+'_doc_freq_inverted_index_lemmatizer_spacy.json'    
 
    inverted_index_lemmatizer_spacy=\
    load_inverted_index(IDX_FILE_NAME_with_lemmatizer_spacy)
    
    doc_freq_inverted_index_lemmatizer_spacy=\
    load_terms_document_freq(doc_freq_with_lemmatizer_spacy_FILE_NAME);
    
    document_length_lemmatizer_spacy = compute_docs_length(document_names, \
                                          doc_freq_inverted_index_lemmatizer_spacy,\
                                          inverted_index_lemmatizer_spacy )   
    
    
    
    
    
    
    
    #------------------------------------------------------------------------
    
    
    
    print("All Inverted Index loading complete....")
    
    
    print("How u want to proceed ..? \n1. User Input \n2. Pre-stored terms ")
    
    ch=input("Enter choice : ")
    
    if(ch=='1'):
        
        query = input("Enter query : ")
        K = int(input("Enter value of K : "))
        
    else:
        query ='Space science and astronauts are related'
        query='OZONE LAYER Space FAQ 12/15 - Controversial Questions SATURN V PLANS RISKS OF NUCLEAR';
        #query='Controversial';

        K=8

    #Keeping track of retrieval speed
    ST=[];
    ET=[];
    
        
    print("--------------------------------------------------------------------------------------------")
    
    ###----Without Preprocessing----------------------------------------------------------------------------
   
    
    ST.append(time.time())
    tokenized_query =  getTokens(query);
    if tokenized_query == []:
        sys.exit()
    
    
    Scores_without_preprocess = getTopKScores(K,tokenized_query,\
                                        document_length_without_preprocess,\
                                        inverted_index_without_preprocess ,\
                                        doc_freq_inverted_index_without_preprocess   );

    print("Retrieved Documents - Inverted Index created without any preprocessing");       
                                                         
    printScores(Scores_without_preprocess);       
    
    ET.append(time.time())
    
    print("\n--------------------------------------------------------------------------------------------\n")

   
    
    
    ##---------WithPreprocessing--WordNetLemmatization---without POSTags----------------
     
    ST.append(time.time())
    preprocessed_query_wordnetlemmatizer_without_pos =  preprocessWordnetLemma(query);
    if preprocessed_query_wordnetlemmatizer_without_pos == []:
        sys.exit()
    
    
    Scores_wordnetlemmatizer_without_pos = getTopKScores(K,preprocessed_query_wordnetlemmatizer_without_pos,\
                                        document_length_wordnetlemmatizer_without_pos,\
                                        inverted_index_wordnetlemmatizer_without_POStags ,\
                                        doc_freq_inverted_index_wordnetlemmatizer_without_POStags   );
                                                         
                                                      
    print("Retrieved Documents - Inverted Index created with wordnet lemmatizer without POS tags");       
    printScores(Scores_wordnetlemmatizer_without_pos);  

    ET.append(time.time())                                                   
    
    print("\n--------------------------------------------------------------------------------------------\n")
    
    
    
    ##---------WithPreprocessing--WordNetLemmatization---with POSTags----------------
    
    ST.append(time.time())
    
    preprocessed_query_wordnetlemmatizer_with_pos =  preprocessWordnetLemmaPOSTag(query);
    if preprocessed_query_wordnetlemmatizer_with_pos == []:
        sys.exit()
    
    
    Scores_wordnetlemmatizer_with_pos = getTopKScores(K,preprocessed_query_wordnetlemmatizer_with_pos,\
                                        document_length_wordnetlemmatizer_with_pos,\
                                        inverted_index_wordnetlemmatizer_with_POStags ,\
                                        doc_freq_inverted_index_wordnetlemmatizer_with_POStags   );
                                                         
    print("Retrieved Documents - Inverted Index created with wordnet lemmatizer with POS tags");       
                                                
    printScores(Scores_wordnetlemmatizer_with_pos);                                                     
    
    
    
    ET.append(time.time())
    
    print("--------------------------------------------------------------------------------------------")
  
    
    ##---------WithPreprocessing--Lemmatization---SPACY----------------
    
    ST.append(time.time())
    preprocessed_query_lemmatizer_spacy =  preprocessSpacyLemma(query);
    if preprocessed_query_lemmatizer_spacy == []:
        sys.exit()
    
    
    Scores_lemmatizer_spacy = getTopKScores(K,preprocessed_query_lemmatizer_spacy,\
                                        document_length_lemmatizer_spacy,\
                                        inverted_index_lemmatizer_spacy ,\
                                        doc_freq_inverted_index_lemmatizer_spacy   );
                                                         

    print("Retrieved Documents - Inverted Index created with lemmatizer of spacy library");       
                                                       
    printScores(Scores_lemmatizer_spacy);                                                     
    
    ET.append(time.time())
    
    print("--------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------")
    
    
 
    InvertedIndexNames = [ 'Inverted Index created without preprocessing', \
                         'Inverted Index created with WordNet Lemmatization', \
                         'Inverted Index created with WordNet Lemmatization with POS Tags', \
                         'Inverted Index created with lemmatization from spacy' \
                         ]
    printRetrievalSpeed(ST, ET, InvertedIndexNames)
    
    