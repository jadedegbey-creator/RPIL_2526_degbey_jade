# IFRI_MentorLink — Rattrapage Projet Intégrateur 2025-2026

## Description

Application web simplifiée de mise en relation mentor/mentoré, développée dans le cadre du rattrapage du projet intégrateur IFRI_MentorLink.

L'application permet à un mentoré de rechercher un mentor compatible selon :
- Les matières / compétences recherchées,
- L'heure de disponibilité souhaitée (avec une tolérance de ±1 heure),
- La filière (critère optionnel).

Aucune authentification n'est requise, conformément aux consignes de l'énoncé.

## Technologies utilisées

- **Frontend** : HTML, CSS, JavaScript, Bootstrap 5, Bootstrap Icons
- **Backend** : Python 3, Flask
- **Base de données** : PostgreSQL
- **Connecteur base de données** : psycopg 3 (psycopg[binary])

## Structure du projet
RPIL_2526_degbey_jade/
├── app.py
├── matching.py
├── database.py
├── database.sql
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   ├── script.js
│   └── style.css
└── README.md
## Prérequis

- Python 3.10 ou supérieur installé, avec pip fonctionnel
- PostgreSQL installé et un serveur actif localement (port 5432 par défaut)
- pgAdmin (recommandé, installé avec PostgreSQL) pour la gestion visuelle de la base

## Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/jadedegbey-creator/RPIL_2526_degbey_jade.git
cd RPIL_2526_degbey_jade
```

### 2. Installer les dépendances Python

```bash
python -m pip install -r requirements.txt
```

### 3. Créer la base de données PostgreSQL

Avec pgAdmin :
1. Ouvrir pgAdmin, se connecter au serveur PostgreSQL local.
2. Clic droit sur "Databases" puis Create puis Database.
3. Nommer la base mentorlink, puis Save.
4. Clic droit sur la base mentorlink puis Query Tool.
5. Copier-coller le contenu du fichier database.sql dans l'éditeur, puis exécuter (F5).

### 4. Configurer la connexion à la base de données

Ouvrir le fichier database.py et renseigner votre mot de passe PostgreSQL dans la variable password de la fonction get_connection().
Créer un fichier `.env` à la racine du projet, contenant :

DB_PASSWORD=votre_mot_de_passe_postgresql
### 5. Lancer l'application

```bash
python app.py
```

Le serveur démarre par défaut sur : http://127.0.0.1:5000

Ouvrir cette adresse dans un navigateur pour accéder à l'application.

## Fonctionnement de l'algorithme de matching

La fonction matcher() (fichier matching.py) applique les règles suivantes :

1. Filtre sur la filière (si renseignée) : seuls les mentors de la filière demandée sont conservés.
2. Compatibilité des compétences : un mentor est retenu uniquement s'il partage au moins une matière/compétence en commun avec la recherche.
3. Compatibilité horaire : l'heure souhaitée doit tomber dans un des créneaux de disponibilité du mentor, avec une tolérance de ±1 heure.
4. Calcul du score : le score de compatibilité correspond au pourcentage de matières demandées effectivement couvertes par le mentor.
5. Tri des résultats : les mentors compatibles sont triés par score décroissant.

## Données de test incluses

| Nom | Compétences | Disponibilités | Filière | Format |
|---|---|---|---|---|
| Marie Adjovi | Python, Algorithmique, Mathématiques | 14:00-16:00, 18:00-20:00 | IA | En ligne |
| Jean Koudjo | Java, Génie Logiciel, UML | 09:00-11:00, 15:00-17:00 | GL | Présentiel |
| Fatou Diallo | JavaScript, HTML, CSS, React | 10:00-12:00, 16:00-18:00 | SI | Les deux |

## Auteure

Degbey Jade — Licence IA/IM/GL/SE&IoT/SI — IFRI, Université d'Abomey-Calavi