import streamlit as st
from data.import_data import load_data

def page_features():

    data = load_data()
    data = data[['escola', 'idade', 'motivo_para_escolher_escola', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares']]
    
    st.title(':1234: Variáveis e suas características :mag_right:')

    st.markdown('## O que são variáveis? :thinking_face:')

    st.markdown('''
                <div style="text-align: justify">
                <b>Variáveis</b> (Features) são características que descrevem os dados na sua população ou amostra :books:.
                <div>
                ''', unsafe_allow_html=True)
    
    st.info('População em estatística não é sinônimo de população em demografia, ou seja, não precisam ser pessoas, podem ser objetos, eventos ou situações também :earth_americas:.')

    st.markdown('''
                <div style="text-align: justify">
                Nesse contexto, iremos utilizar o seguinte banco de dados:
                <div>
                ''', unsafe_allow_html=True)
    
    
    st.write(data.head().T)

    st.markdown('## Tipos de variáveis :abacus:')

    st.markdown('''
                <div style="text-align: justify">
                Variáveis podem ser de dois tipos:
                <div>
                ''', unsafe_allow_html=True)

    st.markdown('''
                - **Quantitativas**: São aquelas que representam valores numéricos :1234:.
                    - Exemplos: idade, tempo para ir à escola.
                
                - **Qualitativas**: São aquelas que representam categorias :label:.
                    - Exemplos: motivo para escolher escola, qualidade das relações familiares.
                
                Vamos ver um exemplo em python?
                ''')
    
    st.code('''
            import pandas as pd
            
            # Carregando arquivo csv
            data = pd.read_csv('data.csv')

            # Selecionando somente varáveis qualitativas
            qualitativas = data.select_dtypes(include='object')

            # Selecionando somente varáveis quantitativas
            quantitativas = data.select_dtypes(exclude='object')

            # Pode-se utilizar também a seleção de colunas manualmente
            quantitativas = data[['idade', 'tempo_para_ir_à_escola']]
            qualitativas = data[['motivo_para_escolher_escola', 'qualidade_das_relações_familiares']]
            
            ''', language='python')
    
    st.info('Variáveis qualitativas podem ser representadas por números, como por exemplo a variável ***qualidade das relações familiares***. Nesse caso, a variável é qualitativa, pois os números representam uma hierarquia :arrow_up_down:.')

    st.markdown('## Classificação dos tipos :file_folder:')

    st.markdown('''
                <div style="text-align: justify">
                Dentre os dois tipos de variáveis, ainda podemos classificá-las em:
                <div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
                - **Quantitativas Discretas**: Valores específicos e contáveis :counting:.
                    - Exemplo: idade;

                - **Quantitativas Contínua**: Possuem uma infinidade de possíveis valores dentro de um intervalo :infinity:.
                    - Exemplo: tempo para ir à escola.
                
                - **Qualitativas Ordinais**: Existe uma ordem ou hierarquia nos valores :chart_with_upwards_trend:.
                    - Exemplo: qualidade das relações familiares.
                
                - **Qualitativas Nominais**: Não possuem uma ordem :no_entry_sign:.
                    - Exemplo: motivo para escolher escola.
                ''')

