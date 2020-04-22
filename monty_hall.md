# Monty Hall (difficile)

Critères de notation:

* Difficulté du sujet choisi 
* Lisibilité du code
* Effort de groupe, au moins 1 commit par membre du groupe (pas de commit = pas de note!)

## Enoncé du problème

Le problème de Monty Hall est un casse-tête probabiliste librement inspiré du jeu télévisé américain __Let's Make a Deal__. 

Le jeu oppose un présentateur à un candidat (le joueur). Ce joueur est placé devant trois portes fermées.
Derrière l'une d'elles se trouve une voiture et derrière chacune des deux autres se trouve une chèvre.
Il doit tout d'abord désigner une porte. 
Puis le présentateur doit ouvrir une porte qui n'est ni celle choisie par le candidat, ni celle cachant la voiture (le présentateur sait quelle est la bonne porte dès le début). 
Le candidat a alors le droit d'ouvrir la porte qu'il a choisie initialement, ou d'ouvrir la troisième porte.

Les questions qui se posent au candidat sont :

* Que doit-il faire ?
* Quelles sont ses chances de gagner la voiture en agissant au mieux ?

## Modélisation

On souhaite modéliser le jeu comme suit:

- une classe `Game` qui modélise une partie
- une classe `Door` qui modélise une porte

Une partie contient 3 portes.

Chaque porte peut être:
* gagnante ou perdante
* désignée ou non par le candidat
* ouverte ou non par le présentateur

Une partie se déroule en appelant les méthodes dans l'ordre suivant:

* `init_game` : qui initialise une nouvelle partie en désignant aléatoirement une porte gagnante.
* `choose`: qui permet au joueur de désigner une porte
* `reveal`: qui renvoie la porte ouverte par le présentateur
* `open`: qui permet au joueur d'ouvrir une porte et lui indique s'il a gagné ou perdu

## Tests unitaires

Ecrire des tests unitaires vérifiant le bon fonctionnement des méthodes implémentées.

## Implémentation

Il existe deux stratégies:

* ouvrir la porte choisie initialement
* ou changer et ouvrir la troisième porte

On souhaite déterminer si une des deux stragégies est meilleure que l'autre.

Pour cela, on va simuler `N` parties pour chacune des deux stratégies et compter le nombre de victoires.

Pour chaque simulation, on va donc:

* initialiser une nouvelle partie 
* choisir une porte aléatoire
* récupérer la porte revelée
* en fonction de la stratégie testée, ouvrir l'une ou l'autre des portes

## Conclusion

Tester la simulation pour `N=10`, `N=1000` et `N=100000`. Que peut-on conclure?
