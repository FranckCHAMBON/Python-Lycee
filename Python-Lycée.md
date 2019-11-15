---
export_on_save:
  html: true
---

<!-- @import "assets/EducNat.jpg" {width="400px" title="Logo de l'Éducation Nationale" alt="Logo de l'Éducation Nationale"} -->

# Python au lycée - une présentation {ignore=true}

@import "assets/Python.svg" {width="400px" title="Logo de Python" alt="Logo de Python"}

Auteur : <a href="mailto:franck.chambon@ac-aix-marseille.fr">Franck CHAMBON</a>, enseignant au lycée Lucie AUBRAC de Bollène.

@import "assets/CC-BY-NC-SA.svg" {width="100px" title="Licence" alt="Licence CC-BY-NC-SA-4.0"}

Les documents suivants sont placés sous licence libre [CC - BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode.fr) :

- Ils sont accessibles gratuitement.
- Ils peuvent être modifiés, adaptés, étoffés, quitte à citer les différents auteurs.
- Leur utilisation commerciale n'est pas acceptée.

## Sommaire {ignore=true}

[TOC]

## :fa-question-circle: Pourquoi Python

Dans le [bulletin Officiel](https://cache.media.education.gouv.fr/file/SP1-MEN-22-1-2019/26/8/spe633_annexe_1063268.pdf) du programme de NSI, on trouve une justification de ce choix pour *Python* :
> **Modalités de mise en œuvre**
>>Les activités pratiques et la réalisation de projets supposent, pour chaque élève, l’accès à un équipement relié à internet. Un langage de programmation est nécessaire pour l’écriture des programmes :  un  langage simple d’usage, interprété, concis, libre et gratuit, multiplateforme, largement répandu, riche de bibliothèques adaptées et bénéficiant d’une vaste communauté d’auteurs dans le monde éducatif  est  à  privilégier.  Au  moment  de  la  conception  de  ce  programme,  le  langage  choisi est Python version 3 (ou supérieure). L’expertise dans tel ou tel langage de programmation n’est cependant pas un objectif de formation.

L'utilisation de *Python* au lycée est retenue ou possible :

- en NSI (Numérique et Science de l'Informatique),
- en maths, en particulier pour la partie algorithmique du programme,
- en SNT, pour les élèves de seconde,
- en sciences physiques, en chime,
- en SVT,
- en SES.

Nous aborderons dans ce cours différents outils.

- La console, pour la découverte de [*Python*](https://www.python.org/ "Site officiel").
- Un éditeur de script, comme [Spyder](https://www.spyder-ide.org/ "Site officiel").
- [*Jupyter*](https://jupyter.org/ "Site officiel"), pour la réalisation de documents.
- [*Matplotlib*](https://matplotlib.org/ "Site officiel"), pour la création de graphiques.
- [*Pandas*](https://pandas.pydata.org/ "Site officiel"), pour l'analyse de données.

## :fa-wifi: Python, en ou hors ligne

Voyons d'abord comment utiliser Python avec une tablette ou un ordinateur, avec ou sans connexion internet.

### Solutions en Ligne

Avec un navigateur et une connexion internet ; il est inutile d'installer un autre logiciel.

- Sans inscription : [ideone](ideone.com "Site officiel"), un outil simple et complet. Idéal pour expérimenter un script, en mode nomade.
- Sans inscription : [Python Tutor](http://pythontutor.com/visualize.html#mode=edit), un outil pour visualiser l'exécution d'un petit script.
- Avec inscription : cocalc.com, un outil puissant et très complet basé sur des logiciels libres. Il permet de stocker ses scripts dans un nuage, et de les lancer depuis toute machine. Un outil utile pour les enseignants qui ont un ordinateur ayant un manque de logiciels.

[RGPD](https://www.cnil.fr/fr/comprendre-le-rgpd "Explication par la CNIL") oblige, on ne peut pas proposer toute solution avec inscription aux élèves. D'autre part, l'utilisation du réseau en classe peut ne pas être garantie.
> **Il vaut mieux donc considérer une solution hors ligne.**

### Solutions hors ligne

Il est nécessaire d'installer un logiciel s'il n'est pas déjà présent. Une connexion à internet n'est plus ensuite requise *normalement* pour l'utiliser.

Les logiciels à avoir sont :

- une version de l'interpréteur Python (le noyau ou *kernel*) ;
- une console (terminal ou *shell*) pour entrer et exécuter des commandes ;
- un éditeur de scripts pour enregistrer des fichiers, à exécuter ;
- et éventuellement un carnet pour rassembler texte et code.

> **La distribution [Anaconda](https://www.anaconda.com/distribution/) propose une solution complète, libre et multiplateforme**. C'est idéal pour débuter et aussi pour aller loin dans l'utilisation scientifique, très loin. Le défaut qu'on lui reproche est d'être parfois trop complète et lourde.

## :fa-android: Python avec une tablette Android

Les lycéens et professeurs de la région disposent d'une tablette.
Parmi les applications disponibles sur le PlayStore :

- [*Termux*](https://play.google.com/store/apps/details?id=com.termux&hl=fr), qui sera minimaliste, pour travailler en console. Sans publicité ;
- [*Pydroid3*](https://play.google.com/store/apps/details?id=ru.iiec.pydroid3&hl=fr), qui sera complète, mais pourra proposer des publicités.

> **Ces deux applications disposent d'un clavier virtuel adapté**,
ce qui permet de taper les symboles courants. Cela reste précaire, et uniquement adapté à de petites créations !

*Jupyter*
:    *Pydroid3* permet aussi d'utiliser *Jupyter*, pour faire tourner des carnets qui auront été préparés plus facilement sur ordinateur, voire sur tablette avec clavier physique.
    > **Attention**, le clavier virtuel de *Jupyter* sur tablette n'est pas pratique du tout. Sans clavier physique, on ne fera que des modifications mineures.

**:fa-check: Conclusion**
La tablette est un outil intéressant :

- pour créer un script simple,
- pour exécuter un code python déjà créé par le professeur,
- pour modifier à la marge un script ou un carnet,
- pour lire un carnet *Jupyter* en ligne avec [mybinder](https://mybinder.org/). Des exemples suivront.

## :fa-laptop: Python avec un ordinateur

La solution complète la plus simple est d'utiliser la distribution [*Anaconda*](https://www.anaconda.com/distribution/ "Site officiel").
Elle offre Python facilement sur les systèmes d'exploitation courants, et de nombreux outils performants, comme :

- [*JupyterLab*](https://jupyter.org/ "Site officiel"), un éditeur de carnets (ou *notebooks*) ; très complet.
- [*Spyder*](https://www.spyder-ide.org/ "Site officiel"), un éditeur de scripts, avec aussi une console Python, un terminal du système d'exploitation, un suivi des variables ; très complet.
- [*Matplotlib*](https://matplotlib.org/ "Site officiel"), pour créer des représentations graphiques.
- [*Pandas*](https://pandas.pydata.org/ "Site officiel") pour l'analyse de données.

<!-- @import "assets/python_environment.png" title="https://xkcd.com/1987/" -->

> Cette image issue d'un comic illustre la pagaille possible à installer de multiples environnements de travail avec Python.

Avant de créer un premier script ou *notebook*, **il faut découvrir un peu la console**. Elle sera toujours utile à la marge.

## :fa-graduation-cap: Apprendre Python

### Un programme d'apprentissage local

Lire à son rythme ces premières parties, en fonction des connaissances de chacun.
Plusieurs lectures rapides sont possibles.

1. [Découverte de Python par la console](Python-Console.html)
   1. Premier lancement
   1. Une calculatrice (entiers, flottants, variables)
   1. Un peu d'anglais utile
   1. Exercices
1. [Création d'un script avec un éditeur](Python-Spyder.html)
   1. Premier lancement
   1. Création et utilisation de fonctions
   1. Premières boucles
   1. Corriger ses erreurs
   1. Structures conditionnelles
   1. Exercices
1. [Écriture d'un carnet avec *Jupyter*](Python-Jupyter-1.html)
*En construction*
   1. Utilisations
   1. Cellules *Markdown*
   1. Premiers graphiques


1. [Écrire des mathématiques avec Jupyter](Python-Jupyter-2.html)
   1. Balises maths
   1. Nombres et les 4 opérations
   1. Calcul littéral
   1. Fractions
   1. Parenthèses
   1. Puissances
   1. Indices
   1. Écriture scripte
   1. Toujours un peu plus loin

1. [Relecture du niveau 1 sur FranceIOI]()
*En construction*
   1. Texte
   1. Boucles `for`
   1. Variables
   1. Lecture
   1. Conditions
   1. Structures avancées
   1. Booléens
   1. Boucles `while`

1. [Relecture du niveau 2 sur FranceIOI]()
*En construction*
    1. Flottans
    1. Tableaux
    1. Chaînes de caractères
    1. Fonctions

1. [Relecture du niveau 3 sur FranceIOI]()
    *En construction*

1. [Des carnets d'exercices avec Jupyter]()
*En construction*
   1. Mathématiques
      1. Le second degré (niveau 1^ère^)
      1. La conjecture de Syracuse (niveau 1^ère^)
      1. Le crible d'Ératosthène (niveau 1^ère^)
      1. Les suites numériques (niveau 1^ère^)
      1. Les nombres de Mersenne
      1. Quelques problèmes issus de [Project Euler](https://projecteuler.net/)
   1. NSI
      1. Les nombres en binaires
      1. Les booléens
      1. Les ensembles
      1. Les dictionnaires
   1. Sciences physiques
   1. Chimie
   1. SVT
   1. Économie
1. [Arithmétique modulaire](https://mybinder.org/v2/gh/FranckCHAMBON/L1-Math-Info---Arith/master?filepath=Sommaire.ipynb) (niveau L1 maths-info ; **avancé**)
    1. Décomposition en facteurs premiers
    1. Divisibilité dans Z
    1. Théorème de Bachet-Bézout
    1. Arithmétique modulaire
    1. Applications simples
    1. TD corrigés et évaluation
    1. [Liste complémentaire de problèmes d'algorithmique](https://www.spoj.com/problems/FRANCKY/) ; *in english*

### Autres programmes d'apprentissage possibles

Chacun ayant ses préférences en termes de style, ou d'éthique, on pourra aussi consulter d'autres références **pour débuter**.

- La [documentation officielle](https://docs.python.org/fr/3/) ; très riche. Parties 1 à 5 du tutoriel.
- Le livre [Apprendre à programmer avec Python3](https://inforef.be/swi/download/apprendre_python3_5.pdf) de Gérard Swinnen. (Chapitres 1 à 7, puis 10).
- Le livre [Une introduction à Python 3](https://perso.limsi.fr/pointal/_media/python:cours:courspython3.pdf) de Bob Cordeau & Laurent Pointal (Chapitres 1 à 5).
- Sur [Zeste de savoir](https://zestedesavoir.com/), [les bases](https://zestedesavoir.com/tutoriels/799/apprendre-a-programmer-avec-python-3/) (3h30) puis [parties avancées](https://zestedesavoir.com/tutoriels/954/notions-de-python-avancees/) (12h).
- Sur [OpenClassRoom](https://openclassrooms.com/fr/) la [partie 1](https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python) du cours sur Python.
- Sur [developpez.com](https://flossmanuals.developpez.com/tutoriels/debuter/initiation-python/), un parmi [d'autres](https://python.developpez.com/cours/).

Ensuite, résoudre des exercices est le plus gros moteur de progrès. On en trouvera sur :

- [France IOI](http://france-ioi.org) ; très adapté aux élèves.
- [Prologin](https://prologin.org/) ; dans un second temps.
- [Project Euler](https://projecteuler.net/) ; en anglais.
- [SPOJ](https://www.spoj.com/) ; en anglais.

Enfin, chacun pourra être autonome pour compléter avec les aspects ou les modules qui l'intéresse le plus. Développement Web, sciences appliquées, algorithmique, mathématiques, ...

Voici une série d'articles récents sur [linuxfr.org](https://linuxfr.org/news/python-pour-la-rentree-2019-partie-1) pour les plus curieux sur Python.

D'autres liens en anglais en cliquant sur l'image suivante :

[![](assets/choix-langage.png)](http://carlcheo.com/startcoding)
