from flask import Flask, jsonify,render_template,redirect,url_for
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
                SELECT
                    seance.id AS id_seance,
                    seance.date AS horaire,
                    seance.langue,
                    film.id AS id_film,
                    film.nom_film AS titre_film,
                    salle.id AS id_salle,
                    salle.num_salle AS numero_salle
                FROM seance
                JOIN film
                    ON film.id_seance = seance.id
                JOIN salle
                    ON salle.id_film = film.id
                ORDER BY ABS(
                    TIMESTAMPDIFF(SECOND, NOW(), seance.date)
                ) ASC
                LIMIT 1
            """

            cursor.execute(sql)
            resultat = cursor.fetchone()

        # Affichage du template HTML avec les données récupérées
        return render_template('index.html', seance=resultat)

    except pymysql.MySQLError as error:
        return jsonify({
            "statut": "erreur",
            "message": str(error)
        }), 500

    finally:
        if connection is not None:
            connection.close()


# Route sans variable : redirection vers l'accueil
@app.route('/film/')
def film_sans_variable():
    return redirect(url_for('home'))


# Route avec variable : affichage des informations du film

@app.route('/film/<int:id_film>')
def film_avec_variable(id_film):

    connection = None

    # Association entre les identifiants des films et leurs affiches
    affiches = {
        1: "affiche-croquette.jpg",
        2: "affiche-smile.jpg",
        3: "affiche-leemiller.png"
    }

    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:

            sql = """
                SELECT
                    film.id AS id_film,
                    film.nom_film AS titre_film,
                    film.resume AS resume,
                    seance.date AS horaire,
                    seance.langue,
                    salle.num_salle AS numero_salle
                FROM film
                LEFT JOIN seance
                    ON film.id_seance = seance.id
                LEFT JOIN salle
                    ON salle.id_film = film.id
                WHERE film.id = %s
            """

            cursor.execute(sql, (id_film,))
            resultat = cursor.fetchone()

        if resultat is None:
            return "Film introuvable", 404

        # Choix de l'affiche selon l'identifiant du film
        nom_affiche = affiches.get(
            id_film, "affiche-defaut.png"
        )

        return render_template(
            'film.html',
            film=resultat,
            affiche=nom_affiche
        )

    except pymysql.MySQLError as error:
        return f"Erreur SQL : {str(error)}", 500

    finally:
        if connection is not None:
            connection.close()



@app.route('/seance/<int:numSalle>')
def seances(numSalle):

    connection = None

    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:

            sql = """
                  SELECT seance.id       AS id_seance, \
                         seance.date     AS horaire, \
                         seance.langue, \
                         film.id         AS id_film, \
                         film.nom_film   AS titre_film, \
                         film.resume, \
                         salle.num_salle AS numero_salle

                  FROM seance

                           JOIN film
                                ON film.id_seance = seance.id

                           JOIN salle
                                ON salle.id_film = film.id

                  WHERE salle.num_salle = %s

                  ORDER BY seance.date ASC \
                  """

            cursor.execute(sql, (numSalle,))
            resultat = cursor.fetchall()

            cursor.execute(sql, (numSalle,))
            resultat = cursor.fetchall()

        return render_template(
            'seance.html',
            seances=resultat,
            numSalle=numSalle
        )

    except pymysql.MySQLError as error:
        return f"Erreur SQL : {str(error)}", 500

    finally:
        if connection is not None:
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)
