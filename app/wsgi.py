from flask import Flask, render_template ,request, redirect
#from requests.api import request
app = Flask(__name__,template_folder='templates')
from templates.Cowin_Slots import *

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

            if data==False:
                return redirect("/")
            elif len(data)==0:
                return render_template('no-slots.html')
            else:
                return render_template('data.html',data=data)
        else:
            return redirect("/")
    else:
        return redirect("/")

if __name__ == '__main__':
    app.run()
