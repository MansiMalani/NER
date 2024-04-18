import streamlit as st
import spacy 
from spacy import displacy
import en_core_web_sm
nlp= en_core_web_sm.load()
from pprint import pprint
from newspaper import Article



st.title ("Page for NER")
u= st.text_input("Please enter your URL")
p= st.text_area("If you want to enter your paragraph")
if st.button("Submit4NER"):
    if (u):
        article= Article(u)
        article.download()
        article.parse()
        doc= nlp(article.txt)
        ent_html= displacy.render(doc,jupyter= False,style= 'ent')
        st.markdown(ent_html,unsafe_allow_html=True)
    else:
        doc= nlp(p)
        ent_html= displacy.render(doc,jupyter= False,style= 'ent')
        st.markdown(ent_html,unsafe_allow_html=True)
