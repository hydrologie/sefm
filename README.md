# Stochastic Event Flood Model (SEFM)

sefm est une approche stochastique de génération des apports et du laminage basé 
sur la prise en compte des corrélations spatiotemporelles des conditions météo (pluie, neige au sol) et des conditions en réservoirs


## Gestion de projet
- [X] [Collecte des données météo](notebooks/ipynb/Data_Acquisition_and_Cleaning) ([JIRA](https://jiraprd03.solutions.hydroquebec.com/browse/DEBIEHH-95))
- [ ] [Classification des tempêtes](doc/task-1.3_climate-region-delineation.md) (**en cours**) ([JIRA](https://jiraprd03.solutions.hydroquebec.com/browse/DEBIEHH-150))
- [ ] Saisonnalité des tempêtes (**en cours**)
- [ ] Distribution régionale de la magnitude de la précipitation pour chaque type de tempête/durée (**en cours**)
- [ ] Distribution spatiale et temporelle des tempêtes 
- [ ] Patron temporelle de la température de l'air et du niveau de gel
- [ ] Simulation de la température de l'air à 1000 mb
- [ ] Taux de décroissance de la température de l'air
- [ ] Niveau de gel
- [ ] Échantillonage des états antécédants du modèle hydrologique HSAMI
- [ ] Mise en oeuvre du moteur SEFM (**en cours**)
- [ ] Génération stochastique des apports


## Installation et configuration de l'environnement

Git et Anaconda/Miniconda doivent préalablement être installé

```bash
git clone https://github.com/hydrologie/sefm.git
cd sefm

conda env update --name sefm --file environment.yml
```

## Utilisation

- le répertoire "sefm" contient le programme général : l'engin de calcul sefm, la base de données 
de même que les classes et les fonctions de chaque composante. L'utilisateur ne devrait pas avoir à interagir avec ce répertoire.
- le répertoire "notebook" contient l'ensemble des notes de calculs pour réaliser chaque composante de sefm. 
L'utilisateur utilisent ces notes de calculs pour appeler l'engin de calcul de "sefm" afin de réaliser les tâches du projet.
