import pandas as pd
import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from functions.lastUpdate import get_file_modification_date


st.set_page_config(
    page_title='Listagem de imoveis caixa',
    page_icon='⚖️',
    #initial_sidebar_state="collapsed",
    layout='wide'
)

file_path = "./datasets/dados_processados.csv"
file_modification_date = get_file_modification_date(file_path)
last_update_str = file_modification_date.strftime("%d/%m/%Y")
if "data" not in st.session_state:
    df = pd.read_csv("./datasets/dados_processados.csv", sep=";", encoding="ISO-8859-1", engine='python', index_col=0)

uf = st.sidebar.selectbox('Escolha a UF:', ['Todos'] + sorted(df['UF'].unique()))

#Filtros com hierarquia UF > Cidade > Bairro
if uf != "Todos":
    cidades_filtradas = sorted(df[df['UF'] == uf]['Cidade'].unique())
else:
    cidades_filtradas = sorted(df['Cidade'].unique())

cidade = st.sidebar.selectbox('Escolha a cidade:', ['Todos'] + cidades_filtradas)

if cidade != "Todos":
    bairros_filtrados = sorted(df[df['Cidade'] == cidade]['Bairro'].unique())
else:
    bairros_filtrados = sorted(df['Bairro'].unique())

bairro = st.sidebar.selectbox('Escolha o bairro:', ['Todos'] + bairros_filtrados)

if bairro != "Todos":
    tipo_venda_filtrados = sorted(df[df['Bairro'] == cidade]['Modalidade de venda'].unique())
else:
    tipo_venda_filtrados = sorted(df['Modalidade de venda'].unique())

tipo_venda = st.sidebar.selectbox('Escolha a modalidade de venda:', ['Todos'] + tipo_venda_filtrados)

if st.sidebar.button('Limpar filtros'):
    #st.rerun()
    #st.experimental_rerun
    streamlit_js_eval(js_expressions="parent.window.location.reload()") 
    

conditions = []
if uf != "Todos":
    conditions.append(df['UF'] == uf)
if cidade != "Todos":
    conditions.append(df['Cidade'] == cidade)
if bairro != "Todos":
    conditions.append(df['Bairro'] == bairro)
if tipo_venda != "Todos":
    conditions.append(df['Modalidade de venda'] == tipo_venda)

if conditions:
    combined_condition = conditions[0]
    for condition in conditions[1:]:
        combined_condition &= condition
    filtered_df = df[combined_condition]
else:
    filtered_df = df

st.write('Anuncios encontrados', filtered_df[filtered_df.columns[0]].count())
st.dataframe(
    filtered_df,
    column_config= {
         "num_property": "N° do imóvel",
         "UF" : "UF",
         "Cidade" : "Cidade",	
         "Bairro" : "Bairro",
         "Endereço" : "Endereço",
         "Preço": st.column_config.NumberColumn("Preço", format="R$ %.2f"),
         "Valor de avaliação" : st.column_config.NumberColumn("Valor de avaliação", format="R$ %.2f"),
         "Desconto" : st.column_config.ProgressColumn("Desconto %", format=" %.2f", min_value=0, max_value=100),
         "Descrição" : "Descrição",
         "Modalidade de venda" : "Modalidade de venda",	
         "Link de acesso" : st.column_config.LinkColumn("Link")
     }
)

st.write(f'Listagem mensal ultima atualização: {last_update_str}')
