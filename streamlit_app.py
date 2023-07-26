import streamlit as st 
# from streamlit_card import card
import numpy as np
from animenames import animenames
from app import predict
import webbrowser

def show_page() :
    st.title("Anime Recommandation Web App")
    st.subheader("Enter the Anime that have watched before ")
    animename = st.selectbox("Anime names",animenames)
    columns = st.columns((2, 1, 2))
    ok = columns[1].button("Recommand")
    
    if ok:
        st.subheader("Recommanded Anime")
        recommandanime = predict(animename)
        # col1, col2, col3 = st.columns(3)
        # i = 0
        # ans = col1
        # for anime in recommandanime:
        #     if i == 0:
        #         ans = col1
        #     elif i == 2:
        #         ans = col2
        #     else:
        #         ans = col3
        #     i = (i+1)%3
        #     with ans:
        #         st.caption(anime['title'])
        #         st.image(anime['img_url'])
        # col1 = st.columns(1)
        for anime in recommandanime:
            
                col11,col22 = st.columns(2)
                with col11:
                    st.image(anime['img_url'])
                with col22:
                    st.title(anime['title'])
        
            