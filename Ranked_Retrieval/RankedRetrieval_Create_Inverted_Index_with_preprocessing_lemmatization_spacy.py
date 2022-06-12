# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 12:00:53 2021

@author: Aarna
"""



# -*- coding: utf-8 -*-

"""
Created on Fri Nov 26 17:47:45 2021

@author: Arpita Nema

@StudentID : 2021pcs1018 


"""


import os
import spacy
import json
from collections import defaultdict

Allwords=[]

nlp = spacy.load('en_core_web_sm')

stop_words = nlp.Defaults.stop_words

def preprocessSpacyLemma(D ):
    
    global Allwords
    
    #CASE NORMALIZATION
    CaseNormalizedText = D.lower()
    
    
    spacyDoc= nlp(CaseNormalizedText)
    
    #TOKENIZATION
    lemmatizedtokens = []
    for token in spacyDoc:
        lemmatizedtokens.append(token.lemma_)
    
    #print(lemmatizedtokens)
    
    wordList = []
    
    
    for w in lemmatizedtokens:
        if  w not in stop_words and len(w.strip()) > 2 and  w.isalpha(): 
            wordList.append(w.strip())
    
    Allwords=wordList;

    DocumentVocabulary = sorted(list(set(wordList)))

    return DocumentVocabulary




def Create_Inverted_Index_With_Preprocessing_lemmatization_spacy(folder , subfolder ):
   
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
        
        WordBag=preprocessSpacyLemma(file_text );
       
        for word in WordBag:
            
            inverted_index[word][file]=Allwords.count(word)

    print("\nInverted Index with preprocessing (lemmatization using Spacy) constructed successfully..");
    
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_lemmatization_spacy.json'    
    
    with open(IDX_FILE_NAME, 'w') as fp:
        json.dump(inverted_index, fp)
        
    
    
if __name__=="__main__":    
    
    
    
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    
    Create_Inverted_Index_With_Preprocessing_lemmatization_spacy(folder , subfolder  )
    
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_lemmatization_spacy.json'    
    
    with open(IDX_FILE_NAME) as json_file:
        index_read = json.load(json_file)
    
    
    try:
    
        print(index_read[preprocessSpacyLemma('andromeda')[0]]);  
    except Exception as e:
        print(type(e))
    
    
    
        
    
    
    