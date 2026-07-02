def heure_en_minutes(heure_str):
    """Convertit 'HH:MM' en nombre de minutes depuis minuit."""
    h, m = map(int, heure_str.strip().split(':'))
    return h * 60 + m

def parse_competences(chaine):
    """Transforme 'Python,Java' en set {'python', 'java'}."""
    return set(c.strip().lower() for c in chaine.split(','))

def parse_disponibilites(chaine):
    """Transforme '14:00-16:00,18:00-20:00' en liste de tuples (debut_min, fin_min)."""
    creneaux = []
    for plage in chaine.split(','):
        debut_str, fin_str = plage.strip().split('-')
        creneaux.append((heure_en_minutes(debut_str), heure_en_minutes(fin_str)))
    return creneaux

def matieres_communes(matieres_demandees, matieres_mentor_set):
    """Renvoie l'intersection entre matières demandées et matières du mentor."""
    demandees_set = set(m.strip().lower() for m in matieres_demandees if m.strip())
    return demandees_set & matieres_mentor_set

def horaire_compatible(heure_souhaitee_min, creneaux_mentor, tolerance=60):
    """Vérifie si l'heure souhaitée tombe dans un créneau du mentor, ±tolerance minutes."""
    for debut, fin in creneaux_mentor:
        if (debut - tolerance) <= heure_souhaitee_min <= (fin + tolerance):
            return True
    return False

def calculer_score(matieres_demandees, communes_set):
    """Score simple basé sur le pourcentage de matières en commun."""
    if not matieres_demandees:
        return 0
    score = len(communes_set) / len(matieres_demandees)
    return round(score * 100, 1)

def matcher(mentors, matieres_demandees, heure_souhaitee_str, filiere=None):
    """
    Fonction principale de matching.
    - mentors : liste de dicts venant de la BD
    - matieres_demandees : liste de strings, ex: ["Python", "Algorithmique"]
    - heure_souhaitee_str : string 'HH:MM'
    - filiere : string optionnelle
    """
    if not heure_souhaitee_str:
        return []

    heure_souhaitee_min = heure_en_minutes(heure_souhaitee_str)
    resultats = []

    for mentor in mentors:
        # Filtre optionnel sur la filière
        if filiere and mentor.get('filiere', '').lower() != filiere.lower():
            continue

        matieres_mentor_set = parse_competences(mentor['competences'])
        communes = matieres_communes(matieres_demandees, matieres_mentor_set)

        if not communes:
            continue  # aucune matière en commun -> éliminé

        creneaux_mentor = parse_disponibilites(mentor['disponibilites'])
        if not horaire_compatible(heure_souhaitee_min, creneaux_mentor):
            continue  # horaire incompatible -> éliminé

        score = calculer_score(matieres_demandees, communes)

        resultats.append({
            'nom': mentor['nom'],
            'matieres_communes': list(communes),
            'disponibilites': mentor['disponibilites'],
            'format': mentor['format_mentorat'],
            'score': score
        })

    resultats.sort(key=lambda x: x['score'], reverse=True)
    return resultats