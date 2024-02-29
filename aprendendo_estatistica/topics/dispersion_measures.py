import streamlit as st
import plotly.graph_objects as go
from classes.equations import StatisticsEquations
from data.import_data import load_data

def page_dispersion_measures():
    
    data = load_data()
    data = data[['idade', 'tempo_para_ir_à_escola']]

    equations = StatisticsEquations()

    st.title(':two: Medidas de Dispersão')

    st.markdown('## O que são medidas de dispersão? :thinking_face:')

    st.markdown('''
                <div style="text-align: justify">
                Medidas de dispersão são estatísticas que descrevem a extensão em que os dados estão em um conjunto, podem ser distribuídos ou espalhados em torno dos valores centrais vistos no capítulo anterior. Nesse caso, elas fornecem informações sobre a variabilidade dos dados. Alguns exemplos comuns de medidas de dispersão incluem a amplitude, a variância, o desvio padrão e o intervalo interquartil. Vamos usar o mesmo dataset para exemplificar:
                <div>
                ''', unsafe_allow_html=True)
    
    st.write(data.head())
    
    st.markdown('## Amplitude')

    st.markdown('''
                <div style="text-align: justify">
                A amplitude é a diferença entre o maior e o menor valor de um conjunto de dados. Pode ser calculada da seguinte forma:
                <div>
                ''', unsafe_allow_html=True)
    
    equations.range()

    st.code('''
            # Python
            def amplitude(data):
                return data.max() - data.min()
            ''')
    
    st.write(data.max() - data.min())

    st.markdown('## Variância e Desvio Padrão')

    st.markdown('''
                <div style="text-align: justify">
                A variância é uma medida de dispersão que indica o quão distantes os valores estão da média. Já o desvio padrão é a raiz quadrada da variância, ou seja, é uma medida estatística que quantifica a dispersão ou variabilidade dos valores em um conjunto de dados. Ele indica o quanto os valores estão afastados da média também. Essas medidas podem ser calculadas da seguinte forma:
                <div>
                ''', unsafe_allow_html=True)

    equations.variance()

    equations.standard_deviation()

    st.code('''
            import pandas as pd

            # Calcular a média de cada coluna
            medias = data.mean()

            # Calcular a diferença entre cada valor e a média ao quadrado para cada coluna
            diferenca_quadrada = (data - medias) ** 2

            # Calcular a soma dos quadrados das diferenças para cada coluna
            sum_diferenca_quadrada = diferenca_quadrada.sum()

            # Calcular a variância para cada coluna
            variancia = sum_diferenca_quadrada/ len(data)

            # Calcular o desvio padrão para cada coluna (é a raiz quadrada da variância)
            desvio_padrao = variancia ** 0.5

            print("Variância de cada coluna:")
            print(variance)
            print("Desvio padrão de cada coluna:")
            print(std_deviation)

            # De forma mais simples
            variancia = data.var()
            desvio_padrao = data.std()

            variancia
            desvio_padrao

            ''')
    
    st.write('Variância:')
    variance = data.var()
    st.write(variance)

    st.write('Desvio Padrão:')
    std_deviation = data.std()
    st.write(std_deviation)

    st.markdown('## Intervalo Interquartil')

    st.markdown('''
                <div style="text-align: justify">
                O intervalo interquartil é a diferença entre o terceiro e o primeiro quartil. Mas o que é um quartil? Um quartil é um valor que divide um conjunto de dados em quatro partes iguais. O primeiro quartil (Q1) é o valor que separa o primeiro quarto dos dados, o segundo quartil (Q2) é a media e o terceiro quartil (Q3) é o valor que separa o terceiro quarto dos dados. O intervalo interquartil pode ser calculado da seguinte forma:
                <div>
                ''', unsafe_allow_html=True)

    equations.quartile_1()

    equations.quartile_3()

    equations.interquartile_range()

    st.code('''
            import pandas as pd

            # Ordene os dados em cada coluna
            df_ordenado = data.apply(sorted)

            # Calcule os índices dos quartis
            n = len(df_ordenado)
            q1_index = int(0.25 * (n + 1))
            q3_index = int(0.75 * (n + 1))

            # Calcule os quartis
            q1 = df_ordenado.iloc[q1_index - 1]
            q3 = df_ordenado.iloc[q3_index - 1]

            # Calcule o intervalo interquartil (IQR)
            iqr = q3 - q1

            print("Primeiro Quartil (Q1):", q1)
            print("Terceiro Quartil (Q3):", q3)
            print("Intervalo Interquartil (IQR):", iqr)

            # De forma mais simples
            q1 = data.quantile(0.25)
            q3 = data.quantile(0.75)
            iqr = q3 - q1

            iqr
            ''')

    st.write('Intervalo Interquartil (IQR):')
    st.write(data.quantile(0.75) - data.quantile(0.25))

