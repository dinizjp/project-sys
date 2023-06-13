import pandas as pd 
import streamlit as st
from PIL import Image 
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
        page_title= 'Análise das Médias',
        page_icon='📊',
       layout="wide")


image = Image.open('sys.png')
st.sidebar.image(image, use_column_width='auto')

st.sidebar.markdown('''---''')
st.sidebar.markdown('### Powered by Diniz JP')


#---------------------------------------------##---------------------------------------------#

def adicionar_anotacoes(fig, df, x_column, y_column, text_list):
    for i, text in enumerate(text_list):
        x = df.sort_values(y_column, ascending=False).iloc[i][x_column]
        y = df.sort_values(y_column, ascending=False).iloc[i][y_column]
        fig.add_annotation(x=x, y=y, text=text, showarrow=True, font=dict(size=8, color='black'), arrowsize=0.3)


#---------------------------------------------##---------------------------------------------#


df = pd.read_csv('/Users/dinizjp/Programação /Projetos /Projeto SYS/dados_publicacoes/Dashboard/dados_tratados.csv', sep=',')


tab1, tab2, tab3 = st.tabs( ['Correlação, Média e Desvio Padrão', 'Análise de posts', 'Dispersão por métrica'])

#---------------------------------------------##---------------------------------------------#


with tab1:   
    
    with st.container():

        st.markdown('#### Correlação entre as métricas')
        st.markdown('###### Quanto mais próximo o valor estiver de 1, maior é a correlação entre as duas váriaveis')

        st.markdown(''' A correlação entre **Alcance e Curtidas é de 0.87**. Isso significa que, em geral, quanto maior o alcance de uma postagem, maior é o número de curtidas recebidas.

A correlação entre **Curtidas e Compartilhamento é de 0.83**. Isso significa que postagens que recebem um alto número de curtidas tendem a ser mais compartilhadas pelos usuário.

A correlação entre **Alcance e Impressões é praticamente perfeita, com um valor de 0.98**. Isso indica que essas métricas estão altamente relacionadas, ou seja, quanto maior o alcance de uma postagem, maior é o número de vezes que ela é exibida
        ''')


        df1 = df[['impressões','alcance','compartilhamentos','seguimentos','curtidas','comentários','salvamentos']].corr().round(2)

        # Exibir o DataFrame estilizado no Streamlit
        st.dataframe(df1, width=1200)

        st.divider()


#---------------------------------------------##---------------------------------------------#
        st.markdown('#### Média e Desvio Padrão das principais métricas')

        st.markdown('O fato de todas as métricas apresentarem um desvio padrão alto indica que há uma variação alta no engajamento dos seguidores. Isso implica que algumas postagens têm um bom desempenho, enquanto outras têm um desempenho abaixo da média.')

        col1, col2, col3, col4, col5, col6 = st.columns(6)


        col1.metric("Média Alcance", "19.082")
        col1.metric("Desvio Padrão", '± 12.589' )


        col2.metric("Média Impressões", "23.252")
        col2.metric("Desvio Padrão", '± 15.771' )


        col3.metric("Média Curtidas", "1.268")
        col3.metric("Desvio Padrão", '± 1.253' )


        col4.metric("Média Compartilhamento", "367")
        col4.metric("Desvio Padrão", '± 640' )


        col5.metric("Média Coméntarios", "19")
        col5.metric("Desvio Padrão",'± 55.43' )


        col6.metric("Média Salvamentos", "186")
        col6.metric("Desvio Padrão", '± 303' )


#---------------------------------------------##---------------------------------------------#

        st.divider()



        df_aux = df[['tipo_de_publicação', 'alcance']].groupby('tipo_de_publicação').agg({'alcance':['mean','std']}).round()

        df_aux.columns = ['alcance médio', 'Desvio padrão']

        df_aux = df_aux.reset_index()


        fig = go.Figure()

        fig.add_trace(go.Bar(
            name='Control',
            x=df_aux['tipo_de_publicação'],
            y=df_aux['alcance médio'],
            error_y=dict(type='data', array=df_aux['Desvio padrão']),
            marker=dict(color=['#ED618C', '#B5385E','#A8123E'])  
        ))

        fig.update_layout(
            barmode='group',
            width=1000,
            height=600,
            yaxis_title='Alcance médio',
            xaxis_title='Tipo de publicação'
        )

        st.markdown('### Média de Alcance por tipo de post')
        st.markdown('O **Desvio padrão** (Barra preta no centro do gráfico) está muito alto, isso indica que os dados têm uma grande variabilidade. Em termos práticos, um alto desvio padrão sugere que os valores individuais estão mais espalhados e menos previsíveis, o que dificulta indentificar padrões replicáveis ')

        st.plotly_chart(fig)


#---------------------------------------------##---------------------------------------------#

with tab2: 
    
    with st.container():
        
        
        
#---------------------------------------------##---------------------------------------------#
       #plot 1 - 20 melhores em alcance  
    
    
        st.markdown('## Os 20 melhores post por Alcance')
        st.markdown('Em relação ao Alcance, não foi identificado nenhum padrão constante com o formato ou tema dos posts. Isso indica que o alcance das postagens de melhor desempenho não está fortemente ligado a características específicas, mas pode ser uma combinação de Tema/Timing')
        
        cores = ['#ED618C', '#A8123E', '#FFCFC2']


        fig = px.scatter(df.sort_values('alcance', ascending=False).head(20),
                         x='data',
                         y='alcance',
                         width=1100,
                         height=700,
                         color='tipo_de_publicação',
                         color_discrete_sequence=cores)




        fig.update_traces(mode='markers', marker=dict(size=12))


        textos = ['Post Guia Astro Tesao', 'Polêmica Daniel Alves', 'Tipos de Sexo', 'Carrossel Twitter', 'Post Frase Safada',
                  'Amiga sofrendo por macho', 'Colab VenusEmLeao', 'Monte seu nome de Gostosa', '3 posições para dar em pé',
                  'Carrossel Twitter', 'Ajuda para chegar no boy', '4 tecnicas para chupada fatal', 'Comentarios Grupo Facebook',
                  'Publi Feel Lub', 'Cansada de papai e mamãe?', 'Tesão Bloquinho', 'Colab Hellomeyfe', 'Insegura no Uber Audio',
                  'Polêmica Juíza', 'Vale Calcinha, vem retirar']


        adicionar_anotacoes(fig, df, 'data', 'alcance', textos)


        st.plotly_chart(fig)
        
        
#---------------------------------------------##---------------------------------------------#
    #plot 2 - 20 melhores por curtida   
        
        cores = ['#ED618C', '#A8123E', '#FFCFC2']

        fig = px.scatter(df.sort_values('curtidas', ascending=False).head(20),
                         x='data',
                         y='curtidas',
                         width=1100,
                         height=700,
                         color='tipo_de_publicação',
                         color_discrete_sequence=cores)

        fig.update_traces(mode='markers', marker=dict(size=12))

        textos = ['Carrossel Twitter','Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Twitter', 'Cansada de papai e mamãe?','Polêmica Juíza', 
                  'Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Twitter','Carrossel Twitter', '3 posições para dar em pé',
                  'Post Frase Safada', 'Carrossel Twitter', 'Camisa 24 seleção', 'Meme Luiza Sonza', '4 tecnicas para chupada fatal','Carrossel Twitter',
                  'Colab VenusEmLeao', 'Carrossel Twitter']

        adicionar_anotacoes(fig, df, 'data', 'curtidas', textos)
        
        st.markdown('## Os 20 melhores post por Curtida')
        st.markdown('Em relação às curtidas e compartilhamentos, foi observado que 12 dos 20 melhores posts têm o formato de carrossel Twitter. Isso sugere que esse formato tem uma tendência a gerar um maior envolvimento dos usuários, levando a mais curtidas e compartilhamentos.')
        
        st.plotly_chart(fig)
        
#---------------------------------------------##---------------------------------------------#
        
        
        cores = ['#ED618C', '#A8123E', '#FFCFC2']


        fig = px.scatter(df.sort_values('compartilhamentos', ascending=False).head(20),
                         x='data',
                         y='compartilhamentos',
                         width=1100,
                         height=700,
                         color='tipo_de_publicação',
                         color_discrete_sequence=cores)

        fig.update_traces(mode='markers', marker=dict(size=12))


        textos = ['Carrossel Twitter','Carrossel Twitter', 'Polêmica Juíza', 'Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Dia do Beijo', 
                  'Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Twitter', 'Carrossel Twitter','Carrossel Twitter', 
                  'Monte seu nome de Gostosa', 'Dia do Sexo', 'Carrossel Twitter', 'Carrossel Twitter', 'Camisa 24 seleção','Post Frase Safada',
                  '3 posições para dar em pé','Comentarios Grupo Facebook2']


        adicionar_anotacoes(fig, df, 'data', 'compartilhamentos', textos)
        
        st.markdown('## Os 20 melhores post por Compartilhamento')
        st.markdown('Além de 12 posts em formato de carrossel, outros 3 posts que apareceram nos melhores em curtidas e compartilhamento, são eles: Post Frase Safada, Polêmica Juíza e 3 Posições para dar em pé')
        
        st.plotly_chart(fig)
        
#---------------------------------------------##---------------------------------------------#
        
        st.divider()
        
        st.markdown('### Vocês podem encontrar o link dos post em ordem descrecente do maior para o menor aqui nessas tabelas')
        
        
        
        st.markdown('##### Os 20 melhores post por Alcance')
        
        st.dataframe(df[['link_permanente', 'alcance','data']].sort_values('alcance', ascending=False).head(20), width=1000, height=738)
        
        
        st.markdown('##### Os 20 melhores post por Curtidas')
        
        st.dataframe(df[['link_permanente', 'curtidas','data']].sort_values('curtidas', ascending=False).head(20), width=1000, height=738)
        
        
        st.markdown('##### Os 20 melhores post por Compartilhamentos')
        
        st.dataframe(df[['link_permanente', 'compartilhamentos','data']].sort_values('compartilhamentos', ascending=False).head(20), width=1000, height=738)
        
#---------------------------------------------##---------------------------------------------#
        

with tab3:   
    
    with st.container():
        
        st.markdown('## Gráficos de dispersão das 3 principais métricas: Alcance, Curtidas, Compartilhamentos.')
        st.markdown('#### Uma visão geral de como os posts estão dispersos por métrica ao longo de 1 ano.')        
        st.divider()
        
        color_map = {
            'Carrossel do Instagram': '#ED618C',
            'Imagem do Instagram': '#FFCFC2',
            'Vídeo do Instagram': '#A8123E'}

        fig = go.Figure()

        for category, color in color_map.items():
            filtered_data = df[df['tipo_de_publicação'] == category]
            fig.add_trace(go.Scatter(
                x=filtered_data['data'],
                y=filtered_data['alcance'],
                mode='markers',
                marker=dict(color=color),
                name=category))

        fig.update_layout(
            width=1100,
            height=600,
            xaxis_title='Data',
            yaxis_title='Quantidade de pessoas alcançadas')

        st.markdown('###  Dispersão por alcance e por tipo de post')
        st.markdown('A uma quantidade de **373 posts que performaram entre 0 e 25.000 de alcance**, enquanto **136 performaram entre 25.001 e 50.000** e somente **12 posts performaram acima de 50.001**.   ')
        
        st.plotly_chart(fig)
        
#---------------------------------------------##---------------------------------------------#
            
        
        color_map = {
            'Carrossel do Instagram': '#ED618C',
            'Imagem do Instagram': '#FFCFC2',
            'Vídeo do Instagram': '#A8123E'}

        fig = go.Figure()

        for category, color in color_map.items():
            filtered_data = df[df['tipo_de_publicação'] == category]
            fig.add_trace(go.Scatter(
                x=filtered_data['data'],
                y=filtered_data['curtidas'],
                mode='markers',
                marker=dict(color=color),
                name=category))

        fig.update_layout(
            width=1100,
            height=600,
            xaxis_title='Data',
            yaxis_title='Número de Curtidas')

        st.markdown('### Dispersão por curtida e por tipo de post')
        st.markdown('A uma quantidade de **412 posts que performaram entre 0 e 2000 curtidas**, enquanto **82 performaram entre 2001 e 4000** e somente **27 posts performaram acima de 4000**.   ')
        
        st.plotly_chart(fig)
        
        
        
#---------------------------------------------##---------------------------------------------#
            
        
        color_map = {
            'Carrossel do Instagram': '#ED618C',
            'Imagem do Instagram': '#FFCFC2',
            'Vídeo do Instagram': '#A8123E'}

        fig = go.Figure()

        for category, color in color_map.items():
            filtered_data = df[df['tipo_de_publicação'] == category]
            fig.add_trace(go.Scatter(
                x=filtered_data['data'],
                y=filtered_data['compartilhamentos'],
                mode='markers',
                marker=dict(color=color),
                name=category))

        fig.update_layout(
            width=1100,
            height=600,
            xaxis_title='Data',
            yaxis_title='Número de Compartilhamentos')

        st.markdown('### Dispersão por compartilhamento e por tipo de post')
        st.markdown('A uma quantidade de **472 post que performaram entre 0 e 1000 compartilhamentos**, enquanto **42 posts performaram entre 1000 e 3000** e **somente 7 performaram acima de 3000**. ')
        
        
        st.plotly_chart(fig)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        