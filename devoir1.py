# coding : utf-8
# ©2019 - Université du Québec à Montréal

##########################
### Corrigé du devoir1 ###
##########################

### La ligne ci-dessous offre une autre façon d'importer des données dans un script
### Il s'agit, d'abord, de placer la grande variable «articles» (pas seulement son contenu, mais toute la déclaration: articles = [...])
### dans un autre fichier auquel on peut donner le nom qu'on veut (je l'ai appelé eureka.py, car les données viennent du service Eurêka)
### (pour que ça fonctionne, il faut que cet autre fichier soit un document python [se terminant par .py])
### La commande «from a import b» importe dans notre script une variable b (ou tout autre objet python) se trouvant dans le fichier a.
from eureka import articles

### J'aime bien saupoudrer des «print» régulièrement dans mes scripts, histoire de vérifier si tout fonctionne comme prévu
### quitte à mettre ces «print» en commentaire une fois la vérification faite.
# print(len(articles))

### Je déclare tout de suite six variables qui vont me servir à compter le nombre d'articles de chacun des médias inclus dans les données
lapresse = 0
ledevoir = 0
lesoleil = 0
latribune = 0
lenouvelliste = 0
lavoixdelest = 0

### On fait une boucle pour traiter le contenu de la variable «articles»
### Chaque article est placé dans la variable «article» (au singulier).
for article in articles:

	### Chaque variable «article» est une chaîne de caractères (du texte, ou une «string»)
	### Les informations qui nous intéressent sont séparées par une virgule suivie d'un espace
	### On brise notre variable en fonction de ces caractères avec la méthode «.split()»
	### Ce faisant, on transforme notre variable «article» en une liste.
	article = article.split(", ")

	### Un autre «print aux fins de vérification
	# print(len(article),article)

	### Le premier élément de notre nouvelle liste «article» contient toujours le nom du média
	### On place ce nom dans la variable «media».
	### On retranche tout espace superflu à l'aide de la méthode «.strip()»
	media = article[0].strip()

	### Tout de suite, on peut compter le nombre d'articles de chaque média à l'aide de la série de conditions suivantes
	### On se demande d'abord si le nom contenu dans la variable «media» est «La Presse+» (on aurait pu commencer par Le Devoir ou tout autre média)
	if media == "La Presse+":
	### Si cette première condition se vérifie, on ajoute 1 à notre variable servant à compter le nombre d'articles de La Presse+
		lapresse += 1
	### Sinon, on vérifie si c'est un autre média
	### La commande «elif» est la contaction de «else if», qui signifie «sinon, si»
	elif media == "Le Devoir":
		ledevoir += 1
	elif media == "Le Soleil":
		lesoleil += 1
	elif media == "La Tribune":
		latribune += 1
	elif media == "Le Nouvelliste":
		lenouvelliste += 1
	### Comme on sait qu'on n'a que six médias possibles, il n'est pas nécessaire de faire un «elif», un simple sinon («else») peut suffire.
	### «Else» n'est accompagné d'aucune condition. Il ne fait que dire ce qui se passe si toutes les conditions précédentes ne se sont pas avérées.
	else:
		lavoixdelest += 1

	### Il y avait une petite difficulté.
	### La plupart des variables «article» contenaient 4 éléments.
	### Mais certaines n'en contenaient que 3.
	### Dans ces cas, c'est l'information sur la section qui manquait.
	### Il faut donc prévoir une condition pour vérifier si on a affaire à une variable «article» avec trois ou quatre éléments
	if len(article) == 3:
		### Si «article» ne compte que 3 éléments, le nombre de mots se trouve dans le 2e élément.
		### On opère un autre «.split()» sur cet élément en fonction des espaces et on le place dans une variable appelée «mots»
		mots = article[1].split()
		### Le nombre de mots est l'avant-dernier élément de cette nouvelle variable «mots» (qui est une liste).
		### On écrase la variable «mots» avec cet avant-dernier élément qu'on débarrasse, au passage, de ses espaces superflus avec la méthode «.strip()»
		mots = mots[-2].strip()
		### On l'a dit plus tôt, si «article» ne compte que 3 éléments, c'est qu'il manque l'information sur la section. La valeur de cette variable est donc inconnue.
		section = "Inconnue"
	else: ### Ici, comme on n'a que deux cas possible (3 ou 4 éléments dans la variable «article»), s'il n'y a pas 3 éléments, c'est qu'il y en a 4, alors un «else» suffit.
		### On opère la même extraction pour le nombre de mots, mais à partir du 3e élément de la variable «article».
		mots = article[2].split()
		mots = mots[-2].strip()
		### La section se trouve dans le 2e élément de la variable «article»
		section = article[1].strip()

	### Enfin, les informations sur la page se trouvent toujours dans le dernier élément de la variable «article»
	page = article[-1].strip()

	### À chaque passage de la boucle, on en profite pour afficher les informations demandées pour chaque article:
	print("Un article de {} mots a été publié dans la section {} du journal {} en {}".format(mots,section,media,page))

### Le code ci-dessous est aligné à gauche et n'est plus «indenté» comme la ligne précédente.
### Nous sommes donc sortis de la boucle définie à la ligne 29.
### On peut désormais afficher le contenu des compteurs qu'on a élaborés pour compter le nombre d'articles par média.
print("Ce jour-là, {} articles ont été publiés dans La Presse+".format(lapresse))
print("Ce jour-là, {} articles ont été publiés dans Le Devoir".format(ledevoir))
print("Ce jour-là, {} articles ont été publiés dans Le Soleil".format(lesoleil))
print("Ce jour-là, {} articles ont été publiés dans La Tribune".format(latribune))
print("Ce jour-là, {} articles ont été publiés dans Le Nouvelliste".format(lenouvelliste))
print("Ce jour-là, {} articles ont été publiés dans La Voix de l'Est".format(lavoixdelest))

### Ce n'est pas plus compliqué que ça

############
### BONI ###
############

### Une autre méthode pour compter le nombre d'articles par média a été proposée par Martin Ouellet-Diotte
### Il s'agit d'abord de transformer la liste «articles» en une immense chaîne de caractères
art = str(articles)

### Puis d'utiliser la méthode «.count()» qui retourne le nombre d'occurences d'une chaîne recherchée dans une chaîne donnée
print("Ce jour-là, {} articles ont été publiés dans La Presse+.".format(art.count("La Presse+")))
print("Ce jour-là, {} articles ont été publiés dans Le Devoir.".format(art.count("Le Devoir")))
print("Ce jour-là, {} articles ont été publiés dans Le Soleil.".format(art.count("Le Soleil")))
print("Ce jour-là, {} articles ont été publiés dans La Tribune.".format(art.count("La Tribune")))
print("Ce jour-là, {} articles ont été publiés dans Le Nouvelliste.".format(art.count("Le Nouvelliste")))
print("Ce jour-là, {} articles ont été publiés dans La Voix de l'Est.".format(art.count("La Voix de l'Est")))