# Analyse des précipitations et des tempêtes
La réalisation de l'analyse des tempêtes se décline sous plusieurs récits :
- Classification des types de tempêtes (DDST : database des type de tempêtes)
- Analyse de la saisonnalité des tempêtes
- Analyse de la magnitude et fréquence des précipitations régionales (L-moments)
- Analyse des patrons spatiotemporels des tempêtes

## Classification des types de tempêtes 
Le storm typing est réalisé à l'aide du DDST (database des tempêtes) suivant la méthodologie présentée à l'annexe E du [rapport TVA](http://www.mgsengr.com/damsafetyfiles/TVA_Point%20Precipitation-Frequency_2015-03-02_Release.pdf?target=_blank&#page=132) réalisé par MGS Eng. et MetStat.

Le storm typing est une approche de classification supervisée basé sur des variables indépendantes météorologiques. Ces variables proviennent de deux sources:
- [NOAA-CIRES-DOE 20th Century Reanalysis (v3)](https://psl.noaa.gov/data/gridded/data.20thC_ReanV3.html)
- Réseau de stations météorologiques canadiennes et américaines 
  - Environnement Canada
  - Ministère de l'Environnement 
  - Ministère des Ressources Naturelles
  - SOPFEU
  - HQP
  - HQE
  - RTA
  - Financière Agricole
  - National Weather Service

![alt text](https://github.com/hydrologie/sefm/blob/master/img/AMS.png?raw=true)
