
from flask import Flask, jsonify
import pymysql
import pymysql.cursors
from config import Config

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=Config.DB_HOST,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route('/')
def home():
    connection = None

    try:
        # Connexion à la base de données
        connection = get_db_connection()

        with connection.cursor() as cursor:

            sql = """
                  SELECT seance.id       AS id_seance, \
                         seance.date     AS horaire, \
                         seance.langue, \
                         film.id         AS id_film, \
                         film.nom_film   AS titre_film, \
                         salle.id        AS id_salle, \
                         salle.num_salle AS numero_salle
                  FROM seance
                           JOIN film
                                ON film.id_seance = seance.id
                           JOIN salle
                                ON salle.id_film = film.id
                  ORDER BY ABS(TIMESTAMPDIFF(SECOND, NOW(), seance.date)) ASC LIMIT 1 \
                  """
            cursor.execute(sql)
            resultat = cursor.fetchone()

        # Retour du résultat en JSON
        return jsonify({
            "statut": "succès",
            "message": "Séance la plus proche récupérée",
            "seance": resultat
        }), 200

    except pymysql.MySQLError as error:
        return jsonify({
            "statut": "erreur",
            "message": str(error)
        }), 500

    finally:
        if connection is not None:
            connection.close()


if __name__ == '__main__':
    app.run(debug=True)
