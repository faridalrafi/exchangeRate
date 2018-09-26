from flask import Flask, render_template, json,request, redirect, url_for

from models import db
from models import MasukanRate,ExchangeRate
app = Flask(__name__)

POSTGRES = {
    'user': 'farid',
    'pw': 'farid',
    'db': 'tes_farid',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db.init_app(app)

@app.route("/", methods = ['POST', 'GET'])
def main():
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
	#
            average = sum(list_Rate) / float(len(list_Rate))
            if len(list_Rate) >= 7 :
                average = sum(list_Rate) / float(len(list_Rate))
            else:
                average = 0.0
            try:
                update = ExchangeRate.query.filter(ExchangeRate.cur_Date == date,ExchangeRate.cur_From == dari,ExchangeRate.cur_To == ke).first()
                update.cur_avg_Rate = average
            #insert2 = ExchangeRate(cur_From = dari,cur_To = ke, cur_Date = date,cur_Rate = rate, cur_avg_Rate = average)
            #db.session.add(insert2)
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
        #insert2 = ExchangeRate(cur_From = dari,cur_To = ke, cur_Date = date,cur_Rate = rate, cur_avg_Rate = average)
        #db.session.add(insert2)
        #db.session.commit()
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
            #average = sum(list_Rate) / float(len(list_Rate))
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
        return render_template( 'histori.html')

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

if __name__ == '__main__':
    app.run()
