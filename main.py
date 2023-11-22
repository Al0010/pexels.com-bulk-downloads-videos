import pexelsPy
import requests

PEXELS_API = 'hCBODgTl5OnSfnBSTD68IoY0wyxZjmLh7I9fYamgzZGbz4Tt9wfckaIk'
api = pexelsPy.API(PEXELS_API)

pageNumbers = 1 
resultsPage = 5 

api.search_videos('Sea', page=pageNumbers, results_per_page=resultsPage)
videos = api.get_videos()


for data in videos:
    url_video = 'https://www.pexels.com/video/' + str(data.id) + '/download'
    r = requests.get(url_video)
    with open(data.url.split('/')[-2]+'.mp4', 'wb') as outfile:
        outfile.write(r.content)
