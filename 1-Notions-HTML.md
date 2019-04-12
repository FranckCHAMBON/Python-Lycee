# Notions sur le langage HTML
[HTML](https://fr.wikipedia.org/wiki/Hypertext_Markup_Language "Article Wikipédia") : _HyperText Markup Language_ ; langage de balisage d'hypertexte.

* C'est le langage qui permet de créer des pages web, le contenu est structuré dans un fichier `.html`
* On peut séparer le fond de la forme en utilisant une feuille de style en cascade (CSS), dans un fichier à part.
* On peut rendre les pages dynamiques par l'utilisation de code en JavaScript, avec des fichiers à part.

> Que retenir du HTML ?
* Du contenu est placé entre balises.
* Ce contenu placé entre balises, est contrôle par le texte de la balise.
* Tout est texte. Description d'images, forme de paragraphes, contenu, lien, ...
* Ceci structure tout le web.
* Le HTML peut être pénible à écrire :
    + Des robots écrivent l'essentiel du code HTML ; il faut programmer ces robots.
    + Le Markdown va simplifier la façon d'écrire le même contenu, écrit par un humain.
    + Il faut au moins comprendre les bases de fonctionnement du HTML.

Exemple :
```html
<!DOCTYPE html PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
 <head>
  <title>
   Exemple de HTML
  </title>
 </head>
 <body>
  Ceci est une phrase avec un <a href="cible.html">hyperlien</a>.
  <p>
   Ceci est un paragraphe où il n’y a pas d’hyperlien.
  </p>
 </body>
</html>
```

Les balises sont de la forme :  
`<nom>` pour une balise ouvrante  
`</nom>` pour une balise fermante

Elles vont presque toujours par paire.
* Il peut y avoir des balises orphelines, comme pour un saut de ligne `<br>` ou `</br>` au choix.
* Les balises peuvent s'imbriquer les unes dans les autres, mais pas se croiser.
    + `<truc> bla <bidule> bla </bidule> bla </truc>` est possible.
    + `<truc> bla <bidule> bla </truc> bla </bidule>` est interdit.




## I] L'emphase
#### Définitions
> Le sens courant du mot [emphase](http://www.cnrtl.fr/definition/emphase "Dictionnaire") est manière exagérée de parler ou d’écrire.

En anglais, il y a deux expressions assez communes :
* _to lay emphasis on_ : mettre l’accent sur
* _to put emphasis_ : insister sur

En français, on utilise aussi des expressions comme :
* mettre en relief,
* souligner,
* faire ressortir,
* attirer l’attention sur,
* mettre en évidence,
* etc.



Afin de démarquer certains mots dans du texte, on peut choisir de les écrire :
* en _italique_
* en **gras**
* en ~~barré~~
* souligné, encadré, en couleur, clignotant, etc

Si on prend comme principe de séparer le fond de la forme, on peut dire que certains mots doivent :
* ne pas se démarquer, avec une écriture normale ; sans emphase
* _se démarquer un peu, on parle d'emphase faible_
* **se démarquer plus, on parle d'emphase forte**

Parlant de la forme, souvent :
* _l'emphase faible est associée à l'italique_
* **l'emphase forte est associée au gras**

Il n'y rien d'obligatoire à cela, et un designer pourrait décider de changer la ligne éditoriale de son site web.
* Le 1 avril, il veut remplacer les mots en italique par des mots écrits en orange.
* À partir de demain, il veut aussi souligner en rouge les mots qui étaient en gras.
* Ces modifications peuvent se faire facilement à l'ensemble d'une page, d'un site web, uniquement en modifiant un peu le fichier CSS.
* C'est le principe de séparation du fond et de la forme.

#### Concrètement en html
```html
Un mot se démarque <em>légèrement</em>, un autre plus <strong>fortement</strong>.
```
> Un mot se démarque <em>légèrement</em>, un autre plus <strong>fortement</strong>.

* `em` est l'abréviation de _emphasis_ ; l'emphase en anglais.
* `strong` signifie **fort** en anglais.

#### En Markdown
Uniquement pour montrer la simplicité.
```markdown
Un mot se démarque _légèrement_, un autre plus **fortement**.
```
> Un mot se démarque _légèrement_, un autre plus **fortement**.


## II] Les listes
#### Définitions
Il y a deux types de listes :

`<ol>  </ol>` pour  ***O**rdered **L**ist* ; liste numérotée

`<ul>  </ul>` pour ***U**nordered **L**ist* ; liste non numérotée

Les listes comportent des items (***L**ist **I**tem*) `<li>  </li>`

Voici deux exemples que l'on peut modifier en ligne.
> **Exercice** : Cliquer sur les liens des exemples, et expérimenter différents niveaux de listes, numérotés ou non.

#### Exemples
[Exemple 1](https://developer.mozilla.org/fr/docs/Web/HTML/Element/ul) liste non numérotée
```html
<ul>
    <li>Milk</li>
    <li>Cheese
        <ul>
            <li>Blue cheese</li>
            <li>Feta</li>
        </ul>
    </li>
</ul>
```
<ul>
    <li>Milk</li>
    <li>Cheese
        <ul>
            <li>Blue cheese</li>
            <li>Feta</li>
        </ul>
    </li>
</ul>

[Exemple 2](https://developer.mozilla.org/fr/docs/Web/HTML/Element/ol) liste numérotée
```html
<ol>
  <li>Mix flour, baking powder, sugar, and salt.</li>
  <li>In another bowl, mix eggs, milk, and oil.</li>
  <li>Stir both mixtures together.</li>
  <li>Fill muffin tray 3/4 full.</li>
  <li>Bake for 20 minutes.</li>
</ol>
```
<ol>
  <li>Mix flour, baking powder, sugar, and salt.</li>
  <li>In another bowl, mix eggs, milk, and oil.</li>
  <li>Stir both mixtures together.</li>
  <li>Fill muffin tray 3/4 full.</li>
  <li>Bake for 20 minutes.</li>
</ol>

#### Concrètement
* L'indentation du code (le décalage) n'est pas obligatoire en HTML, mais conseillée pour la lisibilité.
* En Markdown, l'écriture sera simplifiée, mais l'indentation devra est rigoureusement respectée.




## III] La structuration en parties, sections, sous-sections
#### Définitions
Un document structuré possède :
* un titre, puis
  * des chapitres, qui chacuns contiennent
    * des parties, comportant
      * des sections,
        * des sous-sections...

Afin d'établir un sommaire, ou bien changer le style d'affichage des en-têtes, il faut une balise pour indiquer le type d'en-tête. Il y a 6 niveaux de titre.

`<h1> Titre de niveau 1 </h1>`  
`...`  
`<h6> Titre de niveau 6 </h6>`  

* Le style avec lequel ils sont affichés se règle dans la feuille CSS (une feuille de style en cascade).
  * Par principe, on sépare le fond de la forme.
  * En général, la taille de la police diminue, ainsi que la graisse.
* Certains sont tentés de souligner les titres.
  * C'était la méthode traditionnelle des enseignants sur tableaux noirs pour ajouter de l'emphase aux titres.
  * Sur un document moderne, on considère que cela rompt le gris typographique.

![](https://imgs.xkcd.com/comics/scientific_paper_graph_quality.png)


[Exemple 3](https://developer.mozilla.org/fr/docs/Web/HTML/Element/Heading_Elements)
```html
<h1>Beetles</h1>
    <h2>External morphology</h2>
        <h3>Head</h3>
            <h4>Mouthparts</h4>
        <h3>Thorax</h3>
            <h4>Prothorax</h4>
            <h4>Pterothorax</h4>
```

#### En Markdown
On simplifiera l'écriture de l'exemple précédent en :
```markdown
#  Beetles
##    External morphology
###      Head
####        Mouthparts
###      Thorax
####        Prothorax
####        Pterothorax
```

> **À noter** : `#` est un croisillon, et non un dièse. En anglais, on dit _sharp_ ou _hash_.  
> L'indentation n'est ici pas obligatoire, mais uniquement à but pédagogique.



## IV] Les liens
Donnons immédiatement un exemple, avec [la balise](https://developer.mozilla.org/fr/docs/Web/HTML/Element/a) `<a>` (a pour _anchor_ ; ancre en anglais).

```html
<a href="https://www.w3schools.com/"> Un site pour apprendre le HTML </a>, mais aussi CSS, JavaScript.
```
> <a href="https://www.w3schools.com/"> Un site pour apprendre le HTML </a>, mais aussi CSS, JavaScript.

* Nous ne donnons ici que les bases, le principe de fonctionnement.
* Pour la plupart des balises, on peut ajouter des attributs pour modifier le comportement de la balise.
* Restons simples, et donnons ci-dessous la version en Markdown.

```markdown
[Un site pour apprendre le HTML](https://www.w3schools.com/), mais aussi CSS, JavaScript.
```

## V] Les images
Donnons cette fois le modèle à utiliser, pour la [balise](https://developer.mozilla.org/fr/docs/Web/HTML/Element/img) `<img>`

```html
<img src="votre-source-d-image" alt="un texte alternatif décrivant l'image" />
```

* C'est une balise orpheline, ouvrante et fermante.
* Elle possède ici deux attributs, le premier étant essentiel :
    + `src="..."` pour indiquer le lien vers l'image, qui peut être un lien internet ou local, vers un fichier.
    + `alt="..."` pour donner un texte alternatif, utile :
        - en cas de fichier image absent,
        - pour les déficients visuels qui se font lire par un robot le texte des pages web, dans ce cas les images sont décrites par le texte alternatif uniquement.

#### En Markdown
```markdown
![texte alternatif](lien.image)
```
La syntaxe reprend celle du lien, en le précédent d'un `!`

#### Exemple
Ici l'attribut `width="200px"` indique une largeur (_width_ en anglais) de 200 pixels.  
Le fichier est une image vectorielle SVG stockée dans le répertoire `images`
```html
<img src="images/HTML5_logo.svg" alt="le logo de HTML5" width="200px" />
```
<img src="images/HTML5_logo.svg" alt="le logo de HTML5" width="200px" />

## VI] Conclusions
Dans un premier temps, il est bon de :
* connaître uniquement le principe de base du langage HTML,
* comprendre que le Markdown sera une façon plus rapide et légère d'écrire du contenu web,
* savoir qu'en section Markdown, on peut utiliser certaines balises HTML, en particulier avec plus d'attributs.
