import streamlit as st
from classes.equations import StatisticsEquations
from data.import_data import load_data

def page_central_tendency():

    data = load_data()
    data = data[['idade', 'tempo_para_ir_à_escola']]

    equations = StatisticsEquations()

    st.title(':one: Medidas de Tendência Central')

    st.markdown('## Quais são essas medidas? :thinking_face:')

    st.markdown('''
                <div style="text-align: justify">
                Medidas de tendência central são medidas que representam o centro dos dados, as três fundamentais são média, mediana e moda. Vamos utilizar o mesmo dataset para exemplificar:
                <div>
                ''', unsafe_allow_html=True)
    
    st.write(data.head())
    
    st.markdown('## Média')

    st.markdown('''
                <div style="text-align: justify">
                A média é a soma de todos os valores dividido pela quantidade de valores. Pode ser definida da seguinte forma:
                <div>
                ''', unsafe_allow_html=True)
    
    equations.mean()

    st.code('''
            # Python
            import pandas as pd
            
            # Carregando arquivo csv
            data = pd.read_csv('data.csv')

            # Selecionando somente as variáveis qualitativas
            data = data[['idade', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares']]

            # Calculando a média manualmente utilizando a equação
            media = {coluna: data[coluna].sum()/len(data[coluna]) for coluna in data.columns}

            # Pode-se calcular de forma mais simples
            media = data.mean()

            media
            ''', language='python')
    
    st.write(data.mean())

    st.markdown('## Mediana')

    st.markdown('''
                <div style="text-align: justify">
                A mediana é o valor que separa a metade maior e a metade menor de uma amostra, ou seja, o valor central. Definida assim:
                <div>
                ''', unsafe_allow_html=True)
    
    equations.median()


    st.code('''
            # Python
            import pandas as pd
            
            # Carregando arquivo csv
            data = pd.read_csv('data.csv')

            # Selecionando somente as variáveis qualitativas
            data = data[['idade', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares']]

            # Calculando a mediana manualmente utilizando a equação
            def calcular_mediana(valores):
                n = len(valores)
                valores_ordenados = sorted(valores)
    
                if n % 2 == 0:
                    mediana = (valores_ordenados[n//2 - 1] + valores_ordenados[n//2]) / 2
                else:
                    mediana = valores_ordenados[n//2]
    
                return mediana

            mediana = {coluna: calcular_mediana(df[coluna]) for coluna in df.columns}

            # Pode-se calcular de forma mais simples
            mediana = data.median()

            mediana
            ''', language='python')
    
    st.write(data.median())

    st.markdown('## Moda')

    st.markdown('''
                <div style="text-align: justify">
                A moda é o valor que mais se repete na amostra. Simples assim:
                <div>
                ''', unsafe_allow_html=True)
    
    equations.mode()

    st.code('''
            import pandas as pd
            
            # Carregando arquivo csv
            data = pd.read_csv('data.csv')

            # Selecionando somente as variáveis qualitativas
            data = data[['idade', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares']]

            # Calculando a moda manualmente
            def calcular_moda(valores):
                contagem = Counter(valores)
                maxima_frequencia = max(contagem.values())
                modas = [val for val, freq in contagem.items() if freq == maxima_frequencia]
    
                # Retornar todos os valores de moda se houver mais de um, ou apenas um valor se for o único
                if len(modas) == 1:
                    return modas[0]
                else:
                    return modas

            moda = {coluna: calcular_moda(df[coluna]) for coluna in df.columns}

            # Pode-se calcular de forma mais simples
            moda = data.mode()

            moda
            ''', language='python')
    
    st.write(data.mode())
