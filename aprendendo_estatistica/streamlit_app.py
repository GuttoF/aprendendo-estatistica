import pandas as pd
import streamlit as st
from topics.learning_features import page_features
from topics.introduction import page_introduction
from topics.central_tendency import page_central_tendency
from topics.dispersion_measures import page_dispersion_measures
from topics.graphs import page_graphs

# Page config
st.set_page_config(page_title='Aprendendo Estatística', page_icon=':bar_chart:', layout='wide', initial_sidebar_state='auto')

def main():
    st.sidebar.title(':bar_chart: Tópicos')
    selected_page = st.sidebar.selectbox('Selecione um tema', ['Início', 'Variáveis', 'Medidas de Tendência Central', 'Medidas de Dispersão', 'Gráficos'])

    if selected_page == 'Início':
        page_introduction()
    elif selected_page == 'Variáveis':
        page_features()
    elif selected_page == 'Medidas de Tendência Central':
        page_central_tendency()
    elif selected_page == 'Medidas de Dispersão':
        page_dispersion_measures()
    elif selected_page == 'Gráficos':
        page_graphs()

if __name__ == "__main__":
    main()



    
    
    
    
    
    
    
    
    
    
    
    