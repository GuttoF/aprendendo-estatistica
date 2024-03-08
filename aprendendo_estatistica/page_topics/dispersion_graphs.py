import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from data.import_data import load_data

# Set the style
st.set_option('deprecation.showPyplotGlobalUse', False)
sns.set(style = 'whitegrid', palette = 'tab10', color_codes = True)
color1 = sns.color_palette('tab10')[0]
color2 = sns.color_palette('tab10')[1]
color3 = sns.color_palette('tab10')[2]
color4 = sns.color_palette('tab10')[3]
color5 = sns.color_palette('tab10')[4]
color6 = sns.color_palette('tab10')[5]

hex_color1 = f'#{int(color1[0]*255):02x}{int(color1[1]*255):02x}{int(color1[2]*255):02x}'
hex_color5 = f'#{int(color5[0]*255):02x}{int(color5[1]*255):02x}{int(color5[2]*255):02x}'

def page_dispersion():
    # Data
    data = load_data()

    st.title('Gráficos de Dispersão :bar_chart:')

    st.markdown('''
                <div style="text-align: justify">
                Os gráficos de dispersão são usados para mostrar a relação entre duas variáveis. Eles são úteis para identificar padrões e correlações entre as variáveis. Lembrando, aqui, utilizaremos o banco de dados de sempre.
                <div>
                ''', unsafe_allow_html=True)


    st.markdown('## Como faço isso? :mag_right:')

    st.markdown('''
                <div style="text-align: justify">
                Para criar um gráfico de dispersão, você precisa de duas variáveis. Uma será representada no eixo x e a outra no eixo y. Vamos ver um exemplo de como criar um gráfico de dispersão usando o seaborn.
                <div>
                ''', unsafe_allow_html=True)

    dispersion_sns = sns.scatterplot(x='faltas_na_escola', y='notas_finais', data=data, color=color1)
    dispersion_sns.set_title('Gráfico de Dispersão')
    dispersion_sns.set_xlabel('Faltas na Escola')
    dispersion_sns.set_ylabel('Notas Finais')
    st.pyplot(dispersion_sns.get_figure())

    st.markdown('Usando o plotly ficaria assim:')

    dispersion_plotly = go.Figure(data=go.Scatter(x=data['faltas_na_escola'], y=data['notas_finais'], mode='markers', marker=dict(color=hex_color1)))
    dispersion_plotly.update_layout(title='Gráfico de Dispersão', xaxis_title='Faltas na Escola', yaxis_title='Notas Finais')
    st.plotly_chart(dispersion_plotly)

    st.code('''
            import sns as sns
            import plotly.graph_objects as go
            import plotly.express as px

            # Caso opte pelo plotly
            fig = go.Figure(data=go.Scatter(x=data['faltas_na_escola'], y=data['notas_finais'], mode='markers')))
            fig.update_layout(title='Gráfico de Dispersão', xaxis_title='Faltas na Escola', yaxis_title='Notas Finais')
            fig.show()

            # Caso opte pelo seaborn
            sns.scatterplot(x='faltas_na_escola', y='notas_finais', data=data)
            sns.set_title('Gráfico de Dispersão')
            sns.set_xlabel('Faltas na Escola')
            sns.set_ylabel('Notas Finais')
            fig.show()
            ''', language='python')

    st.markdown('## Gráfico bonito, mas e a interptetação? :thinking:')

    st.info('No Diagrama de Dispersão, podemos analisar se a correlação entre variáveis é forte ou fraca. Forte: quanto maior a correlação entre as variáveis, maior será a proximidade dos pontos, ou seja, estarão menos dispersos. Fraca: quanto menor a correlação entre as variáveis, mais dispersos estarão os pontos.')

    st.markdown(''''
                <div style="text-align: justify">
                No exemplo acima, podemos ver que quanto mais
				<div>
                ''', allow_unsafe_html=True)
