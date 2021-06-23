from flask import Flask, render_template ,request, redirect
import requests
import time
def findAvailability(pincode,date):
    URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
        pincode,date)

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

    result = requests.get(URL)
    response_json = result.json()
    print(response_json)
    data = response_json["sessions"]
    return data

app = Flask(__name__,template_folder='templates')

global URL, header

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data',methods=["POST","GET"])
def data():
    if request.method == 'POST':
        if request.form['pincode'].isdigit() and len(request.form['pincode'])==6:
            date=list(request.form['date'].split("-"))
            date.reverse()
            date=f"{date[0]}-{date[1]}-{date[2]}"
            
            data=findAvailability(request.form['pincode'],date)
            
            if len(data)==0:
                return render_template('no-slots.html')
            else:
                return render_template('data.html',data=data)
        else:
            return redirect("/")
    else:
        return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
