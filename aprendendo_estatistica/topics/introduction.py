import streamlit as st

def page_introduction():
    st.title(':chart_with_upwards_trend: Bem-vindo ao AprendendoEstatística!')

    st.markdown('''
    <div style="text-align: justify">
    A estatística é uma poderosa ferramenta que nos ajuda a coletar, analisar e interpretar dados, permitindo a tomada de decisões em diversos campos, desde a ciência até a economia. Neste aplicativo, exploraremos os conceitos fundamentais da estatística e como eles podem ser aplicados para entender melhor o mundo ao nosso redor.
    <div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
    ## O que é estatística? :mag:
    A estatística pode ser dividida em duas grandes áreas: **estatística descritiva** e **estatística inferencial**.
    - **Estatística Descritiva**: Envolve a organização, resumo e apresentação de dados de forma a facilitar a compreensão. Isso inclui o uso de gráficos, tabelas, medidas de tendência central (como média, mediana e moda) e medidas de dispersão (como variância e desvio padrão) :chart_with_upwards_trend:.
    - **Estatística Inferencial**: Permite-nos tirar conclusões e fazer previsões sobre uma população com base em uma amostra dessa população. Isso é feito através de técnicas como testes de hipóteses, intervalos de confiança e análise de regressão :crystal_ball:.

    ## Por que devo aprender? :thinking_face:
                ''')
    
    st.markdown('''
    <div style="text-align: justify">
    A estatística é essencial para entender e interpretar os dados que nos cercam. Com o crescimento exponencial de dados disponíveis, a capacidade de analisar conjuntos de dados complexos tornou-se uma habilidade valiosa em praticamente todos os setores.
    <div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
    ## Como Este Aplicativo Pode Ajudar? :rocket:
                ''')
    
    st.markdown('''
    <div style="text-align: justify">
    Este aplicativo é projetado para ser um guia interativo que introduzirá você aos conceitos básicos da estatística utilizando python. Aqui, você encontrará:
    <div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
    - **Exemplos Interativos**: Aprenda aplicando os conceitos em exemplos reais :bulb:.
    - **Visualizações de Dados**: Entenda os conceitos através de gráficos e visualizações claras :notebook:.

    Estamos entusiasmados para acompanhá-lo nesta jornada de descoberta estatística. Vamos mergulhar nos dados! :swimmer:
    ''')