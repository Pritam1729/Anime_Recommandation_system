import streamlit as st 
# from streamlit_card import card
import numpy as np
from animenames import animenames
from app import predict
import webbrowser

# def click_button():
#     st.session_state.clicked = True

def show_page() :
    
    # col1,col2 = st.columns([0.21,0.79])
    st.title("Anime Recommandation Web App")
    st.caption("NOTE : Enter the Anime that you have already watched")
    animename = st.selectbox("Anime names",animenames)
    
    
    columns = st.columns((2, 1, 2))
    
    
    ok = columns[1].button("Recommand")
    
    
    if ok:
        
        # st.session_state.clicked = False
        st.subheader("Recommanded Anime")
        recommandanime = predict(animename)
        anime = recommandanime
        # webbrowser.open(anime[0]['link'])
        # coll = st.columns()
        col11,col22 = st.columns([0.3,0.7])
        with col11:
                st.image(anime[0]['img_url'],width=300)
        with col22:
                st.subheader(anime[0]['title'])
                st.subheader(f"Rating : {anime[0]['score']}")
                st.caption(anime[0]['synopsis'])
                st.caption(f"Episodes : {anime[0]['episodes']}")
        
        col11,col22 = st.columns([0.3,0.7])
        with col11:
                st.image(anime[1]['img_url'],width=300)
        with col22:
                st.subheader(anime[1]['title'])
                st.subheader(f"Rating : {anime[1]['score']}")
                st.caption(anime[1]['synopsis'])
                st.caption(f"Episodes : {anime[1]['episodes']}")
        
        col11,col22 = st.columns([0.3,0.7])
        with col11:
                st.image(anime[2]['img_url'],width=300)
        with col22:
                st.subheader(anime[2]['title'])
                st.subheader(f"Rating : {anime[2]['score']}")
                st.caption(anime[2]['synopsis'])
                st.caption(f"Episodes : {anime[2]['episodes']}")
        
        col11,col22 = st.columns([0.3,0.7])
        with col11:
                st.image(anime[3]['img_url'],width=300)
        with col22:
                st.subheader(anime[3]['title'])
                st.subheader(f"Rating : {anime[3]['score']}")
                st.caption(anime[3]['synopsis'])
                st.caption(f"Episodes : {anime[3]['episodes']}")
                
        col11,col22 = st.columns([0.3,0.7])
        with col11:
                st.image(anime[4]['img_url'],width=300)
        with col22:
                st.subheader(anime[4]['title'])
                st.subheader(f"Rating : {anime[4]['score']}")
                st.caption(anime[4]['synopsis'])
                st.caption(f"Episodes : {anime[4]['episodes']}")
                
                
            
        col11,col22 = st.columns([0.3,0.7])
        with col11:
                st.image(anime[5]['img_url'],width=300)
        with col22:
                st.subheader(anime[5]['title'])
                st.subheader(f"Rating : {anime[5]['score']}")
                st.caption(anime[5]['synopsis'])
                st.caption(f"Episodes : {anime[5]['episodes']}")
        
            
                
                    
        
            