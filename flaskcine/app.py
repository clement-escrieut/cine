from flask import Flask, jsonify
import pymysql
import pymysql.cursors
from config import Config # Importe la configuration
app = Flask(__name__)

def get_db_connection():
    """Crée la connexion à MariaDB avec les identifiants de config.py."""
    return pymysql.connect(
    host=Config.DB_HOST,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    database=Config.DB_NAME,
    cursorclass=pymysql.cursors.DictCursor
    )
# Route unique pour la page d'accueil
@app.route('/')
def home():
    connection = None

    try:
        # 1. Connexion à la base de données
        connection = get_db_connection()

        # 2. Exécution de la requête SQL
        with (connection.cursor() as cursor):
            sql = ("SELECT seance.id,seance.date AS horaire,"
                   "film.id AS id_film, "
                   "film.nom_film AS titre_film,"
                   "salle.id AS id_salle,"
                   "salle.num_salle AS numero_salle "
                   "FROM seance JOIN film ON film.id_seance = seance.id "
                   "JOIN salle ON "
                   "salle.id_film = film.id "
                   "WHERE seance.date >= NOW() "
                   "ORDER BY seance.date ASC LIMIT 1")

            print(sql)
            cursor.execute(sql)
            resultat = cursor.fetchone()


        # 3. Retour du résultat au format JSON
        return jsonify({
            "statut": "succès",
            "message": "Connexion BDD réussie !",
            "seance": resultat
        }), 200

    except pymysql.MySQLError as error:
        return jsonify({
            "statut": "erreur",
            "message": f"Erreur SQL : {str(error)}"
        }), 500

    finally:
        # 4. Fermeture de la connexion
        if connection is not None:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)