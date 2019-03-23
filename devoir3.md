# Devoir 3

<img style="border:dotted #ff33cc 10px;" src="assets/deputeHonoreMercier.jpg">

*Bonsoir…*

Vous me reconnaissez certainement, alors nul besoin de me présenter.

Vous vous intéressez aux subventions octroyées par le ministère dont j’ai la responsabilité? Quel honneur vous me faites!

Laissez-moi vous aider.

Commencez par aller chercher un fichier de données dans le [portail de données ouvertes de mon gouvernement](https://ouvert.canada.ca/data/fr/dataset/432527ab-7aac-45b5-81d6-7597107a7013?_ga=2.226424798.573001236.1552335882-176626075.1551983477). Téléchargez la ressource appelée *Divulgation des octrois de subventions et de contributions*. Le fichier de près de 240 Mo s’appelle [**_grants.csv_**](https://open.canada.ca/data/dataset/432527ab-7aac-45b5-81d6-7597107a7013/resource/1d15a62f-5656-49ad-8c88-f40ce689d831/download/grants.csv). Il contient près d’un quart de million de subventions octroyées par différents ministères ces dernières années, surtout en 2018. Je sais. On est généreux.

Créez un carnet (*notebook*) Jupyter qui commencera par une cellule d’entête (*heading*) et qui&nbsp;:

- lira le fichier *grants.csv* (vous pouvez le lire dans le web [en entrant son URL complet] ou le télécharger et le lire localement);
- éliminera de ce fichier les colonnes dans lesquelles se trouve de l’information en anglais seulement;
- donnera des noms français aux colonnes qui restent;
- fera le ménage dans la colonne contenant le montant de la subvention (*«agreement_value»*) pour la transformer en un nombre que Pandas peut traiter;
- fera la liste de tous les programmes de mon ministère;
- créera un sous-ensemble avec le programme qui a octroyé le plus grand nombre de subventions (vous verrez, ce programme a un lien avec le journalisme);
- fera la liste des entreprises [selon leur nom légal] qui ont le plus bénéficié de ce programme (par ordre descendant du montant reçu);
- calculera le pourcentage des subventions reçues par chaque province en vertu de ce programme (histoire de voir si le Québec tire bien son épingle du jeu).

À chacune des étapes décrites dans la liste ci-dessus, votre carnet devra inclure au moins une cellule de texte qui décrira ce que vous faites et/ou l’information que *pandas* vous permet de découvrir.

Nommez ce carnet **devoir3.ipynb**.

Placez-le dans un nouveau répertoire (*«repo»*) de votre compte Github que vous baptiserez **EDM5240-devoir-3**.

Bien sûr, la tombée a été repoussée d’une semaine en raison de :snowflake: et de :loudspeaker:. C’est désormais le **17 mars 2019**, toujours **à 23h59**.

N’hésitez pas à consulter le [formidable tutoriel](https://github.com/jhroy/tuto-pandas) confectionné avec :heart: par votre sympathique professeur.

Bonne chance et au plaisir de vous serrer la main dans un souper-spaghetti dans mon comté.

<hr>

Je vous invite maintenant à consulter le [corrigé de mon devoir](devoir3-corrige.ipynb)