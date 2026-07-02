document.getElementById('formRecherche').addEventListener('submit', async function (e) {
    e.preventDefault();

    const matieres = document.getElementById('matieres').value
        .split(',')
        .map(m => m.trim())
        .filter(m => m.length > 0);
    const heure = document.getElementById('heure').value;
    const filiere = document.getElementById('filiere').value.trim();

    const conteneur = document.getElementById('resultats');
    conteneur.innerHTML = '<p>Recherche en cours...</p>';

    try {
        const reponse = await fetch('/api/match', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ matieres, heure, filiere })
        });

        if (!reponse.ok) {
            const erreur = await reponse.json();
            conteneur.innerHTML = `<p class="text-danger">Erreur : ${erreur.erreur || 'inconnue'}</p>`;
            return;
        }

        const resultats = await reponse.json();
        afficherResultats(resultats);
    } catch (err) {
        conteneur.innerHTML = '<p class="text-danger">Erreur de connexion au serveur.</p>';
        console.error(err);
    }
});

function afficherResultats(resultats) {
    const conteneur = document.getElementById('resultats');
    conteneur.innerHTML = '';

    if (resultats.length === 0) {
        conteneur.innerHTML = '<p class="alert alert-warning">Aucun mentor compatible trouvé.</p>';
        return;
    }

    resultats.forEach(mentor => {
        conteneur.innerHTML += `
            <div class="card mb-3 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">${mentor.nom} <span class="badge bg-success">${mentor.score}%</span></h5>
                    <p class="mb-1"><strong>Matières en commun :</strong> ${mentor.matieres_communes.join(', ')}</p>
                    <p class="mb-1"><strong>Disponibilités :</strong> ${mentor.disponibilites}</p>
                    <p class="mb-0"><strong>Format :</strong> ${mentor.format}</p>
                </div>
            </div>
        `;
    });
}