from flask import Flask, request, render_template


app = Flask(__name__) #Bu instance i kendimize uyarliyoruz. Acip tekrar tekrar kullaniyoruz.

@app.route("/")
def home():
    return "Hello world"



@app.route('/<name>')
def hi(name):
    return f"Hello <b>{name.capitalize()}</b>, welcome to my homepage"

@app.route('/hello')
def hello():
    name='John'
    return f"<h3>Hello {name}, welcome to my homepage"

@app.route('/diff')
def diff():
    name='John'
    return f"Hello <b>{name}</b>, welcome to my homepage"

data = {
    'ankara' : {'region' : 'middle anatolia', 'pop': '3.5m', 'places' : ['ulus', 'kizilay', 'sincan']},
    'izmir' : {'region' : 'west anatolia', 'pop' : '4m', 'places ': ['kordon', 'saat kulesi', 'goztepe', 'konak']},
    'konya' : {'region' : 'middle anatolia', 'pop' : '2m', 'places' : ['alaaddin tepesi', 'mevlana']}
}

@app.route('/city/<city>')
def city(city):
    return {'data':str(data[city])}

@app.route('/city/<city>/<feature>')
def city_f(city,feature):
    return {'data':str(data[city][feature])}

def mass_index(w,h):
    return h**2/w

@app.route('/calc')
def calc():
    w=float(request.args['w'])
    h=float(request.args['h'])
    return {'Your mass index' : f'{(mass_index(w,h)):.2f}'}

# json formati ile gelen value' lari alacak, bunlari coef degerleri ile carpip toplayip geri gonderecek :
def predict(vals):
    import numpy as np
    coefs = np.array([1,2,3])
    return sum(coefs*vals)

# Gerekli olan vals' lari gelen json formatindaki degerleri okuyarak alacak. Bunlari alip floata cevirecek. 
# Bir array elde ettikten sonra  prediction fonksiyonuna gonderecek ve bir sonuc getirecek :
@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == 'GET' :
        return 'My api server is running'
    else :
         data = request.json.values()
         print(data) # Hata cikmasina karsin kodun nerde calismadigini anlamak icin 'debug' etmek gerekir. Bu yuzden her adimda print yaptik. Bunlar terminalde gorunecek.
         vals = [float(i) for i in data]  #  reguest.json' in icine gelen value' lari bir listeye ve floata cevirecek.
         print(vals) 
         pred = predict(vals) # Bu value' lar ile bir prediction elde edecek.
         print('result: ', pred)
         return {'prediction result': f'$ {pred:.2f}'}

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == 'GET' :
        return render_template('index.html')
    else :
         data = request.form.values()  # else deyince post kismi aktif olacak.
         print(data) # Hata cikmasina karsin kodun nerde calismadigini anlamak icin 'debug' etmek gerekir. Bu yuzden her adimda print yaptik. Bunlar terminalde gorunecek.
         vals = [float(i) for i in data]  #  reguest.json' in icine gelen value' lari bir listeye ve floata cevirecek.
         print(vals) 
         pred = predict(vals) # Bu value' lar ile bir prediction elde edecek.
         print('result: ', pred)
         return render_template('index.html', result=pred)

if __name__ == "__main__":       # Dosya dogrudan cagrilirsa run et.
        app.run(debug=True, host="0.0.0.0", port=80)

