import streamlit as st
from page_topics.learning_features import page_features
from page_topics.introduction import page_introduction
from page_topics.central_tendency import page_central_tendency
from page_topics.dispersion_measures import page_dispersion_measures
from page_topics.graphs import page_graphs, page_graphs_1
from page_topics.dispersion_graphs import page_dispersion

# Page config
st.set_page_config(page_title='Aprendendo Estatística',
                   page_icon=':bar_chart:',
                   layout='wide',
                   initial_sidebar_state='auto')


def main():

    st.sidebar.title(':bar_chart: Tópicos')
    selected_page = st.sidebar.selectbox('Selecione um tema', ['Início', 'Variáveis', 'Medidas de Tendência Central', 'Medidas de Dispersão', 'Gráficos estatísticos', 'Histogramas e Boxplots', 'Gráficos de Dispersão'])

    if selected_page == 'Início':
        page_introduction()
    elif selected_page == 'Variáveis':
        page_features()
    elif selected_page == 'Medidas de Tendência Central':
        page_central_tendency()
    elif selected_page == 'Medidas de Dispersão':
        page_dispersion_measures()
    elif selected_page == 'Gráficos estatísticos':
        page_graphs()
    elif selected_page == 'Histogramas e Boxplots':
        page_graphs_1()
    elif selected_page == 'Gráficos de Dispersão':
        page_dispersion()

if __name__ == "__main__":
    main()
