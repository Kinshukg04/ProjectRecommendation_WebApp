from flask import Flask,render_template,url_for,request,redirect


@app.route('/')
def home():
	return render_template('index.html')
@app.route(/upload)
	return render_template('upload.html')
app = Flask(__name__)
if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)