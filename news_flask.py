from flask import Flask,request,jsonify,render_template,redirect,url_for,Response
from flask_cors import CORS, cross_origin
import json
app = Flask(__name__)
CORS(app)
@app.route('/news',methods=['GET','POST'])
def news():
	if request.method=='POST':
		text=request.get_json()
		query=text['text']#gets keyword given by user from search bar
		# print text['text']
		from news import get_news
		x=get_news(query)

		print x
		return jsonify(x) #returns title of news
if __name__ is '__main__':
	app.run(debug=True)