from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'challenge'
mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']

        # Insérer les données dans la base de données
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO utilisateur (nom, prenom) VALUES (%s, %s)", (nom, prenom))
        mysql.connection.commit()
        cur.close()

        return 'Données enregistrées avec succès !'
    
    return render_template('formulaire.html')

if __name__ == '__main__':
    app.run()
