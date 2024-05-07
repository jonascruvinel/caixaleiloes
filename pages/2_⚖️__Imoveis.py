import pandas as pd
import streamlit as st
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(
    page_title='Listagem de imoveis caixa',
    page_icon='⚖️',
    #initial_sidebar_state="collapsed",
    layout='wide'
)


if "data" not in st.session_state:
    df = pd.read_csv(".\datasets\dados_processados.csv", sep=";", encoding="ISO-8859-1", engine='python', index_col=0)

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

#if tipo_venda != "Todos":
#    flg_fgts_filtrados = sorted(df[df['Mod_venda'] == tipo_venda]['flg_fgts'].unique())
#else:
#flg_fgts_filtrados = sorted(df['flg_fgts'].unique())
      
#flg_fgts = st.sidebar.selectbox('FGTS:', ['Todos'] + flg_fgts_filtrados)
                                          
#if flg_fgts != "Todos":
#    flg_financiamento_filtrados = sorted(df[df['flg_fgts'] == flg_fgts]['flg_financiamento'].unique())
#else:
#    flg_financiamento_filtrados = sorted(df['flg_financiamento'].unique())
    
#flg_financiamento = st.sidebar.selectbox('Financiamento:', ['Todos'] + flg_financiamento_filtrados)

#if flg_financiamento != "Todos":
#    flg_parcelamento_filtrados = sorted(df[df['flg_financiamento'] == flg_financiamento]['flg_parcelamento'].unique())
#else:
#    flg_parcelamento_filtrados = sorted(df['flg_parcelamento'].unique())

#flg_parcelamento = st.sidebar.selectbox('Parcelamento:', ['Todos'] + flg_parcelamento_filtrados)

#if flg_parcelamento != "Todos":
#    flg_consorcio_filtrados = sorted(df[df['flg_parcelamento'] == flg_parcelamento]['flg_consorcio'].unique())
#else:
#    flg_consorcio_filtrados = sorted(df['flg_consorcio'].unique())

#flg_consorcio = st.sidebar.selectbox('Consorcio:', ['Todos'] + flg_consorcio_filtrados)

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
#if flg_fgts != "Todos":
#    conditions.append(df['flg_fgts'] == flg_fgts)
#if flg_financiamento != "Todos":
#    conditions.append(df['flg_financiamento'] == flg_financiamento)
#if flg_parcelamento != "Todos":
#    conditions.append(df['flg_parcelamento'] == flg_parcelamento)
#if flg_consorcio != "Todos":
#    conditions.append(df['flg_consorcio'] == flg_consorcio)

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