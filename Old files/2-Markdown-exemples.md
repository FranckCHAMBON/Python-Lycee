# Découvrir le Markdown, avec quelques exemples

## Motivation
Jupyter propose ses zones de texte en [Markdown](https://fr.wikipedia.org/wiki/Markdown) ; ce qui permet une saisie de texte rapide avec une qualité de rendu HTML. En fait, on peut écrire aussi quelques balises HTML lorsque les balises Markdown sont limitées.
> En particulier, pour insérer des images et choisir des attributs, on utilisera la balise html `<img>`.

## Liste de tutoriels pour écrire en Markdown :
* https://www.markdowntutorial.com/ _in english by GitHub_
* [Syntaxe assez complète](https://michelf.ca/projets/php-markdown/syntaxe/)
* [another, in english, by GitHub](http://agea.github.io/tutorial.md/)  <===== Il faudrait le traduire TODO work in progress !!!!
* [Un résumé assez succinct](https://github.com/luong-komorebi/Markdown-Tutorial/blob/master/README_fr.md)
* [Élaboration et conversion de documents avec Markdown et Pandoc](https://enacit1.epfl.ch/markdown-pandoc/) ; pour les utilisateurs avancés.

Il ne faut que quelques minutes pour avoir les bases suffisantes pour la suite.

## Quelques exemples
### L'emphase faible et forte
```
Du _texte en italique_ entouré de la balise tiret bas *ou* une étoile.
```
> Du _texte en italique_ entouré de la balise tiret bas *ou* une étoile.

```
Du **texte en gras** entouré de la balise double étoile, __ou__ double tiret.
```
> Du **texte en gras** entouré de la balise double étoile, __ou__ double tiret.

```
**_Un_** exemple _avec_ tous *les* cas *__possibles__*, **fort1** ou __fort2__.
```
> **_Un_** exemple _avec_ tous *les* cas *__possibles__*, **fort1** ou __fort2__.

```
**Un dernier _exemple_** : _une section italique avec un mot en **gras**._
```
> **Un dernier _exemple_** : _une section italique avec un mot en **gras**._

### Les listes
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


### Les entêtes
Pour créer l'architecture d'un document, on place des titres de niveaux variés avec autant de `#`.
> L'indentation n'est pas obligatoire ici, c'est juste à titre pédagogique.

```
# Gros titre
##  Partie 1
###     Section a
###     Section b
####        sous section
Un paragraphe...
####        autre sous section
Un autre paragraphe
##  Partie 2
###     Section a
On peut avoir jusqu'à 6 niveaux de titres
```

### Liens et images
#### lien direct
```
On peut écrire directement une url,
 exemple avec www.startpage.com un moteur de recherche,
 ou bien https://duckduckgo.com/
```
On peut écrire directement une url,
 exemple avec www.startpage.com un moteur de recherche,
 ou bien https://duckduckgo.com/

#### lien simple
```
Un lien vers [Qwant](https://www.qwant.com/ "Le seul européen") un moteur de recherche.
```
Un lien vers [Qwant](https://www.qwant.com/ "Le seul européen") un moteur de recherche.

> Noter l'info bulle ; optionnelle.

#### lien dans un titre avec un peu d'emphase
```
##### Un lien vers [*LinuxFr*.org](https://linuxfr.org/) dans un titre
```
##### Un lien vers [*LinuxFr*.org](https://linuxfr.org/) dans un titre
> On peut imbriquer les balises, et donc mettre des liens dans des listes, ou des images dans des liens...

#### images
**Syntaxe :**  
```
![texte alternatif](source internet ou non)
```
> Pour l'insertion d'images avec plus de réglages, on utilise les balises HTML.

**Exemple :**
```
![logo de Markdown](images/Markdown.svg)
```
![logo de Markdown](images/Markdown.svg)
