from flask import Flask, render_template, request, jsonify
from database import recuperer_mentors
from matching import matcher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/match', methods=['POST'])
def match():
    data = request.get_json()

    matieres_demandees = data.get('matieres', [])
    heure_souhaitee = data.get('heure')
    filiere = data.get('filiere') or None

    if not matieres_demandees or not heure_souhaitee:
        return jsonify({'erreur': 'Matières et heure sont obligatoires'}), 400

    mentors = recuperer_mentors()
    resultats = matcher(mentors, matieres_demandees, heure_souhaitee, filiere)

    return jsonify(resultats)

if __name__ == '__main__':
    app.run(debug=True)