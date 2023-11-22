
import streamlit as st
import yt

st.set_page_config(
	page_title = 'JecoTube - o seu YouTube sem anúncios',
	layout = 'wide',
	page_icon = 'https://rotony.com.br/wp-content/uploads/2021/09/free-youtube-logo-icon-2431-thumb.png',
	initial_sidebar_state = 'collapsed' 
)

st.header('JecoTube - o seu YouTube sem anúncios', divider = 'red')

st.session_state['ultima_busca'] = "Notícias em Alta no Brasil"

col1, col2 = st.columns(2)

with col1:

    st.subheader('Acesso com Link')

    link = st.text_input('URL do Vídeo:', value = 'https://www.youtube.com/watch?v=VnaN2hYOM8k')

    with st.expander('Mostrar/Ocultar Vídeo'):

        st.markdown(
            yt.embed_link(
                hash_video = yt.get_hash_video(link)
            ),
            unsafe_allow_html = True
        )

with col2:
    
    st.subheader('Acesso com Hash')

    hash_ = st.text_input('Hash do Vídeo:')

    with st.expander('Mostrar/Ocultar Vìdeo '):

        st.markdown(
            yt.embed_link(
                hash_video = hash_
            ),
            unsafe_allow_html = True
        )

st.subheader('Pesquisa de Vídeo')

termo = st.text_input('Termo de Pesquisa:')
botao = st.button('Pesquisar')

if botao:
    st.session_state['ultima_busca'] = termo

resultados = yt.get_data_query(search_term = st.session_state['ultima_busca'])

lines = len(resultados) // 5

c1, c2, c3, c4, c5 = st.columns(5)

WIDTH = 200

with c1:
	
	for i in resultados[0:lines]:
		st.image(i['thumb'], caption = i['title'] + ' - ' + i['hash_video'], width = WIDTH)
	
with c2:
	
	for i in resultados[lines + 1:lines * 2]:
	        st.image(i['thumb'], caption = i['title'] + ' - ' + i['hash_video'], width = WIDTH)
	
with c3:
	
	for i in resultados[(lines * 2) + 1:lines * 3]:
	        st.image(i['thumb'], caption = i['title'] + ' - ' + i['hash_video'], width = WIDTH)
	
with c4:
	
	for i in resultados[(lines * 3) + 1:lines * 4]:
	        st.image(i['thumb'], caption = i['title'] + ' - ' + i['hash_video'], width = WIDTH)
	
with c5:
	
	for i in resultados[(lines * 4) + 1:len(resultados)]:
	        st.image(i['thumb'], caption = i['title'] + ' - ' + i['hash_video'], width = WIDTH) 
