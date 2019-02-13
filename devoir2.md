# Devoir 2

![](assets/mmeBolduc.png)

Vous avez découvert que [Bibliothèques et Archives nationales du Québec](http://www.banq.qc.ca/accueil/) dispose d’un API un peu secret dans la mesure où il n’est pas documenté.

Pour y faire des requêtes, il suffit d’utiliser l’URL suivant&nbsp;:

**http://collections.banq.qc.ca/api/service-notice?handle=52327/**

puis de le faire suivre d’un numéro de code quelconque.

Par exemple, avec le numéro de code **995**, on obtient l’URL [http://collections.banq.qc.ca/api/service-notice?handle=52327/995](http://collections.banq.qc.ca/api/service-notice?handle=52327/995) qui vous donne des informations sur *La java des Laurentides*, chanson de 1938 qui flaire bon le terroir.

Vous êtes curieux d’avoir une vue d’ensemble de tous les fichiers musicaux que contient BAnQ. Votre devoir consiste à satisfaire votre curiosité par le biais d'un script.

Celui-ci doit vérifier tous les numéros de code de l'API de BAnQ entre 1000 et 2000.

Lorsque le **type** est « audio », votre script doit placer les éléments suivants dans une liste que vous appellerez *infos*&nbsp;:
- le titre de la chanson ou du document audio;
- le nom du créateur du document (s’il y a plusieurs créateurs, ne prendre que le premier);
- l’année de création;
- la description matérielle du support d’enregistrement;
- l’URL du fichier audio permettant de télécharger le document (s’il y a plusieurs URLs, ne prendre que le premier).

Enfin, votre script doit enregistrer toutes ces informations dans un fichier CSV que vous appellerez **banq.csv**.

Comme la semaine dernière, vous devez enfin mettre votre script, une fois que vous l'aurez complété, dans un répertoire sur votre compte Github. Vous donnerez cette fois-ci à votre répertoire le nom de **EDM5240-devoir2** et ferez tout cela avant l'[heure de tombée](travaux.md#devoir-2---BAnQ).

<hr>

Consultez le [corrigé du devoir2](devoir2.py) et [le fichier CSV qu’il produit](banq.csv)