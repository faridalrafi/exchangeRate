from flask import Flask, render_template, json,request, redirect, url_for,jsonify

from models import db
from models import MasukanRate,ExchangeRate
app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'postgres',
    'host': 'postgres',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route("/", methods = ['POST', 'GET'])
def home():
     if request.method == 'POST':
        date = request.form['tanggal']
        data = MasukanRate.query.filter(MasukanRate.cur_Date == date).all()
        for iter_ in data :
            dari = iter_.cur_From
            ke = iter_.cur_To
            rate = iter_.cur_Rate
            data1 = MasukanRate.query.filter(MasukanRate.cur_Date >= date,MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).limit(7).all()
            list_Rate = []
            for iterate_ in data1 :
                list_Rate.append(iterate_.cur_Rate)
	# Calculate the average using data from MasukanRate Table record
            average = sum(list_Rate) / float(len(list_Rate))
            if len(list_Rate) >= 7 :
                average = sum(list_Rate) / float(len(list_Rate))
            else:
                average = 0.0
            try:
                update = ExchangeRate.query.filter(ExchangeRate.cur_Date == date,ExchangeRate.cur_From == dari,ExchangeRate.cur_To == ke).first()
                update.cur_avg_Rate = average
            
                db.session.commit()
            except:
                insert2 = ExchangeRate(cur_From = dari,cur_To = ke, cur_Date = date,cur_Rate = rate, cur_avg_Rate = average)
                db.session.add(insert2)
                db.session.commit()
        data_Curency = ExchangeRate.query.filter(ExchangeRate.cur_Date == date)
        return render_template( 'index.html',data = data_Curency,date = date)

     else:
        return render_template( 'index.html')


@app.route("/new", methods = ['POST', 'GET'])
def new():
    if request.method == 'POST':
        date = request.form['tanggal']
        dari = request.form['dari']
        ke = request.form['ke']
        rate = request.form['rate']
        insert = MasukanRate(cur_From = dari,cur_To = ke, cur_Date = date,cur_Rate = rate)
        db.session.add(insert)
        db.session.commit()
        data = MasukanRate.query.filter(MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).limit(7).all()
        list_Rate = []
        for iterate_ in data :
            list_Rate.append(iterate_.cur_Rate)
        if len(list_Rate) >= 7 :
            average = sum(list_Rate) / float(len(list_Rate))
        else:
            average = 0
        
        return ("OKE")
    else:
        return render_template( 'new.html')

@app.route("/histori", methods = ['POST', 'GET'])
def histori():
     if request.method == 'POST':
        dari = request.form['dari']
        ke = request.form['ke']
        data = MasukanRate.query.filter(MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).limit(7).all()
        list_Rate = []
        for iterate_ in data :
            list_Rate.append(iterate_.cur_Rate)
            
        if len(list_Rate) >= 7 :
            average = sum(list_Rate) / float(len(list_Rate))
        else:
            average = 0.0

        try:
            variance = max(list_Rate)- min(list_Rate)
        except:
            variance = 0.0
        return render_template( 'histori.html',data = data,average=average,variance=variance)

     else:
        return render_template( 'histori.html',data = [],average = 0)

@app.route("/hapus", methods = ['POST', 'GET'])
def hapus():
     if request.method == 'POST':
        dari = request.form['dari']
        ke = request.form['ke']
        del_data = MasukanRate.query.filter(MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).delete()
        db.session.commit()
        del_data1 = ExchangeRate.query.filter(ExchangeRate.cur_From == dari,ExchangeRate.cur_To == ke).delete()
        db.session.commit()
        return redirect("/hapus")

     else:
        data_Curency = ExchangeRate.query.filter().all()
        return render_template( 'delet.html', data = data_Curency)

@app.route("/api/data_curency", methods = ['POST','GET'])
def data_curency():
     if request.method == 'POST':
        content = request.get_json(force=True)
        date = content['date']
        data = MasukanRate.query.filter(MasukanRate.cur_Date == date).all()
        for iter_ in data :
            dari = iter_.cur_From
            ke = iter_.cur_To
            rate = iter_.cur_Rate
            data1 = MasukanRate.query.filter(MasukanRate.cur_Date >= date,MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).limit(7).all()
            list_Rate = []
            for iterate_ in data1 :
                list_Rate.append(iterate_.cur_Rate)
	# Calculate the average using data from MasukanRate Table record
            average = sum(list_Rate) / float(len(list_Rate))
            if len(list_Rate) >= 7 :
                average = sum(list_Rate) / float(len(list_Rate))
            else:
                average = 0.0
            try:
                update = ExchangeRate.query.filter(ExchangeRate.cur_Date == date,ExchangeRate.cur_From == dari,ExchangeRate.cur_To == ke).first()
                update.cur_avg_Rate = average
            
                db.session.commit()
            except:
                insert2 = ExchangeRate(cur_From = dari,cur_To = ke, cur_Date = date,cur_Rate = rate, cur_avg_Rate = average)
                db.session.add(insert2)
                db.session.commit()
        data_Curency = ExchangeRate.query.filter(ExchangeRate.cur_Date == date)
        list_data = []
        dic_rate = {}
        for x in data_Curency :
            dic_rate = {"from":x.cur_From, "To":x.cur_To}
            list_data.append(dic_rate)            
        result = jsonify({"data_Curency":list_data,"date":date})
        return (result)




@app.route("/api/new", methods = ['POST', 'GET'])
def add_Rate():
    if request.method == 'POST':
        content = request.get_json(force=True)
        date = content['tanggal']
        dari = content['dari']
        ke = content['ke']
        rate = content['rate']
        insert = MasukanRate(cur_From = dari,cur_To = ke, cur_Date = date,cur_Rate = rate)
        db.session.add(insert)
        db.session.commit()
        data = MasukanRate.query.filter(MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).limit(7).all()
        list_Rate = []
        for iterate_ in data :
            list_Rate.append(iterate_.cur_Rate)
        if len(list_Rate) >= 7 :
            average = sum(list_Rate) / float(len(list_Rate))
        else:
            average = 0
        
        message = {
        'status': 201,
        'message': 'OK'}
        resp = jsonify(message)
        resp.status_code = 201
        return (resp)
    

@app.route("/api/histori", methods = ['POST', 'GET'])
def api_histori():
     if request.method == 'POST':
        content = request.get_json(force=True)
        dari = content['dari']
        ke = content['ke']
        data = MasukanRate.query.filter(MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).limit(7).all()
        list_Rate = []
        for iterate_ in data :
            list_Rate.append(iterate_.cur_Rate)
          
        if len(list_Rate) >= 7 :
            average = sum(list_Rate) / float(len(list_Rate))
        else:
            average = 0.0

        try:
            variance = max(list_Rate)- min(list_Rate)
        except:
            variance = 0.0
        list_data = []
        for x in data :
            dic_histori = {"tanggal":x.cur_Date, "rate":x.cur_Rate}
            list_data.append(dic_histori)
        result = jsonify({"data":list_data,"average":average,"variance":variance,"From":dari,"To":ke})
        result.status_code = 200
        return ( result)


@app.route("/api/hapus", methods = ['POST', 'GET'])
def api_hapus():
     if request.method == 'POST':
        content = request.get_json(force=True)
        dari = content['dari']
        ke = content['ke']
        del_data = MasukanRate.query.filter(MasukanRate.cur_From == dari,MasukanRate.cur_To == ke).delete()
        db.session.commit()
        del_data1 = ExchangeRate.query.filter(ExchangeRate.cur_From == dari,ExchangeRate.cur_To == ke).delete()
        db.session.commit()
        message = {
        'status': 200,
        'message': 'OK'}
        return (jsonify(message))
     else:
        try:
            data_Curency = ExchangeRate.query.filter().all()
            list_data = []
            dic_rate = {}
            for x in data_Curency :
                dic_rate = {"from":x.cur_From, "To":x.cur_To}
                list_data.append(dic_rate)
            result = {
            'status': 200,
            'data':list_data}
            resp = jsonify(result)
            resp.status_code = 200
            return (resp)
        except:
            result = {
            'status': 200,
            'data':[]}
            resp = jsonify(result)
            resp.status_code = 200
            return (resp)

@app.route("/api/add_exchange_rate", methods = ['POST', 'GET'])
def api_add_exchange_rate():
     if request.method == 'POST':
        content = request.get_json(force=True)
        dari = content['dari']
        ke = content['ke']
        insert2 = ExchangeRate(cur_From = dari,cur_To = ke, cur_Date = None,cur_Rate = 0, cur_avg_Rate = 0)
        db.session.add(insert2)
        db.session.commit()
        message = {
        'status': 201,
        'message': 'OK'}
        resp = jsonify(message)
        resp.status_code = 201
        return (resp)

if __name__ == '__main__':
    app.run()
