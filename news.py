import json
import requests



url='https://api.newsapi.aylien.com/api/v1/stories?title=&published_at.start=NOW-60DAYS%2FDAY&published_at.end=NOW&categories.id%5B%5D=&categories.taxonomy=iab-qag&sort_by=relevance'
headers={'X-AYLIEN-NewsAPI-Application-ID':'5a962e4f','X-AYLIEN-NewsAPI-Application-Key':'b989dcacb25936a63412aa8feeacf017'}
# Get the news title based on the keyword given
def  get_news(q):
	pay={
	"title":q,
	"categories.id":'IAB19',
	# Category id for news:IAB12, Category id for technology: IAB19 the rest is given in the documentation of API
	}
	j=requests.get(url,params=pay,headers=headers)

	json_file= json.dumps(j.json(),indent=4)
	json_dict=json.loads(json_file)
	news_title=[]
	for i in range(0,len(json_dict['stories'])):
		news_title.append(json_dict['stories'][i]['title'])
# For news summary,images use json_dict['stories'][i]['summary']['sentences'],json_dict['stories'][i]['media'][0]['url'] respectively

	return news_title
