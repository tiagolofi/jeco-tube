
import streamlit as st
from pytube import YouTube
from io import BytesIO
import yt

st.set_page_config(
	page_title = 'JecoTube - o seu YouTube sem anúncios',
	layout = 'wide',
	page_icon = 'https://rotony.com.br/wp-content/uploads/2021/09/free-youtube-logo-icon-2431-thumb.png',
	initial_sidebar_state = 'collapsed' 
)

st.header('JecoTube - o seu YouTube sem anúncios', divider = 'red')

def download_va(type_: str) -> tuple:

	buff = BytesIO()

	if type_ == 'video':

		down_ = YouTube(url = link).streams.filter(progressive = True).filter(file_extension='mp4').order_by('resolution').last()

		down_.stream_to_buffer(buff)

		return down_.default_filename, buff.getvalue()

	else:

		down_ = YouTube(url = link).streams.filter(only_audio = True).filter(file_extension='mp4').order_by('abr').last()

		down_.stream_to_buffer(buff)

		return down_.default_filename, buff.getvalue()

col1, col2, col3 = st.columns(3)

with col1:

	st.subheader('Acesso com Link')

	link = st.text_input('URL do Vídeo:', value = 'https://www.youtube.com/watch?v=oCt_LiCPJfQ&ab_channel=McSuave')

	with st.expander('Mostrar/Ocultar Vídeo'):

		st.markdown(
			yt.embed_link(
				hash_video = yt.get_hash_video(link)
			),
			unsafe_allow_html = True
		)

	s1, s2 = st.columns(2)

	with s1:

		down_but_v = st.button('Preparar Download Vídeo')

		if down_but_v:

			try:

				name, data = download_va('video')

				baixar_video = st.download_button('Baixar Vídeo', data = data, file_name = name)

			except:

				st.info('Este vídeo não pode ser baixado!')

	with s2:

		down_but_a = st.button('Preparar Download Áudio')

		if down_but_a:

			try:

				name2, data2 = download_va('audio')

				baixar_musica = st.download_button('Baixar Áudio', data = data2, file_name = name2)

			except:

				st.info('Este áudio não pode ser baixado!')
		
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

with col3:

	st.subheader('Playlist de Vídeo')

	link_playlist = st.text_input('Source da Playlist', value = "https://www.youtube.com/embed/videoseries?si=3KfAA7PN_faEeDSj&amp;list=PLjEnoakd3pXUeW8FgKdq4RLT4RFLPVoMK")

	with st.expander('Mostrar/Ocultar Playlist'):

		st.markdown(
			f'''
			<iframe 
		 		width="100%" height="300" src="{link_playlist}" 
		   		title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; 
			 		gyroscope; picture-in-picture; web-share" allowfullscreen>
			</iframe>
			''', unsafe_allow_html=True
		)

st.subheader('Pesquisa de Vídeo')

termo = st.text_input('Termo de Pesquisa:', value = 'Live de Python Eduardo Mendes')
botao = st.button('Pesquisar')

if botao:
	st.session_state['ultima_busca'] = termo

if 'ultima_busca' in st.session_state.keys():

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
