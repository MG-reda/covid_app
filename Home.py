#main streamlit

import streamlit as st
st.title('covid-19 data analysis')
st.markdown('''this app is created to analiyze the cofid-19 data''')
with st.container():
    col1,col2=st.columns(2)
    with col1:
        st.markdown('''#''')
        st.markdown('''covid dfhdfi dash bord''')
    with col2:
        #image
        st.image('https://images.app.goo.gl/8P39XpArtmGDe6gx5',width=100)

        

#description 
st.header('Description')
st.markdown('''this app is created to analyze the covid-19 data''')

