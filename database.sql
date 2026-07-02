CREATE TABLE IF NOT EXISTS mentors (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    competences TEXT NOT NULL,
    disponibilites TEXT NOT NULL,
    filiere VARCHAR(100),
    format_mentorat VARCHAR(50) NOT NULL
);

INSERT INTO mentors (nom, competences, disponibilites, filiere, format_mentorat) VALUES
('Marie Adjovi', 'Python,Algorithmique,Mathématiques', '14:00-16:00,18:00-20:00', 'IA', 'en ligne'),
('Jean Koudjo', 'Java,Génie Logiciel,UML', '09:00-11:00,15:00-17:00', 'GL', 'présentiel'),
('Fatou Diallo', 'JavaScript,HTML,CSS,React', '10:00-12:00,16:00-18:00', 'SI', 'les deux');