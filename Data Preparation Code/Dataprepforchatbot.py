# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:26:28 2021

@author: Naveen
"""
pip install xlrd
import pandas as pd
import spacy
import random
import re

nlp = spacy.load('en_core_web_md')

def get_sentence_vectors(text, nlp):
    
    # get tokens for each word in sentence
    embedding = nlp(text).vector.tolist()
    
    # return mean token
    return embedding

illness_df = pd.read_excel(r'C:/Users/Naveen/Downloads/dia_t.xlsx')
symptom_df = pd.read_excel('C:/Users/Naveen/Downloads/sym_t.xlsx')
links_df = pd.read_excel('C:/Users/Naveen/Downloads/diffsydiw.xlsx')


source_data = (links_df
               .merge(illness_df, on="did")
               .merge(symptom_df, on="syd"))

source_data = source_data.loc[~(source_data['symptom'].isna())
                             & ~(source_data['diagnose'].isna()),
                             ['did', 'syd', 'diagnose', 'symptom']]
source_data.columns = ['illness_id', 'symptom_id', 'illness', 'symptom']

source_data['illness'] = source_data['illness'].str.replace('\x0b', ' ')
source_data['symptom'] = source_data['symptom'].str.replace('\x0b', ' ')

symptom_df = symptom_df.loc[~symptom_df['symptom'].isna()]
symptom_df['embedding'] = symptom_df.apply(lambda row: get_sentence_vectors(row['symptom'], nlp), axis = 1)
symptom_df.columns = ['symptom_id', 'symptom', 'symptom_vector']

# remove any messy characters
symptom_df['symptom'] = symptom_df['symptom'].str.replace('\x0b', ' ')

source_data.to_pickle('C:/Users/Naveen/Downloads/source_data.pkl')
symptom_df.to_pickle('C:/Users/Naveen/Downloads/symptoms.pkl')

# ist of illness
illnesses = list(source_data['illness'].drop_duplicates())

# list we will use to store our illness vectors
symptom_vectors = []

for illness in illnesses:
    
    illness_symptoms = list(source_data.loc[source_data["illness"]==illness, 'symptom'].drop_duplicates())
    
    symptom_df["related_to_illness"] = 0
    symptom_df.loc[symptom_df["symptom"].isin(illness_symptoms), "related_to_illness"] = 1
    
    
    symptom_vectors.append(list(symptom_df["related_to_illness"]))
    
diagnosis_data = pd.DataFrame({"illness":illnesses,
                              "illness_vector": symptom_vectors})


diagnosis_data.to_pickle('C:/Users/Naveen/Downloads/diagnosis_data.pkl')



number_of_symptoms = [1, 2, 3, 4]
start_of_description = [
    "I have",
    "I'm suffering from",
    "I have really bad",
    "My symptoms are",
    "For the last few days I have had",
    "My husband is suffering from" ,
    "My wife is suffering from",
    "My son is suffering from",
    "My daughter is suffering from",
    "My child is suffering from",
    "I don't feel well, I have"
]

# get some examples of users describing different numbers of syptoms
for symptons_count in number_of_symptoms:
    
    # make 100 examples of each number of symptoms
    for ex in range(1, 101):
    
        description_beginning = random.choice(start_of_description)
        
        # collect some random symtpoms
        symptom_1 = symptom_df['symptom'].sample(1).iloc[0].lower()
        symptom_2 = symptom_df['symptom'].sample(1).iloc[0].lower()
        symptom_3 = symptom_df['symptom'].sample(1).iloc[0].lower()
        symptom_4 = symptom_df['symptom'].sample(1).iloc[0].lower()
        
        symptoms = [symptom_1, symptom_2, symptom_3, symptom_4]
        symptoms_entity = []
        
        # remove parenthases from symptoms and add nessecary entitiy tags to symptoms
        for symptom in symptoms:
            symptom = re.sub(r"\([^)]+\)", "", symptom).strip()
            symptom = f"[{symptom}](symptom)"
            symptoms_entity.append(symptom)
            
        symptom_1 = symptoms_entity[0]
        symptom_2 = symptoms_entity[1]
        symptom_3 = symptoms_entity[2]
        symptom_4 = symptoms_entity[3]
        
        # create the training sample string
        if symptons_count == 1:
            
            symptom_string = f"- {description_beginning} {symptom_1}"
            
        if symptons_count == 2:
            
            symptom_string = f"- {description_beginning} {symptom_1} and {symptom_2}"
            
        if symptons_count == 3:
            
            symptom_string = f"- {description_beginning} {symptom_1}, {symptom_2}, and {symptom_3}"
            
        if symptons_count == 4:
            
            symptom_string = f"- {description_beginning} {symptom_1}, {symptom_2}, {symptom_3}, {symptom_4}"
        
        print(symptom_string)
