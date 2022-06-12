# -*- coding: utf-8 -*-

"""
Created on Fri Nov 26 17:47:45 2021

@author: Arpita Nema

@StudentID : 2021pcs1018 


"""


#import os
import time
import json


from Create_Inverted_Index_with_preprocessing_wordnetlemmatization_without_postag import preprocessWordnetLemma
#from Create_Inverted_Index_with_preprocessing_wordnetlemmatization_without_postag import Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization
from Create_Inverted_Index_with_preprocessing_wordnetlemmatization_with_postag import preprocessWordnetLemmaPOSTag

from Create_Inverted_Index_with_preprocessing_lemmatization_spacy import preprocessSpacyLemma


#from Create_Inverted_Index_without_preprocessing import getTokens
#from Create_Inverted_Index_without_preprocessing import Create_Inverted_Index_Without_Preprocessing

def getPostingPreprocessLemmatizerSpacy(term ,inverted_index_lemmatizer_spacy ):
    try:
        PT =inverted_index_lemmatizer_spacy[preprocessSpacyLemma(term)[0]];
    except Exception as e:
        print(type(e))
        print(term + " Key Not found in inverted_index constructed using Spacy Lemmatizer ")

        PT=[];
            
    return PT

def getPostingPreprocessWordNetLemmatizerWithoutPOS(term ,inverted_index_wordnetlemmatizer_without_POStags ):
    try:
        PT =inverted_index_wordnetlemmatizer_without_POStags[preprocessWordnetLemma(term)[0]];
    except Exception as e:
        print(type(e))
        print(term + " Key Not found in inverted_index constructed using WordNet Lemmatizer without POS Tags")

        PT=[];
            
    return PT


def getPostingPreprocessWordNetLemmatizerWithPOS(term ,inverted_index_wordnetlemmatizer_with_POStags ):
    
    try:
        PT =inverted_index_wordnetlemmatizer_with_POStags[preprocessWordnetLemmaPOSTag(term)[0]]; 
    except Exception as e:
        print(type(e))
        print(term + " Key Not found in inverted_index constructed using WordNet Lemmatizer with POS Tags")
        PT=[];
            
    return PT
    
    

def getPostingWithoutPreprocess(term ,inverted_index_without_preprocess ):
    
    try:
        PT =inverted_index_without_preprocess[term]; 
    except Exception as e:
        print(type(e))
        print(term + " Key Not found in inverted_index constructed without preprocessing")
        PT=[];
            
    return PT







def f_and(postingList1, postingList2):
    p1 = 0
    p2 = 0
    resultant_list = list()
    while p1 < len(postingList1) and p2 < len(postingList2):
        if postingList1[p1] == postingList2[p2]:
            resultant_list.append(postingList1[p1])
            p1 += 1
            p2 += 1
        elif postingList1[p1] > postingList2[p2]:
            p2 += 1
        else:
            p1 += 1
    return resultant_list

def f_or(postingList1, postingList2):
    p1 = 0
    p2 = 0
    resultant_list = list()
    while p1 < len(postingList1) and p2 < len(postingList2):
        if postingList1[p1] == postingList2[p2]:
            resultant_list.append(postingList1[p1])
            p1 += 1
            p2 += 1
        elif postingList1[p1] > postingList2[p2]:
            resultant_list.append(postingList2[p2])
            p2 += 1
        else:
            resultant_list.append(postingList1[p1])
            p1 += 1
    while p1 < len(postingList1):
        resultant_list.append(postingList1[p1])
        p1 += 1
    while p2 < len(postingList2):
        resultant_list.append(postingList2[p2])
        p2 += 1
    return resultant_list

    
    
if __name__=="__main__":    
    
    
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    
    
    
    
    
    print("How u want to proceed ..? \n1. User Input \n2. Pre-stored terms ")
    
    ch=input("Enter choice : ")
    
    if(ch=='1'):
        term1 = input("Enter term1 : ")
        term2 = input("Enter term2 : ")
        term3 = input("Enter term3 : ")
        term4 = input("Enter term4 : ")
        
    else:
 
        term1 ='shuttle'
        term2='clear'
        term3='abomination'
        term4 ='accounting'
        
    print("--------------------------------------------------------------------------------------------")
    
    ###----Without Preprocessing----------------------------------------------------------------------------
    IDX_FILE_NAME__without_preprocess =subfolder.replace(".", "_")+'_inverted_index_without_preprocesing.json'    
    
    start_time1 = time.time()    
    with open(IDX_FILE_NAME__without_preprocess) as json_file2:
        inverted_index_without_preprocess = json.load(json_file2)
          
    #Getting Posting List
    IIWP_Pterm_1 = getPostingWithoutPreprocess(term1 ,inverted_index_without_preprocess );
    IIWP_Pterm_2 = getPostingWithoutPreprocess(term2 ,inverted_index_without_preprocess );
    IIWP_Pterm_3 = getPostingWithoutPreprocess(term3 ,inverted_index_without_preprocess);
    IIWP_Pterm_4 = getPostingWithoutPreprocess(term4 ,inverted_index_without_preprocess);
     
    Res1_withoutPreprocess=f_and(f_or(IIWP_Pterm_1, IIWP_Pterm_2),f_or(IIWP_Pterm_3, IIWP_Pterm_4)) 
    Res2_withoutPreprocess=f_or(f_and(IIWP_Pterm_1, IIWP_Pterm_2),f_and(IIWP_Pterm_3, IIWP_Pterm_4)) 
    
    end_time1 = time.time()
    print("\nSTATS : Inverted Index Created Without Preprocessing")
    print("Size (No. of terms in dictionary) - " + str(len(inverted_index_without_preprocess)) )
        
    print("Retrieval Speed  -  %s seconds " % (end_time1 - start_time1))
    
    print("Query 1 : ("+term1+" and "+term2+") or ("+term3+" and "+term4+")")
    print(Res1_withoutPreprocess)
    print("Query 2 : ("+term1+" or "+term2+") and ("+term3+" or "+term4+")")
    print(Res2_withoutPreprocess)


    print("--------------------------------------------------------------------------------------------")


    
    
    ##---------WithPreprocessing--WordNetLemmatization---without POSTags----------------
    
    IDX_FILE_NAME_with_wordnetlemmatizer_without_pos =subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_without_postag.json'    
   
    start_time2 = time.time()  
    with open(IDX_FILE_NAME_with_wordnetlemmatizer_without_pos) as json_file1:
        inverted_index_wordnetlemmatizer_without_POStags = json.load(json_file1)

    #Getting Posting List
    WL_Pterm_1 = getPostingPreprocessWordNetLemmatizerWithoutPOS(term1 ,inverted_index_wordnetlemmatizer_without_POStags );
    WL_Pterm_2 = getPostingPreprocessWordNetLemmatizerWithoutPOS(term2 ,inverted_index_wordnetlemmatizer_without_POStags );
    WL_Pterm_3 = getPostingPreprocessWordNetLemmatizerWithoutPOS(term3 ,inverted_index_wordnetlemmatizer_without_POStags);
    WL_Pterm_4 = getPostingPreprocessWordNetLemmatizerWithoutPOS(term4 ,inverted_index_wordnetlemmatizer_without_POStags);
    
    Res1_wordnet_lemma=f_and(f_or(WL_Pterm_1, WL_Pterm_2),f_or(WL_Pterm_3, WL_Pterm_4)) 
    Res2_wordnet_lemma=f_or(f_and(WL_Pterm_1, WL_Pterm_2),f_and(WL_Pterm_3, WL_Pterm_4)) 
   
    print("\nSTATS : Inverted Index Created With Preprocessing (wordnetlemmatization without POS tags)")
    print("Size (No. of terms in dictionary) - " + str(len(inverted_index_wordnetlemmatizer_without_POStags)) )
    
    end_time2 = time.time()  
    print("Retrieval Speed  -  %s seconds " % (end_time2 - start_time2))
    
    print("Query 1 : ("+term1+" and "+term2+") or ("+term3+" and "+term4+")")
    print(Res1_wordnet_lemma)
    print("Query 2 : ("+term1+" or "+term2+") and ("+term3+" or "+term4+")")
    print(Res2_wordnet_lemma)
    print("--------------------------------------------------------------------------------------------")

    
    
    
    
    ##---------WithPreprocessing--WordNetLemmatization---with POSTags----------------
    
    IDX_FILE_NAME_with_wordnetlemmatizer_with_pos =subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_with_postag.json'    
   
    start_time3 = time.time()  
    with open(IDX_FILE_NAME_with_wordnetlemmatizer_with_pos) as json_file3:
        inverted_index_wordnetlemmatizer_with_POStags = json.load(json_file3)

    #Getting Posting List
    WLPOS_Pterm_1 = getPostingPreprocessWordNetLemmatizerWithPOS(term1 ,inverted_index_wordnetlemmatizer_with_POStags );
    WLPOS_Pterm_2 = getPostingPreprocessWordNetLemmatizerWithPOS(term2 ,inverted_index_wordnetlemmatizer_with_POStags );
    WLPOS_Pterm_3 = getPostingPreprocessWordNetLemmatizerWithPOS(term3 ,inverted_index_wordnetlemmatizer_with_POStags);
    WLPOS_Pterm_4 = getPostingPreprocessWordNetLemmatizerWithPOS(term4 ,inverted_index_wordnetlemmatizer_with_POStags);
    
    Res1_wordnet_lemma_with_pos=f_and(f_or(WLPOS_Pterm_1, WLPOS_Pterm_2),f_or(WLPOS_Pterm_3, WLPOS_Pterm_4)) 
    Res2_wordnet_lemma_with_pos=f_or(f_and(WLPOS_Pterm_1, WLPOS_Pterm_2),f_and(WLPOS_Pterm_3, WLPOS_Pterm_4)) 
   
    print("\nSTATS : Inverted Index Created With Preprocessing (wordnetlemmatization with POS tags)")
    print("Size (No. of terms in dictionary) - " + str(len(inverted_index_wordnetlemmatizer_with_POStags)) )
    
    end_time3 = time.time()  
    print("Retrieval Speed  -  %s seconds " % (end_time3 - start_time3))
    
    print("Query 1 : ("+term1+" and "+term2+") or ("+term3+" and "+term4+")")
    print(Res1_wordnet_lemma_with_pos)
    print("Query 2 : ("+term1+" or "+term2+") and ("+term3+" or "+term4+")")
    print(Res2_wordnet_lemma_with_pos)
    print("--------------------------------------------------------------------------------------------")
    
    
    
    
    
    
    ##---------WithPreprocessing--Lemmatization---SPACY----------------
    
    IDX_FILE_NAME_with_lemmatizer_spacy =subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_lemmatization_spacy.json'    
   
    start_time4 = time.time()  
    with open(IDX_FILE_NAME_with_lemmatizer_spacy) as json_file4:
        inverted_index_lemmatizer_spacy = json.load(json_file4)

    #Getting Posting List
    LS_Pterm_1 = getPostingPreprocessLemmatizerSpacy(term1 ,inverted_index_lemmatizer_spacy );
    LS_Pterm_2 = getPostingPreprocessLemmatizerSpacy(term2 ,inverted_index_lemmatizer_spacy );
    LS_Pterm_3 = getPostingPreprocessLemmatizerSpacy(term3 ,inverted_index_lemmatizer_spacy);
    LS_Pterm_4 = getPostingPreprocessLemmatizerSpacy(term4 ,inverted_index_lemmatizer_spacy);
    
    Res1_spacy_lemma=f_and(f_or(LS_Pterm_1, LS_Pterm_2),f_or(LS_Pterm_3, LS_Pterm_4)) 
    Res2_spacy_lemma=f_or(f_and(LS_Pterm_1,LS_Pterm_2),f_and(LS_Pterm_3, LS_Pterm_4)) 
   
    print("\nSTATS : Inverted Index Created With Preprocessing (lemmatization - Spacy)")
    print("Size (No. of terms in dictionary) - " + str(len(inverted_index_lemmatizer_spacy)) )
    
    end_time4 = time.time()  
    print("Retrieval Speed  -  %s seconds " % (end_time4 - start_time4))
    
    print("Query 1 : ("+term1+" and "+term2+") or ("+term3+" and "+term4+")")
    print(Res1_spacy_lemma)
    print("Query 2 : ("+term1+" or "+term2+") and ("+term3+" or "+term4+")")
    print(Res2_spacy_lemma)
    print("--------------------------------------------------------------------------------------------")
    
    
    
    