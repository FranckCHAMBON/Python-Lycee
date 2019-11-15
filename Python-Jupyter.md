---
export_on_save:
  html: true
---

![Humans outnumbered by Lego people](assets/minifigs.png "https://xkcd.com/1281/")

# Découverte de Jupyter {ignore=true}

@import "assets/Jupyter.svg" {width="300px" height="200px" title="Logo de Jupyter" alt="logo de Jupyter"}

Jupyter est une solution logicielle qui permet de créer des carnets pour inclure des cellules de code en Python, et des cellules de texte avec une mise en forme la plus simple, grâce à la syntaxe *Markdown*.

Ces carnets sont très utiles et commodes en sciences.
- Pour créer des supports de cours, d'exercices, ou des devoirs, nécessitant la visualisation ou l'exécution de code, ou pas !
- Le rendu est assuré par un navigateur web seul. On peut se passer de tout autre logiciel. Tout élève peut l'utiliser sur n'importe quelle machine ayant un navigateur.
- Pour la vidéoprojection, le format HTML permet un zoom avec la mise en page automatique. On peut aussi imprimer facilement.
- On peut partager en ligne un document, le visualiser, et utiliser du code.

![](assets/jupyexemple.png "Exemple avec Jupyter")

## Sommaire {ignore=true}

[TOC]

## Comment utiliser Jupyter

### Utilisation en ligne

#### Avec *Try Jupyter*

<!-- @import "assets/try-jupyter.png" {width="200px" title="Logo de l'Éducation Nationale" alt="Un logo de Jupyter Lab"}-->


Il est possible d'essayer Jupyter avec une feuille par défaut.
- Aller sur [https://jupyter.org/try](https://jupyter.org/try)
- Choisir **Try JupyterLab**
- Attendre quelques instants
- Une page de démonstration se charge
  - elle est interactive
  - vous pouvez la modifier
  - vous pourrez en faire vous-même bientôt.

#### Avec *GitHub*

<!-- @import "assets/github-logo.png" {width="200px" title="Logo de GitHub" alt="Un logo de GitHub"}-->


Il est possible de sauvegarder en ligne vos carnets Jupyter sur la plateforme [GitHub](https://github.com/), et ainsi de les partager facilement.
- Les carnets sont visibles en statique :
  - ils ne peuvent pas être modifiés sur place,
  - ils ne peuvent pas lancer les bouts de code,
  - ils peuvent seulement être lus, et pointer vers d'autres liens.

#### Avec *My Binder*

<!-- @import "assets/binder.svg" {width="200px"} -->

[Cette solution](https://mybinder.org/) permet de rendre dynamique les carnets stockés sur *GitHub*.

L'exemple proposé par *Try Jupyter* repose sur *Binder*, à vous de créer vos propres carnets pour les mettre en ligne.

### Utiliser Jupyter sur son poste

<!-- @import "assets/anaconda.png" {width="200px" title="Logo d'Anaconda" alt="Un logo d'Anaconda"} -->

- Le moyen le plus simple d'obtenir JupyterLab est de passer par la [distribution Anaconda](https://www.anaconda.com/distribution/).
- Il faut bien suivre [les étapes d'installation](https://docs.anaconda.com/anaconda/).

## Premiers exemples simples.

Voici deux exemples de carnets, un mélange de cours, exercices et codes
- un qui présente [Python comme une calculatrice](TODO)
- un qui présente [???](TODO)


## Découvrir le *Markdown*, avec quelques exemples

### Motivation
Jupyter propose ses zones de texte en [Markdown](https://fr.wikipedia.org/wiki/Markdown) ; ce qui permet une saisie de texte rapide avec une qualité de rendu HTML. En fait, on peut écrire aussi quelques balises HTML lorsque les balises Markdown sont limitées.
> En particulier, pour insérer des images et choisir des attributs, on utilisera la balise html `<img>`.
> Le Markdown est volontairement limité à l'essentiel pour rester simple.

### Liste de tutoriels pour écrire en Markdown :
Suivant votre goût pour l'anglais et votre temps :
* https://www.markdowntutorial.com/ _in english by GitHub_
* [Syntaxe assez complète](https://michelf.ca/projets/php-markdown/syntaxe/)
* [another, in english, by GitHub](http://agea.github.io/tutorial.md/)
* [Un résumé assez succinct](https://github.com/luong-komorebi/Markdown-Tutorial/blob/master/README_fr.md)
* [Élaboration et conversion de documents avec Markdown et Pandoc](https://enacit1.epfl.ch/markdown-pandoc/) ; pour les utilisateurs avancés.

Il ne faut **que 5 minutes pour avoir les bases** suffisantes pour la suite.

On reprend ci-dessous l'essentiel.

### Quelques exemples de mise de style

#### L'emphase faible et forte
L'emphase
: Dans un texte, on a souvent envie de mettre en ***relief*** *certains* **mots**. Il y a plusieurs possibilités : *italique*, **gras**, ~~barré~~, <sup>en haut</sup>, <sub>en bas</sub>, <kbd>cadre</kbd>, `police`, couleur, ou même un mélange. On peut aussi avoir envie de changer le style de tout un groupe de mots que l'on avait identifié. Cela se fait avec une feuille de style en cascade (CSS). Cela permet de faire évoluer la charte graphique d'un document d'un seul coup. C'est une bonne pratique. L'emphase faible sera pour mettre un peu de relief, par défaut c'est en *italique*. L'emphase forte, **par défaut est en gras**. Il est conseillé de limiter au maximum son utilisation hors des titres. L'emphase forte doit rester exceptionnelle, au prix de ne plus avoir d'impact.
```
Du _texte en italique_ entouré de la balise tiret bas *ou* une étoile.
```
> Du _texte en italique_ entouré de la balise tiret bas *ou* une étoile.

```
Du **texte en gras** entouré de la balise double étoile, __ou__ double tiret bas.
```
> Du **texte en gras** entouré de la balise double étoile, __ou__ double tiret bas.

```
**_Un_** exemple _avec_ tous *les* cas *__possibles__*, **fort1** ou __fort2__.
```
> **_Un_** exemple _avec_ tous *les* cas *__possibles__*, **fort1** ou __fort2__.

```
**Un dernier _exemple_** : _une section italique avec un mot en **gras**._
```
> **Un dernier _exemple_** : _une section italique avec un mot en **gras**._

#### Les listes numérotées ou non
```
* On peut faire des listes non numérotées :
    + avec des sous-listes imbriquées ;
    + un autre item ;
    + un dernier pour l'exemple.
* Ou des listes numérotées :
    1. première étape ;
    4. la numérotation est automatique
    2. on peut donc aussi y inclure d'autres listes :
        - un ;
        - deux :
            1. alors ?
            2. facile ?
```

* On peut faire des listes non numérotées :
    + avec des sous-listes imbriquées ;
    + un autre item ;
    + un dernier pour l'exemple.
* Ou des listes numérotées :
    1. première étape ;
    4. la numérotation est automatique
    2. on peut donc aussi y inclure d'autres listes :
        - un ;
        - deux :
            1. alors ?
            2. facile ?


#### Les entêtes, les titres (*header*)
Pour créer l'architecture d'un document, on place des titres de niveaux variés avec autant de `#`.
> L'indentation n'est pas obligatoire ici, c'est juste à titre pédagogique.

```
# Gros titre       (niveau 1)
##  Partie 1       (niveau 2)
###     Section a  (niveau 3)
###     Section b
####        sous section
Un paragraphe...
####        autre sous section
Un autre paragraphe
##  Partie 2
###     Section a
On peut avoir jusqu'à 6 niveaux de titres
```

#### Liens et images
##### insérer un lien direct
```
On peut écrire directement une url,
 exemple avec www.startpage.com un moteur de recherche,
 ou bien https://duckduckgo.com/
```
On peut écrire directement une url,
 exemple avec www.startpage.com un moteur de recherche,
 ou bien https://duckduckgo.com/

##### insérer un lien simple
```
Un lien vers [Qwant](https://www.qwant.com/ "Le seul européen") un moteur de recherche.
```
Un lien vers [Qwant](https://www.qwant.com/ "Le seul européen") un moteur de recherche.

> Noter l'info bulle ; optionnelle.

##### lien dans un titre avec un peu d'emphase
```
###### Un lien vers [*LinuxFr*.org](https://linuxfr.org/) dans un titre
```
###### Un lien vers [*LinuxFr*.org](https://linuxfr.org/) dans un titre
> On peut imbriquer les balises, et donc mettre des liens dans des listes, ou des images dans des liens...

##### insérer une image
Syntaxe :
```
![texte alternatif](source internet ou non)
```
> Pour l'insertion d'images avec plus de réglages, on utilise les balises HTML.

**Exemple :**
```
![logo de Markdown](images/Markdown.svg)
```
![logo de Markdown](images/Markdown.svg)


## Exercice 1 : modifier un carnet déjà créé

[Ouvrir ce carnet](TODO) et suivre les instructions.

## Exercice 2 : la création d'un premier carnet

<!-- @import "assets/notebook-py3.png" {width="200px" title="Notebook Python3" alt="Notebook Python3"} -->

- Lancer JupyterLab
- Créer un nouveau carnet : **Notebook Python 3**
