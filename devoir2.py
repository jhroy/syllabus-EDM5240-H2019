# ©2019 Jean-Hugues Roy. GNU GPL v3.
# coding: utf-8

##########################
### Corrigé du devoir2 ###
##########################

# On importe tout ce dont on a besoin.
import csv, requests, json

# On place le nom du fichier CSV qu'on va créer dans une variable.
# Ce n'est pas strictement nécessaire, mais ça facilite le travail si, pour faire des tests, on veut temporairement changer ce nom.
fich = "banq.csv"

# Initialisation d'un compteur pour voir combien de documents, sur l'ensemble, sont de type audio.
nAudio = 0

# Pour ramasser les numéros d'items entre 1000 et 2000,
# on fait une boucle dans un «range» de 1000 à 2001 (le dernier item est toujours exclu dans un «range»).
# À chaque itération, la valeur de la variable «essai» changera, passant de 1000 à 2000, avec toutes les valeurs possibles entre les deux.
for essai in range(1000,2001):

	# On crée une liste pour enregistrer les informations qu'on va recueillir dans l'API de BAnQ.
	infos = []

	# On fait du journalisme à visage découvert.
	entetes = {
		"User-Agent":"Bonjour! Je m'appelle Jean-Hugues Roy. Cette requête est transmise dans le cadre d'un exercice pour un cours de journalisme de données que je donne à l'UQAM (EDM5240)",
		"From":"roy.jean-hugues@uqam.ca"
	}

	# À chaque itération de notre boucle, la variable «url» changera en fonction de la valeur de la variable «essai».
	url = "http://collections.banq.qc.ca/api/service-notice?handle=52327/{}".format(essai)

	# On peut formuler notre requête ainsi et déposer le résultat dans la variable «req».
	req = requests.get(url,headers=entetes)

	# Affichage pour suivre, au fur et à mesure, le travail de notre script.
	# La classe «.status_code» retourne un nombre entier correspondant à un code
	# qui est en quelque sorte la réponse que nous donne le site auquel on veut se connecter.
	# Si vous êtes curieuse.eux, la liste complète de ces codes est ici: [https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP](https://fr.wikipedia.org/wiki/Liste_des_codes_HTTP).
	print("   >>> L'essai {} donne le code {}.".format(essai,req.status_code))

	# Si ce code est égal à 200, c'est que le site est accessible.
	if req.status_code == 200:

		# On peut donc procéder en extrayant le contenu JSON de «req» à l'aide de la méthode «.json()»
		# et en déposant ce contenu dans une variable qu'on peut appeler «donnees», par exemple.
		donnees = req.json()

		### Stéphanie Prévost me propose la méthode ci-dessous pour faire en sorte que le contenu .json
		### soit affiché proprement (en anglais, on appelle ça le mode «beautify»).
		### Le résultat est beaucoup plus facile à lire au terminal.
		print(json.dumps(donnees, indent=4, sort_keys=True)) # On peut mettre cette ligne en commentaire après avoir fait quelques tests, si ces tests sont concluants.

		# Comme on ne cherche que les documents de type audio, il faut vérifier la condition suivante:
		if donnees["type"] == "audio":

			# Si le document est de type audio, on ajoute 1 à notre compteur de documents audio.
			nAudio += 1

			# Tous les «print()» ci-dessous peuvent être mis en commentaires.
			# Mais ils sont utiles pendant qu'on rédige notre script afin de vérifier si on va chercher les bonnes informations.
			# print(donnees["titre"])
			# print(donnees["createurs"][0])
			# print(donnees["dateCreation"])
			# print(donnees["descriptionMat"])
			# print(donnees["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"])

			# On peut commencer à ajouter des éléments dans notre liste «infos».
			# Je commence souvent par mettre des informations qui permettent de faire un suivi en cas de pépin,
			# comme la valeur des variables «essai» et «nAudio» qui nous donnent une idée d'où on est rendu.
			infos.append(essai)
			infos.append(nAudio)

			# Ensuite, on peut ajouter, une à la fois, les informations qui nous intéressent dans le .json que nous envoie BAnQ.
			infos.append(donnees["titre"])
			infos.append(donnees["createurs"][0])
			infos.append(donnees["dateCreation"])
			infos.append(donnees["descriptionMat"])

			# Il y avait un obstacle, comme il y en a souvent avec les données.
			# Le Reel du gailuron (quel titre!) n'est pas accompagné d'un fichier sonore.
			# On n'y trouve donc pas d'url et notre script plante.
			# Il y a deux façons de contourner cet obstacle.

			# FAÇON 1 -> AVEC UN BON VIEUX «IF»:
			if "url" in donnees["bitstreams"]["racine"]["fils"][0]["formats"][0]:
				infos.append(donnees["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"])
			else:
				infos.append("URL inconnu")

			# FAÇON 2 -> EN UTILISANT CE QU'ON APPELLE «LA GESTION DES ERREURS», OU «ERROR HANDLING»
			# La gestion des erreurs consiste à essayer du code et à proposer une alternative si ce code fait planter notre script.
			# La syntaxe est plus simple qu'un «if».
			# On dit juste: «Essaie d'ajouter l'url à la liste «infos»»:
			try:
				infos.append(donnees["bitstreams"]["racine"]["fils"][0]["formats"][0]["url"])

			# Et on indique quoi faire si cet essai donne une erreur:
			except:
				infos.append("URL inconnu")

			# Un petit «print()» aux fins de vérification.
			print(infos)

			# Puis, à chaque fois qu'on trouve un document de type audio, on l'ajoute à notre CSV.
			# Il est important que cet enregistrement soit correctement indenté
			# afin qu'il se fasse à l'intérieur de notre boucle et des conditions qu'on vérifie.
			ying = open(fich, "a")
			yang = csv.writer(ying)
			yang.writerow(infos)
