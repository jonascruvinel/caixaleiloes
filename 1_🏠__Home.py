import streamlit as st 

st.set_page_config(
    page_title='Home',
    page_icon="🏠",
    #initial_sidebar_state="collapsed",
    layout='wide'
)

st.title("Lista completa de imóveis!")

st.write(
    """
       Os dados aqui expostos foram obtidos a partir do relatório mensal de imóveis que estão disponíveis para comercialização pela
       Caixa Econômica Federal. Salienta-se que esta lista é de acesso público. Os registros indicam uma alta frequência de negociações,
       com uma média superior a 15.000 imóveis transacionados por mês. Esta circunstância representa significativas oportunidades 
       tanto para investidores interessados em lucrar quanto para aqueles que desejam adquirir imóveis a preços inferiores aos de mercado.
       Para obter informações adicionais, convida-se os interessados a visitar o site oficial da instituição, acessando o seguinte link:
    """
)
st.write('[Caixa Econômica Federal](https://venda-imoveis.caixa.gov.br/sistema/download-lista.asp)')
st.sidebar.markdown("Desenvolvido por [jonascruvinel](https://github.com/jonascruvinel)")
