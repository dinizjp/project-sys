import pandas as pd 
import streamlit as st
from PIL import Image 

st.set_page_config(
        page_title= 'Project SYS',
        page_icon='📈',
       layout="wide",
initial_sidebar_state="expanded")


image = Image.open('sys.png')
st.sidebar.image(image, use_column_width='auto')

st.sidebar.markdown('''---''')
st.sidebar.markdown('### Powered by Diniz JP')

st.sidebar.markdown('### Linkedin')
st.sidebar.markdown('linkedin.com/in/joão-pedro-diniz-b997b5220')

st.sidebar.markdown('### Discord')
st.sidebar.markdown('dinizjp#8730')

st.sidebar.markdown('### Github')
st.sidebar.markdown('https://github.com/dinizjp')
#---------------------------------------------#




with st.container():
    
    st.markdown(
    """ ## Projeto Análise de dados Instagram"""  )


    
    st.markdown(
    """ ##### O projeto foi desenvolvido para a empresa ShareYourSex, buscando encontrar insights que ajudem a produzir post mais acertivos para sua comunidade """  )
    
    
    st.markdown("""  
    - ### O que você vai encontrar nesse Dashboard?
        
        - ### Alcance e Visitas :
            - **Média de alcance da página entre 2021 e 2023 por mês**  
            - **Alcance da página entre 2021 e 2022 por dia** 
            - **Alcance da página entre 2022 e 2023 por dia**
            - **Média de visitas ao perfil entre 2021 e 2023 por mês**
            - **Visitas diárias ao perfil entre 2021 e 2022 por dia**
            - **Visitas diárias ao perfil entre 2022 e 2023 por dia**
            
        - ### Análise das métricas :
            - **Correlação entre as métricas**
            - **Média e Desvio Padrão das principais métricas**
            - **Média de Alcance por tipo de post**
            - **Os 20 melhores post por Alcance**
            - **Os 20 melhores post por Curtida**
            - **Os 20 melhores post por Compartilhamento**
            - **Gráficos de dispersão das 3 principais métricas: Alcance, Curtidas, Compartilhamentos.**

""")



