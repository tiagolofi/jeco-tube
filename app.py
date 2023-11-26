
import streamlit as st
import yt

st.set_page_config(
	page_title = 'JecoTube - o seu YouTube sem anúncios',
	layout = 'wide',
	page_icon = 'https://rotony.com.br/wp-content/uploads/2021/09/free-youtube-logo-icon-2431-thumb.png',
	initial_sidebar_state = 'collapsed' 
)

css = '''
<style>
section.main > div:has(~ footer ) {
    padding-bottom: 0px;
}
</style>
'''
st.markdown(css, unsafe_allow_html=True)

st.header('JecoTube - o seu YouTube sem anúncios', divider = 'red')

col1, col2 = st.columns(2)

with col1:

	st.subheader('Pesquisa de Vídeo')

	x1, x2 = st.columns(2)
	
	with x1:
	
		termo = st.text_input('Termo de Pesquisa:', value = 'Live de Python Eduardo Mendes')
		botao = st.button('Pesquisar')

	with x2:

		n_videos = st.number_input('Número de Vídeos (máx: 40)', value = 8, max_value = 40, min_value = 4, step = 4)
	
	if botao:
		st.session_state['ultima_busca'] = termo

	if 'ultima_busca' in st.session_state.keys():

		resultados = yt.get_data_query(search_term = st.session_state['ultima_busca'])

		lines = n_videos // 4

		c1, c2, c3, c4 = st.columns(4)

		with c1:

			for i in resultados[0:lines]:

				st.markdown(
					yt.embed_link_minimal(
						hash_video = i['hash_video']
					),
					unsafe_allow_html = True
				)
				st.write(f'''_{i['title']}_''')
				# st.image(i['thumb'], caption = i['title'] + ' - ' + i['hash_video'], width = WIDTH)

		with c2:

			for i in resultados[lines:(lines * 2)]:

				st.markdown(
					yt.embed_link_minimal(
						hash_video = i['hash_video']
					),
					unsafe_allow_html = True
				)
				st.write(f'''_{i['title']}_''')

		with c3:

			for i in resultados[(lines * 2):(lines * 3)]:

				st.markdown(
					yt.embed_link_minimal(
						hash_video = i['hash_video']
					),
					unsafe_allow_html = True
				)
				st.write(f'''_{i['title']}_''')

		with c4:

			for i in resultados[(lines * 3):(lines * 4)]:

				st.markdown(
					yt.embed_link_minimal(
						hash_video = i['hash_video']
					),
					unsafe_allow_html = True
				)
				st.write(f'''_{i['title']}_''')

with col2:

	st.subheader('Acesso com Link')

	link = st.text_input('URL do Vídeo:', value = 'https://www.youtube.com/watch?v=oCt_LiCPJfQ&ab_channel=McSuave')

	with st.expander('Mostrar/Ocultar Vídeo'):

		try: 
			st.markdown(
				yt.embed_link(
					hash_video = yt.get_hash_video(link),
				),
				unsafe_allow_html = True
			)
		except:
			pass

	s1, s2 = st.columns(2)

	with s1:

		down_but_v = st.button('Preparar Download Vídeo')

		if down_but_v:

			try:

				name, data = yt.download_va(link, 'video')

				baixar_video = st.download_button('Baixar Vídeo', data = data, file_name = name)

			except:

				st.info('Este vídeo não pode ser baixado!')

	with s2:

		down_but_a = st.button('Preparar Download Áudio')

		if down_but_a:

			try:

				name2, data2 = yt.download_va(link, 'audio')

				baixar_musica = st.download_button('Baixar Áudio', data = data2, file_name = name2)

			except:

				st.info('Este áudio não pode ser baixado!')

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
