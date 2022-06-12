

# -*- coding: utf-8 -*-

"""
Created on Fri Nov 26 17:47:45 2021

@author: Arpita Nema

@StudentID : 2021pcs1018 


"""


import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

import json



stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocessWordnetLemma(D ):
    
    #CASE NORMALIZATION
    CaseNormalizedText = D.lower()
    
    #TOKENIZATION
    tokens = word_tokenize(CaseNormalizedText)
    
    
    words = [word for word in tokens if word.isalpha()]

    wordList = []
    
    #LEMMATIZATON
    for w in words:
        if  w not in stop_words and len(w) > 2 : 
            wordList.append(lemmatizer.lemmatize(w))


    DocumentVocabulary = sorted(list(set(wordList)))

    return DocumentVocabulary




def Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization(folder , subfolder ):
    
    
    
    
    folder_content=(os.listdir(folder));

    inverted_index = {}
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
        
        WordBag=preprocessWordnetLemma(file_text );
       
        for word in WordBag:
            if word in inverted_index:
                inverted_index[word].append(file)
            else:
                inverted_index[word] = [file]
    
    

    print("\nInverted Index with preprocessing (wordnetlemmatization without POSTags) constructed successfully..");
    
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_without_postag.json'    
    
    with open(IDX_FILE_NAME, 'w') as fp:
        json.dump(inverted_index, fp)
        
    
    
if __name__=="__main__":    
    
    
    
    subfolder="sci.space";
    folder=r"E:\IIT Jammu\Data Organization and Retrieval\Assignment 3\20_newsgroups\\"+subfolder;
    
    Create_Inverted_Index_With_Preprocessing_Wordnetlemmatization(folder , subfolder  )
    
    
    
    IDX_FILE_NAME = subfolder.replace(".", "_")+'_inverted_index_with_preprocesing_wordnetlemmatization_without_postag.json'    
    
    with open(IDX_FILE_NAME) as json_file:
        index_read = json.load(json_file)
    
    
    try:
    
        print(index_read[preprocessWordnetLemma('andromeda')[0]]);  
    except Exception as e:
        print(type(e))
    
    
    
        
    
    
    