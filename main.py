from flask import Flask, render_template,  request
import os
from keras.models import load_model
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':

        model =  load_model( 'immo_model_saved.h5')
        space = request.form['space']
        etage = request.form['etage']
        nbpiece = request.form['nbpiece']
        essaie = { 'Size': int(space), 'nb_piece': int(nbpiece), 'Nb_bathroom': int(etage)}
        mm = pd.DataFrame.from_dict(essaie, orient='index',columns=["Mon_logement" ])
        valeur_à_predire = mm.T.values
        prediction = model.predict(valeur_à_predire)
        
        return render_template('page.html', input=space, output = prediction[0][0])

#if __name__ == "__main__":
#    app.run(host=os.getenv('IP', '0.0.0.0'), 
#        port=int(os.getenv('PORT', 4444)), debug=True)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google Cloud
    # Run, a webserver process such as Gunicorn will serve the app.
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))



