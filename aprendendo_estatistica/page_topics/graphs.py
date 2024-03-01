import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import mode
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


# Data

data = load_data()

data = data[['escola', 'idade', 'motivo_para_escolher_escola', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares', 'notas_do_primeiro_período', 'notas_do_segundo_período']]

def measure_mode(lista, num_bins = 30):
    bins = np.linspace(min(lista), max(lista), num_bins)
    digitized = np.digitize(lista, bins)

    mode_bin = mode(digitized)[0]
    mode_diff = (bins[mode_bin - 1], bins[mode_bin])

    return (mode_diff[0] + mode_diff[1])/2


def plot_data(data, title, num_bins = 30):
    mean = np.mean(data)
    median = np.median(data)
    mode = measure_mode(data, num_bins = num_bins)

    plt.figure(figsize=(12, 6))

    # Histogram
    plt.subplot(1, 2, 1)
    
    # Plot histogram
    sns.histplot(data, kde = True, color = color1, bins = num_bins, edgecolor = 'black')
    
    # Plot mean, median and mode
    plt.axvline(mean, color=color2, linestyle='dashed', linewidth=2, label=f'Média: {mean:.2f}')
    plt.axvline(median, color=color3, linestyle='dashed', linewidth=2, label=f'Mediana: {median:.2f}')
    plt.axvline(mode, color=color4, linestyle='dashed', linewidth=2, label=f'Moda: {mode:.2f}')
    plt.legend()
    
    plt.title(f'Histograma - {title}')
    plt.xlabel('Valores')
    plt.ylabel('Frequência')

    # Boxplot
    plt.subplot(1, 2, 2)
    
    # Plot boxplot
    sns.boxplot(x = data, color = color5)
    
    # Plot mean and median
    plt.axvline(mean, color=color2, linestyle='dashed', linewidth=2, label=f'Média: {mean:.2f}')
    plt.axvline(median, color=color3, linestyle='dashed', linewidth=2, label=f'Mediana: {median:.2f}')
    plt.legend()
    
    plt.title(f'Boxplot - {title}')
    plt.xlabel('Valores')


def plot_seaborn(data, feature = 'idade'):

    # Plot histogram and boxplot 
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    # Acess subplots
    ax1 = axes[0]
    ax2 = axes[1]

    fig.suptitle(f'Histograma e Boxplot da {feature}', fontsize=16)
    sns.histplot(data[feature], kde=True, color=color1, ax=ax1)

    ax1.set_title(f'Histograma da {feature}')
    ax1.set_xlabel('Idade')
    ax1.set_ylabel('Frequência')

    sns.boxplot(x=data[feature], color=color5, ax=ax2)
    
    ax2.set_title(f'Boxplot da {feature}')
    ax2.set_xlabel('Idade')


def plot_plotly(data, feature='idade'):
    # Histogram
    fig_hist = px.histogram(data, x=feature, nbins=20, marginal='rug', color_discrete_sequence=[hex_color1])
    fig_hist.update_layout(title=f'Histograma da {feature}',
                           xaxis_title='Idade',
                           yaxis_title='Frequência')

    # Boxplot
    fig_box = px.box(data, y=feature, color_discrete_sequence=[hex_color5])
    fig_box.update_layout(title=f'Boxplot da {feature}')

    # Show both plots
    st.plotly_chart(fig_hist, use_container_width=True)
    st.plotly_chart(fig_box, use_container_width=True)

def page_graphs():
    st.title(':three: Gráficos estatísticos')
    
    st.markdown('## Quais são os gráficos estatísticos mais importantes? :thinking_face:')

    st.markdown('''
                <div style="text-align: justify">
                <ul>
                Na estatística, alguns dos gráficos mais importantes incluem:

                <li><b>Histograma</b>: Mostra a distribuição de uma variável contínua através de barras. É útil para entender a forma da distribuição, presença de outliers e características importantes dos dados.</li>

                <li><b>Gráfico de Barras</b>: Representa a distribuição de uma variável categórica através de barras. É útil para comparar a frequência ou proporção de diferentes categorias. Histograma é um gráfico de barras</li>

                <li><b>Gráfico de Dispersão</b>: Mostra a relação entre duas variáveis quantitativas. É útil para identificar padrões, tendências e relações entre as variáveis.</li>

                <li><b>Boxplot (Diagrama de Caixa)</b>: Exibe a distribuição de uma variável e destaca os quartis, a mediana e os outliers. É útil para identificar a dispersão dos dados, a presença de outliers e comparar distribuições entre grupos.</li>

                <li><b>Gráfico de Linha</b>: Usado para representar mudanças em uma variável ao longo do tempo ou em relação a outra variável contínua. É comumente usado em séries temporais e análises de tendência.</li>

                <li><b>Gráfico de Pizza</b>: Mostra a distribuição de uma variável categórica em termos de proporções de um todo. É útil para visualizar a composição de um conjunto de dados.</li>
                </ul>

                Existem vários outros mas esses são os mais importantes e mais vistos atualmente.
                <div>
                ''', unsafe_allow_html=True)
    
    st.info('Atualmente, o gráfico de pizza está sendo questionado pelo mercado e caindo em desuso, pois é difícil comparar proporções em um círculo. O gráfico de barras é uma alternativa mais eficaz.')
    
    st.markdown('## Como faço isso em python? :snake:')

    st.markdown('''
                <div style="text-align: justify">
                Existem algumas bibliotecas importantes para a criação de gráficos em python, como <b>matplotlib</b>, <b>seaborn</b> e </plotly>. O seaborn é uma biblioteca de visualização de dados baseada no matplotlib que fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos. O plotly é uma biblioteca de visualização de dados interativa que permite criar gráficos interativos e personalizáveis. Aqui iremos fazer exemplos com os dois.
                <div>
                ''', unsafe_allow_html=True)



def page_graphs_1():
    

    
    st.title('Histogramas e Boxplots :bar_chart:')

    st.markdown('''
                <div style="text-align: justify">
                Nesta aula, exploraremos dois tipos de representações gráficas em estatística: Histogramas e Boxplots. Ambos são ferramentas essenciais para visualizar a distribuição e dispersão dos dados.
                <div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
                O histograma é um gráfico de barras que representa a distribuição de frequência de um conjunto de dados. Detalhes do Histograma:

                - **Barras**: Cada barra representa a frequência de um intervalo de valores (chamado de "bin"). A altura da barra indica a quantidade de dados nesse intervalo.
                - **Largura da Barra**: A largura pode variar, mas geralmente é constante, representand o intervalos iguais.
                - **Assimetria**: A forma do histograma pode mostrar a assimetria da distribuição. Uma cauda mais longa à direita indica assimetria positiva e à esquerda, negativa.
                - **Posição da Média, Mediana e Moda**: Em um histograma simétrico, média, mediana e moda estão no centro. Em histogramas assimétricos, suas posições variam.
                - **Distribuição Bimodal**: Se houver dois picos, a distribuição é bimodal, indicando possivelmente duas populações diferentes nos dados.
                ''')

                
    st.markdown('''
                <div style="text-align: justify">
                Já o boxplot, ou gráfico de caixa, é uma representação gráfica que mostra a distribuição de dados quantitativos e facilita a identificação de outliers. Detalhes do Boxplot:
                <div>
                ''', unsafe_allow_html=True)
    
    st.markdown('''
                - **Quartis**: Divide os dados em quartis. O "box" (caixa) representa o intervalo interquartil (IQR), do primeiro ao terceiro quartil.
                - **IQR (Intervalo Interquartil)**: Mede a dispersão dos dados e é a diferença entre o terceiro e o primeiro quartil.
                - **Mediana**: Representada por uma linha dentro do box, indica o valor mediano dos dados. 
                - **Whiskers (Bigodes)**: Linhas que se estendem do box até os valores máximo e mínimo, exceto outliers.
                - **Outliers**: Pontos fora dos whiskers, indicam valores anormalmente altos ou baixos.
                ''')
    
    st.markdown('Aqui utilizaremos dados diferentes para explicar alguns conceitos importantes. Vamos lá?') 


    st.code('''
            import numpy as np

            # Gerando dados de exemplo para diferentes tipos de distribuições
            np.random.seed(42)

            # Dados para uma distribuição simétrica
            symmetric_data = np.random.normal(100, 15, 10000)

            # Dados para uma distribuição assimétrica negativa (com viés para esquerda)
            positive_skew_data = np.random.exponential(scale=50, size=10000)

            # Dados para uma distribuição assimétrica positiva (com viés para direita)
            negative_skew_data = [k+310 if k < 50 else k+200 if k < 100 else k + 100 if k < 150 else 350 if k > 400 else k for k in np.random.exponential(scale=50, size=10000)]
            ''', language='python')


    np.random.seed(42)

    st.markdown('## Distribuição Simétrica')

    st.markdown('''
                <div style="text-align: justify">
                Em uma distribuição simétrica, os dados são distribuídos de forma uniforme em torno da média, de modo que a metade esquerda do histograma é aproximadamente um espelho da metade direita. Isso significa que a média, mediana e moda estão todas centralizadas no mesmo ponto. Um exemplo comum de uma distribuição simétrica é a distribuição normal (ou gaussiana).
                <div>
                ''', unsafe_allow_html=True)
    
    symmetric_data = np.random.normal(100, 15, 10000)
    symmetric_plot = plot_data(symmetric_data, "Distribuição Simétrica")
    st.pyplot(symmetric_plot)

    st.markdown('## Distribuição Assimétrica Negativa')

    st.markdown('''
                <div style="text-align: justify">
                Em uma distribuição com skewness negativa, a cauda da distribuição estende-se mais para a esquerda, em direção aos valores menores, enquanto a maioria dos dados está concentrada na parte direita do histograma. Isso significa que a média é menor do que a mediana, e a cauda mais longa está do lado esquerdo. Um exemplo comum de uma distribuição com skewness negativa é a distribuição gama com parâmetro de forma (shape parameter) menor que 1.
                <div>
                ''', unsafe_allow_html=True)


    negative_skew_data = [k+310 if k < 50 else k+200 if k < 100 else k + 100 if k < 150 else 350 if k > 400 else k for k in np.random.exponential(scale=50, size=10000)]
    negative_skew_plot = plot_data(negative_skew_data, "Distribuição Assimétrica Negativa")
    st.pyplot(negative_skew_plot)

    st.markdown('## Distribuição Assimétrica Positiva')

    st.markdown('''
                <div style="text-align: justify">
                Em uma distribuição com skewness positiva, a cauda da distribuição estende-se mais para a direita, em direção aos valores maiores, enquanto a maioria dos dados está concentrada na parte esquerda do histograma. Isso significa que a média é maior do que a mediana, e a cauda mais longa está do lado direito. Um exemplo comum de uma distribuição com skewness positiva é a distribuição de salários, onde há um pequeno número de pessoas com salários muito altos, enquanto a maioria dos salários está concentrada na faixa mais baixa.
                <div>
                ''', unsafe_allow_html=True)


    positive_skew_data = np.random.exponential(scale=50, size=10000)
    positive_skew_plot = plot_data(positive_skew_data, "Distribuição Assimétrica Positiva")
    st.pyplot(positive_skew_plot)

    st.markdown('## Seaborn')

    st.markdown('''
                <div style="text-align: justify">
                O seaborn é uma biblioteca de visualização de dados baseada no matplotlib que fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos. Ele fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos. Aqui, utilizaremos o banco de dados de sempre:
                <div>
                ''', unsafe_allow_html=True)
    
    st.code('''
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            # Carregando arquivo csv
            data = pd.read_csv('data.csv')

            # Selecionando somente as variáveis quantitativas
            data = data[['escola', 'idade', 'motivo_para_escolher_escola', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares', 'notas_do_primeiro_período', 'notas_do_segundo_período']]

            # Plotando histograma e boxplot com subplots
            # O subplots é para plotar os dois gráficos lado a lado, o primeiro argumento são a quantidade de linhas já o segundo as colunas.
            fig, axes = plt.subplots(1, 2, figsize=(12, 6))

            # Acessando os subplots por eixo
            ax1 = axes[0]
            ax2 = axes[1]

            # Título do gráfico completo
            fig.suptitle('Histograma e Boxplot da idade', fontsize=16)
            
            # Quando setamos o kde=True, o gráfico exibirá a densidade de probabilidade também, com False, apenas o histograma.
            sns.histplot(data['idade'], kde=True, ax=ax1)


            # Aqui podemos definir o título, nome no eixo X e no eixo Y
            ax1.set_title(f'Histograma da idade')
            ax1.set_xlabel('Idade')
            ax1.set_ylabel('Frequência')

            sns.boxplot(x=data['idade'], color=color5, ax=ax2)

            ax2.set_title(f'Boxplot da idade')
            ax2.set_xlabel('Idade')
            ''', language='python')
    
    seaborn_plot = plot_seaborn(data)
    st.pyplot(seaborn_plot)

    st.info('Sabendo da teoria, esse gráfico é assimétrico positivo, negativo ou simétrico?')
    st.info('Observe que o ponto no boxplot é um outlier, ou seja, um valor que está fora do intervalo interquartil.')

    st.markdown('## Plotly')

    st.markdown('''
                <div style="text-align: justify">
                O plotly é uma biblioteca de visualização de dados interativa que permite criar gráficos interativos e personalizáveis. Aqui, utilizaremos o banco de dados de sempre:
                <div>
                ''', unsafe_allow_html=True)
    
    st.code('''
            import pandas as pd
            import plotly.express as px

            # Carregando arquivo csv
            data = pd.read_csv('data.csv')

            # Selecionando somente as variáveis quantitativas
            data = data[['escola', 'idade', 'motivo_para_escolher_escola', 'tempo_para_ir_à_escola', 'qualidade_das_relações_familiares', 'notas_do_primeiro_período', 'notas_do_segundo_período']]


            # Histograma da mesma forma que o seaborn
            # marginal='rug' adiciona uma linha para cada ponto no eixo X
            fig_hist = px.histogram(data, x='idade', marginal='rug')
            fig_hist.update_layout(title='Histograma da idade',
                                   xaxis_title='Idade',
                                   yaxis_title='Frequência')

            # Boxplot da mesma forma que o seaborn também
            fig_box = px.box(data, y='idade')
            fig_box.update_layout(title='Boxplot da idade')

            # Mostrar os plots, diferente do seaborn, eles aparecem individualmente
            fig_hist.show()
            fig_box.show()
            ''', language='python')
    
    plot_plotly(data)




def page_graphs_2():
    pass
