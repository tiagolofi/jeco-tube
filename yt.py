
import requests
import re
import json

def get_hash_video(url: str) -> str:

    if '&' in url:
        return re.search(r'=(.*?)&', url).group(1)
    else:
        return re.search(r'=(.*?)&', url + '&').group(1)

def embed_link(hash_video: str) -> str:

    return f'''
    <iframe
        width="100%" height="300" src="https://www.youtube-nocookie.com/embed/{hash_video}"
	frameborder="0" allow="autoplay; encrypted-media" allowfullscreen> 
    ></iframe>
    '''

def get_data_query(search_term: str) -> list:

    url_query = f'''https://www.youtube.com/results?search_query={search_term}'''

    session = requests.get(
        url_query, 
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
    )

    data_unestrutured = re.findall(r'''{"videoRenderer":(.*?),"longBylineText''', session.text)

    list_struc = []

    for i in data_unestrutured:
        data_un = json.loads(i + '}')
        list_struc.append(
            {
                'hash_video': data_un['videoId'],
                'thumb': data_un['thumbnail']['thumbnails'][0]['url'],
                'title': data_un['title']['runs'][0]['text']
            }
        )

    return list_struc
