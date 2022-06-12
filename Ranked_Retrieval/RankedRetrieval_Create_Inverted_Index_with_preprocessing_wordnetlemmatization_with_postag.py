
# -*- coding: utf-8 -*-

"""
Created on Fri Nov 26 17:47:45 2021

@author: Arpita Nema

@StudentID : 2021pcs1018 


"""


import os
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

import json
from nltk.corpus import wordnet
from collections import defaultdict



stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def get_pos_tag(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:         
        return None
 
Allwords=[]

def preprocessWordnetLemmaPOSTag(D ):
    
    global Allwords
    
    #CASE NORMALIZATION
    CaseNormalizedText = D.lower()
    
    
    #Getting TOKENS - POSTags - LemmatizedWords
    pos_tagged_text = nltk.pos_tag(nltk.word_tokenize(CaseNormalizedText)) 

    pos_tagged_list = list(map(lambda x: (x[0], get_pos_tag(x[1])), pos_tagged_text))
    #print(pos_tagged_list)
    
    lemmatized_words = []
    for word, tag in pos_tagged_list:
        if tag is None:
            
            lemmatized_words.append(word)
        else:       
            
            lemmatized_words.append(lemmatizer.lemmatize(word, tag))
   
     
    #print(lemmatized_words)
    

    words = [word for word in lemmatized_words if word.isalpha()]

    wordList = []
    
    
    for w in words:
        if  w not in stop_words and len(w) > 2 : 
            wordList.append(w)

    Allwords=wordList;
    DocumentVocabulary = sorted(list(set(wordList)))

    return DocumentVocabulary




def Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization_With_POStag(folder , subfolder ):
    
    
    
    
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
        
        WordBag=preprocessWordnetLemmaPOSTag(file_text );
       
        for word in WordBag:
            
            inverted_index[word][file]=Allwords.count(word)
    

    print("\nInverted Index with preprocessing (WordNet lemmatization with POS) constructed successfully..");
    #print(inverted_index['employees']);  
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_with_postag.json'    
    
    with open(IDX_FILE_NAME, 'w') as fp:
        json.dump(inverted_index, fp)
        
    
    
if __name__=="__main__":    
    
    
    
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    
    Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization_With_POStag(folder , subfolder  )
    
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_with_postag.json'    
    
    with open(IDX_FILE_NAME) as json_file:
        index_read = json.load(json_file)
    
    try:
    
        print(index_read[preprocessWordnetLemmaPOSTag('andromeda')[0]]);  
    except Exception as e:
        print(type(e))
    
        
    
    
    