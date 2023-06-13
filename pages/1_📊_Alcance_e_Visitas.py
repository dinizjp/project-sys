import pandas as pd 
import streamlit as st
from PIL import Image 
import plotly.express as px


st.set_page_config(
        page_title= 'Análise das Médias',
        page_icon='📊',
       layout="wide")


image = Image.open('sys.png')
st.sidebar.image(image, use_column_width='auto')

st.sidebar.markdown('''---''')
st.sidebar.markdown('### Powered by Diniz JP')





#---------------------------------------------##---------------------------------------------#
## Tabs

tab1, tab2, = st.tabs( ['Alcance da página', 'Visitas ao Perfil'])


#---------------------------------------------##---------------------------------------------#
#Ploty 1 -  Média de alcance da página entre 2021 e 2023 por mês

with tab1:   
    
    with st.container():
        
        st.markdown('### Média de alcance da página entre 2021 e 2023 por mês')
        st.markdown('Nota-se uma diminuição da média de alcance da página ao longo do ano, possíveis causas são: **Atualização constante do algoritmo do insta**, **Aumento do consumo no tiktok** e **Maior incentivo ao consumo de vídeo em relação aos outros formatos**.')
        

        df = pd.read_csv('project-sys/Alcance_pagina.csv', sep=';')

        df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

        df_grouped = df.groupby(pd.Grouper(key='Data', freq='M')).mean().reset_index()

        # Criar uma nova coluna com o primeiro dia de cada mês
        df_grouped['Data_inicio_mes'] = pd.to_datetime(df_grouped['Data'].dt.year.astype(str) + '-' +
                                                       df_grouped['Data'].dt.month.astype(str) + '-01')

        fig = px.bar(df_grouped, x='Data_inicio_mes', y='Alcance do Instagram', 
                     width=1100,
                     height=500,
                     color_discrete_sequence=['#ED618C'])

        fig.update_layout(
            xaxis_title="<b>Data<b>",
            yaxis_title="<b>Alcance<b>"
        )

        fig.update_xaxes(
            tickformat="%b %Y"
        )

        st.plotly_chart(fig)

#---------------------------------------------##---------------------------------------------#
#Ploty 2 -  Alcance diário da pagina durante o periodo de 2021 a 2023
    
    df_periodo1 = df[(df['Data'] >= '2021-04-24') & (df['Data'] <= '2022-04-24')]

    df_periodo2 = df[(df['Data'] >= '2022-04-25') & (df['Data'] <= '2023-04-24')]    

    
    fig1 = px.line(df_periodo1, x='Data', y='Alcance do Instagram',
               width=1100, height=500,
               color_discrete_sequence=['#ED618C'],
              )


    fig1.update_layout(
        xaxis_title="<b>Data<b>",
        yaxis_title="<b>Alcance da página<b>",
    )


    fig2 = px.line(df_periodo2, x='Data', y='Alcance do Instagram',
                   width=1100, height=500,
                   color_discrete_sequence=['#ED618C'],
                  )

    fig2.update_layout(
        xaxis_title="<b>Data<b>",
        yaxis_title="<b>Alcance da página<b>")


    
    st.markdown('### Alcance da página entre 2021 e 2022 por dia')
    st.markdown('Entre 2021 e 2022 há uma variação maior em relação ao alcance, possível causa **Criação da página recente com grande migração da comunidade do facebook para página no insta**. ')
    
    
    st.plotly_chart(fig1)
    
    
    st.markdown('### Alcance da página entre 2022 e 2023 por dia')
    st.markdown('Entre 2022 e 2023 o alcance ainda oscila bastante em um **range de 1050 / 58.000**, é necessário uma análise detalhada dos picos para entender o a causa dessa dispersão.')
    
    
    st.plotly_chart(fig2)
    
    
#---------------------------------------------##---------------------------------------------#
#Ploty 3 -  Média de visitas por mês durante o periodo de 2021 a 2023

with tab2:    
    with st.container():

        st.markdown('### Média de visitas ao perfil entre 2021 e 2023 por mês ')
        st.markdown('Há uma **tendência decrescente** na média visitas do perfil entre Julho de 2021 e Feveiro de 2022. E logo em seguida uma **tendência crescente** entre Março de 2022, chegando ao pico em Janeiro de 2023 com uma **média de 2.340 visitas por dia no mês de Janeiro**. ')
                    
                    
                    
                    

        path= ('project-sys/visitas_perfil_21_23.csv')

        df_visita = pd.read_csv(path, sep=';')

        df_visita['Data'] = pd.to_datetime(df_visita['Data'], format='%d/%m/%Y')

        df_grouped = df_visita.groupby(pd.Grouper(key='Data', freq='M')).mean().reset_index()

        df_grouped['Data_inicio_mes'] = pd.to_datetime(df_grouped['Data'].dt.year.astype(str) + '-' +
                                                       df_grouped['Data'].dt.month.astype(str) + '-01')

        fig = px.bar(df_grouped, x='Data_inicio_mes', y='Seguidores do Instagram', 
                    width=1100,
                    height=500,
                    color_discrete_sequence=['#ED618C'])

        fig.update_layout(
            xaxis_title="<b>Data<b>",
            yaxis_title="<b>Número de visitas ao perfil<b>")

        fig.update_xaxes( tickformat="%b %Y")


        st.plotly_chart(fig)


#---------------------------------------------##---------------------------------------------#
#Ploty 4 -  quantidade de visitas diárias durante o periodo de 2021 a 2023

        df_periodo1 = df_visita[(df_visita['Data'] >= '2021-04-24') & (df_visita['Data'] <= '2022-04-24')]

        df_periodo2 = df_visita[(df_visita['Data'] >= '2022-04-25') & (df_visita['Data'] <= '2023-04-24')]

        y_max = max(df_periodo1['Seguidores do Instagram'].max(), df_periodo2['Seguidores do Instagram'].max())
        y_min = min(df_periodo1['Seguidores do Instagram'].min(), df_periodo2['Seguidores do Instagram'].min())
        
        fig1 = px.line(df_periodo1, x='Data', y='Seguidores do Instagram',
                       width=1100, height=500,
                       color_discrete_sequence=['#ED618C'],
                      )


        fig1.update_layout(
            xaxis_title="<b>Data<b>",
            yaxis_title="<b>Número de visitas ao perfil<b>",
             yaxis_range=[y_min, y_max])



        fig2 = px.line(df_periodo2, x='Data', y='Seguidores do Instagram',
                       width=1100, height=500,
                       color_discrete_sequence=['#ED618C'],
                      )

        fig2.update_layout(
            xaxis_title="<b>Data<b>",
            yaxis_title="<b>Número de visitas ao perfil<b>",
             yaxis_range=[y_min, y_max])

        st.markdown('### Visitas diárias ao perfil entre 2021 e 2022 por dia ')
        st.markdown('Podemos ver a mesma **tendência** encontrada no gráfico da média, podendo fazer uma análise mais detalhada nos picos de alta e baixa, para entender quais posts estão por trás dessas oscilações positivas e negativas.')

        st.plotly_chart(fig1)

        st.markdown('### Visitas diárias ao perfil entre 2022 e 2023 por dia ')
        st.markdown('Podemos ver a mesma **tendência** encontrada no gráfico da média, podendo fazer uma análise mais detalhada nos picos de alta e baixa, para entender quais posts estão por trás dessas oscilações positivas e negativas.')
        

        st.plotly_chart(fig2)

    #---------------------------------------------##---------------------------------------------#
