---
export_on_save:
  html: true
---

![XKeyboarCD](../assets/xkeyboarcd.png "https://xkcd.com/2150/")

# Découverte d'un éditeur de script {ignore=true}

## Sommaire {ignore=true}

[TOC]

## :fa-edit: Premier lancement d'un éditeur

### Avantages de l'éditeur

- la sauvegarde de scripts,
- les outils d'édition (copier, couper, coller, recherche, sélection),
- la coloration syntaxique du code,
- l'affichage de la liste des variables, leur renommage,
- l'indentation par bloc,
- et d'autres encore en fonction de l'éditeur.

### Éditeurs adaptés à Python

On ne listera ici que des éditeurs libres et multiplateformes, du plus simple au plus élaboré :

- [Thonny](https://thonny.org/) ; basique,
- [Spyder](https://www.spyder-ide.org/) ; inclus dans *anaconda*, **recommandé pour débuter**,
- [Geany](https://geany.org/) ; éditeur **généraliste et simple**, recommandé pour débuter plusieurs langages de programmation,
- [Pyzo](https://pyzo.org/index.html) ; éditeur accompagné de Python et quelques bibliothèques scientifiques,
- [Atom](https://atom.io/ "Site officiel") ; éditeur généraliste moderne, **recommandé pour progresser**,
- [GNU Emacs](https://www.gnu.org/software/emacs/ "Site offciel") ou [Vim](https://www.vim.org/ "Site officel") ; éditeurs modaux et historiques, non conseillés pour débuter,
- [Eclipse+PyDev](http://www.pydev.org/index.html "Site officiel") ; pour les professionnels.


[Visual Studio code - OSS](https://flathub.org/apps/details/com.visualstudio.code.oss "Site officiel de la version libre") est la version libre d'un éditeur populaire ; attention à la télémétrie sur la version compilée de la maison mère... Dans le même genre, Atom est plus clair à ce propos.
[PyCharm](https://www.jetbrains.com/pycharm/) possède une version libre, cependant ...

### Exemple avec *Spyder*

![](../assets/Spyder.png "Logo de Spyder")

*Spyder* est inclus dans *Anaconda*, non sans raisons, nous le présentons ici en particulier, mais tout ce qu'on verra est transposable avec un autre éditeur.

La première ouverture de *Spyder* propose de compléter un fichier `tmp.py` dans un répertoire interne à *Spyder*.

- Commencer par <kbd><b><u>F</u></b>ichier</kbd>$\rightarrow$ <kbd>:fa-save: Enregistrer sous... </kbd>
- Choisir un nom et un répertoire personnel.

Le fichier temporaire proposé contient :

```python {.line-numbers}
# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
```

- Les lignes du fichier sont numérotées ; c'est pratique.
- La ligne 1 indique que l'encodage du fichier est `utf-8` ; c'est un choix moderne qui permet d'écrire sans problème toute lettre accentuée. Cette ligne est inutile sur un système d'exploitation récent, l'[UTF-8](https://fr.wikipedia.org/wiki/UTF-8) étant automatique.
- Les lignes 2 à 6 constituent une chaîne de caractères de 5 lignes. Elle n'est ni affectée à une variable, ni affichée à l'exécution du script ; elle constitue ici un commentaire sur plusieurs lignes.

**print**
: Pour afficher la valeur d'une donnée (si elle existe) pendant l'exécution d'un script on peut utiliser la fonction `print`

>- Recopier le script ci-dessous (avec un copier-coller),
>- le sauver dans un répertoire personnel choisi,
>- anticiper le résultat,
>- et appuyer sur <kbd>F5</kbd> pour faire exécuter le script par la version *Python* proposée.

```python {.line-numbers}
"""
Mon premier script avec Spyder

Affichons des nombres de Mersenne :

    M_n est égal à (2 à la puissance n) moins 1, pour n positif.
    M_n = 2**n - 1
"""

print("M_2 =", 2**2 - 1)
print("M_3 =", 2**3 - 1)
print("M_4 =", 2**4 - 1)
print("M_5 =", 2**5 - 1)
```

On obtient la sortie :

```bash
In [1]: runfile('/home/francky/Documents/Mersenne/mersenne1.py', wdir='/home/francky/Documents/Mersenne')
M_2 = 3
M_3 = 7
M_4 = 15
M_5 = 31
```

- On constate que le commentaire n'a pas été affiché. C'est normal !
- Observer les espaces et l'absence de virgule autour de `=` dans l'affichage. Normal !
- *Spyder* affiche le nom complet du fichier qui a été interprété (*run file*),
- ainsi que le répertoire de travail (`wdir` pour <b>w</b>orking <b>dir</b>ectory).

## :fa-cogs: Les fonctions

### La fonction `print`

- prend en argument zéro, un ou plusieurs paramètres, **mis entre parenthèses**,
- affiche les valeurs de ces paramètres en les **séparant par une espace**, puis **termine par un saut de ligne**,
- (et elle renvoie `None`).

> Oui, en typographie, espace est féminin.

Des exemples simples d'utilisation :

```python {.line-numbers cmd="python3" output="text"}
print("Hello World!") # Une tradition.
print()               # N'affiche rien, mais saute une ligne.
n = 42                # Une affectation.
print("La réponse à la question universelle est", n)
print(1, 10*n+1, "texte", 3.14, 12345e100)
```

> **Remarque** : `print` était un mot réservé avec Python2, c'est désormais une fonction comme les autres !

### La fonction `round`, avec un seul paramètre

> `round(nbr)`

- prend en argument un nombre `nbr` de type entier ou flottant,
- retourne un nombre de **type entier**, le plus proche de `nbr`,
- en cas d'égalité, retourne l'entier **pair** ; *cf* les trois derniers exemples.

```python {.line-numbers cmd="python3" output="text"}
for x in [3.14, 2.718, 3.5, 4.5, -4.5]:
    print("L'arrondi de", x, "est", round(x))
```

> On vient de voir, au passage, comment répéter une instruction avec une variable qui prend des valeurs successives. Nous y reviendrons.

### La fonction `round`, avec deux paramètres

> `round(nbr, d)`

- prend en argument un nombre `nbr` entier ou flottant, et un entier `d`
- retourne un nombre **de même type** que `nbr`, l'arrondi de `nbr` à $10^{-d}$ près.

```python {.line-numbers cmd="python3" output="text"}
for x, d in [(3.14, 1), (2.718, 2), (3.5, 2), (4, 2), (12345, -2), (12345.0, -2), (9.8765e100, 2-100)]:
    print(f"L'arrondi de {x} à 10^{-d} près est {round(x, d)}")
```

> On vient de voir, au passage, une une *f-string* pour afficher du texte et des valeurs. Nous y reviendrons.

> **:fa-bolt: Attention** : [le comportement avec les flottants](https://docs.python.org/fr/3/library/functions.html#round) peut être curieux, mais c'est normal ! Les flottants ne sont pas les décimaux !
> On a constaté également que le comportement de `round` est différent en fonction du nombre de paramètres.

### Fonctions directement accessibles, ou natives

Dans la [liste de la documentation officielle](https://docs.python.org/fr/3/library/functions.html) des fonctions natives, nous avons déjà croisé :

- `print` : pour l'affichage de valeurs de données (nombre, texte, ou ...),
- `round` : pour l'arrondi de nombres,
- `type` : pour retourner le type d'un objet.

Objet
: Avec Python, **tout est objet** : les nombres, les collections (ensembles, listes, dictionnaires, ...), les fonctions, les modules, tout ce qui existe et tout ce que vous allez créer. **Tout est objet**.

Concentrons-nous sur les fonctions liées au type d'un objet.

- `int` : Transforme un objet, si possible, en entier.
- `float` : Transforme un objet, si possible, en flottant.
- `bool` : Transforme un objet, si possible, en booléen.
- `complex` : Transforme un objet, si possible, en nombre complexe.
- `str` : Transforme un objet, si possible, en chaîne de caractères.
- `list` : Transforme un objet, si possible, en liste.
- `tuple` : Transforme un objet, si possible, en tuple.
- `set` : Transforme un objet, si possible, en ensemble.
- `dict` : Crée un nouveau dictionnaire.

Type
: Tout objet possède un type. Nous avons déjà croisé certains de ces types de base : (`int`, `float`, `bool`).

Présentons rapidement les autres fonctions natives liées au type.

- `complex` : Pour les nombres **complex**es, que l'on étudie en terminale (maths expertes et certaines sections scientifiques).
- `str` : Pour les chaînes de caractères (_**str**ing_), du texte. Une fois créée on ne peut pas la modifier. En français, on dit **immuable** (*immutable* en anglais).
- `list` : Pour une **list**e ordonnée d'objets. On peut ajouter des objets, en enlever, et de manière générale la modifier. En français, on dit **muable** (*mutable* en anglais).
- `tuple` : Ressemble à `list`, mais en version immuable.
- `set` : Pour un ensemble. Non ordonné. Sans doublon. Muable. On peut ajouter, enlever un objet. On peut faire des intersections, unions.
- `dict` : Pour créer un dictionnaire associatif. À un élément d'un ensemble (les **clés**), on associe une donnée (les **valeurs**).

Nous reviendrons sur ces types de données. En particulier sur la distinction muable-immuable et le lien direct avec les dictionnaires.

Pour une présentation complète des [modèles de données](https://docs.python.org/fr/3/reference/datamodel.html?highlight=mutable).

### Fonctions et constantes du module math

Dans le module `math`, il y a, par exemple :

- `sqrt` : La fonction racine carrée (_**sq**uare_ _**r**oo**t**_)
- `cos`, `sin`, `tan` : Les fonctions cosinus, sinus, tangente, pour un angle en radian ; un flottant. Les réciproques `acos`, `asin`, `atan`.
- `exp`, `log` : Les fonctions exponentielle et logarithme népérien, pour un flottant.
- `pi`, `e` : Les flottants approximations des constantes $\pi$, et $\textrm{e}$.

Pour utiliser ces objets, il y a deux méthodes.

On peut importer un choix d'objets, prêts à être utilisés directement.

```python {.line-numbers cmd="python3" output="text"}
from math import sqrt, cos, exp, pi
print(sqrt(2))
print(cos(2019 * pi))
print(exp(666))
```

Ou bien, on importe le module entier et chaque objet est accessible via un appel référencé.

```python {.line-numbers cmd="python3" output="text"}
import math
print(math.sqrt(2))
print(math.cos(2019 * math.pi))
print(math.exp(666))
```

Ici, [la liste complète des objets du module `math`](https://docs.python.org/fr/3/library/math.html).

> :fa-bolt: **Attention**
> Il ne faut pas utiliser `from math import *` comme l'on voit trop souvent. Cela importe tout le module `math`, et écrase la fonction `pow` qui existait avant par une nouvelle qui est moins puissante en arithmétique.
> **On n'importe que ce dont on a réellement besoin**.

### Fonctions créées par l'utilisateur

L'utilisateur possède deux façons de créer des fonctions.

#### Constructeur `lambda`

C'est la méthode la plus rapide pour construire une fonction.
Ici on construit et on utilise la fonction $x\mapsto (x+5)(x-5)$.

```python {.line-numbers cmd="python3" output="text"}
ma_fonction = lambda x: (x+5) * (x-5)
print(ma_fonction(15))
print(ma_fonction(6125.7))
```
> On constate encore que les flottans **ne sont pas** les décimaux.
> On constate aussi, ici, que notre fonction traite aussi bien un flottant qu'un entier, une seule définition suffit. Ce n'est pas possible facilement avec d'autres langages, voire interdit. C'est une caractéristique du langage *Python* qui en facilite l'utilisation, mais qui, parfois, peut conduire à l'écriture de code difficilement debuggable.

#### Constructeur `def`

C'est la méthode la plus utilisée pour construire une fonction.

Pour recréer la même fonction :

```python {.line-numbers cmd="python3" output="text"}
def ma_fonction(x):
    return (x+5) * (x-5)

print(ma_fonction(15))
print(ma_fonction(6125.7))
```

Cette seconde méthode est adaptée pour les fonctions dont le corps est conséquent ; plusieurs lignes. Alors que `lambda` est adapté pour les fonctions courtes à définir.

> :fa-bolt: **Attention**.
>
> - Il ne faut pas oublier les deux points à la fin de la ligne de `def`.
> - Chaque ligne de la définition de la fonction doit être **indentée** ; l'ensemble forme un bloc décalé vers la droite d'un même nombre d'espaces. **4 espaces de préférence**, c'est une règle.
> - Il peut y avoir zéro, un ou plusieurs paramètres.
> - Il peut y avoir zéro, une ~(ou~ ~plusieurs)~ instruction~s~ qui commence~nt~ par `return` ; l'expression qui suit le premier `return` rencontré est retourné, l'exécution de la fonction s'arrête. Sans expression après le `return`, ou bien en fin de fonction, `None` est retourné.

Exemple 1

```python {.line-numbers cmd="python3" output="text"}
def aire_rectangle(largeur, longueur):
    "Calcule l'aire d'un rectangle de côté largeur et longueur"
    print("Les côtés du rectangle sont", largeur, "et", longueur)
    return largeur * longueur

print("L'aire est", aire_rectangle(8, 13))
```

> **Remarques**
>
> La fonction `aire_rectangle` :
>
> - requiert deux paramètres obligatoires,
> - possède une `docstring` (ligne 2); un texte d'aide,
> - affiche une information sur les côtés du rectangle,
> - puis retourne une valeur calculée.

Exemple 2

```python {.line-numbers cmd="python3" output="text"}
def ne_fait_rien():
    "Cette fonction ne fait rien !"
    pass

print(ne_fait_rien())
print()
help(ne_fait_rien)
```

> **Remarques**
>
> La fonction `ne_fait_rien` :
>
>- est fidèle à son nom,
>- possède une `docstring`, (c'est une bonne pratique)
>- retourne `None` in fine ; il n'y a pas de `return`
>
> La ligne 5, affiche le retour de cette fonction, c'est la raison du `None`
> Le `print` à la ligne 6 n'affiche rien, mais saute à la ligne.
> La ligne 7 affiche de l'aide sur la fonction `ne_fait_rien`, une aide que nous avions préparée !

#### L'aide sur les fonctions avec `help`

Nous venons de voir que l'on peut créer une fonction auto-documentée avec sa `docstring`. Toutes les fonctions natives de Python le sont.

- L'aide n'est pas utilisée en général dans un programme.
- L'aide est généralement appelée depuis une console ou un terminal.

```python
In [1]: import math

In [2]: help(math.exp)
Help on built-in function factorial in module math:

factorial(x, /)
    Find x!.

    Raise a ValueError if x is negative or non-integral.

In [3]:
```

> :fa-bolt: **Attention**
>
> - Avec *Spyder* l'aide est affichée en console, c'est facile ! **Une raison de plus de préférer _Spyder_ pour débuter.**
> - Avec un terminal classique, l'aide est affichée dans un éditeur annexe. Pour en sortir, il faut taper sur `q` (comme *quit*) ; et ce n'est pas indiqué ; c'est moins pratique !
> - En cas de doute sur l'utilisation d'une fonction, c'est une bonne pratique que de vérifier avec `help`.

### :fa-key: Utilisation de ses propres fonctions en console

Le programme dans le B.O. mentionne explicitement le fait de créer des fonctions dans des fichiers, et de les appeler depuis la console. A priori dans un souci d'éviter les soucis de `int(input())` et de limiter les `print`. Travailler avec *Jupyter* sera très adapté à cette préoccupation. Restons donc avec *Spyder* encore un peu.

1. Écrire une fonction `mersenne` dans un script,

    - qui prend un argument $n$ de type entier,
    - qui possède une `docstring`,
    - qui renvoie le $n$^ième^ nombre de Mersenne $2^n-1$.

2. Enregistrer ce script dans un fichier `outils.py`, par exemple ; l'extension `.py` est obligatoire.

3. Dans la console, entrer les instructions successives :

    - `from outils import mersenne`
    - `mersenne(2)`
    - `mersenne(3)`
    - `mersenne(5)`
    - `mersenne(7)`
    - `mersenne(11)`

On remarque que les quatre premiers résultats sont des nombres premiers : $3$, $7$, $31$ et $127$. Par contre, $2047 = 23\times89$, ne l'est pas !

4. Dans le fichier `outils.py` ajouter les lignes suivantes.

```python {.line-numbers}
for p in [2, 3, 5, 7, 11]:
    print("Le nombre de Mersenne", p, "est", mersenne(p))

if mersenne(11) % 23 == 0:
    print("mersenne(11) n'est pas un nombre premier, en effet il est ...")

if mersenne(11) == "23×89":
    print("Pourquoi ce texte ne s'affiche-t-il pas à l'exécution ?")
```

> :fa-bolt: **Remarques**
>
> - À la ligne 1 de l'ajout, on fait une boucle sur la liste des nombres premiers jusqu'à 11.
>   - Noter le `:` en fin de ligne 1,
>   - et l'indentation ligne suivante.
> - Le `if` entame une structure conditionnelle.
>   - Noter le `:` en fin de ligne 4.
>   - et l'indentation ligne suivante.
> - On rappelle que `%` est l'opérateur modulo, qui donne le reste dans une division entière.

5. Interpréter le test qui est fait ligne 4.
6. Compléter le texte à la fin de la ligne 5.
7. Exécuter votre script en appuyant sur <kbd>F5</kbd>. La sortie devrait apparaître dans la console (sauf si vous avez changé les paramètres de *Spyder*).
8. Expliquer les lignes 7 et 8.

> **Conclusion**
>
>- On vient de découvrir comment faire un test, une structure conditionnelle.
>
>- On vient aussi de découvrir comment répéter plusieurs actions, en itérant sur une liste, nous allons aussi l'apprendre en faisant une boucle tant qu'une condition est respectée.
>
> C'est la base de l'algorithmique. On crée des architectures d'instructions séquentielles, dont le flot d'exécution peut dépendre des résultats précédents. Ensuite, on peut étudier d'autres paradigmes de programmation : programmation orientée objet, en particulier.

## :fa-undo: Premières itérations, et boucles

### Avec une liste ou une chaîne de caractère

Le type `list`
: Une liste est un objet de type `list`, elle possède zéro, un ou plusieurs éléments ; la liste est **ordonnée**, on peut la modifier (elle est **muable** ou *mutable*). Les éléments ne sont pas nécessairement du même type ; mais ce n'est pas conseillé.

Le type `str`
: Une chaîne de caractères est un objet de type `str` (pour *<b>str</b>ing*), elle possède zéro, un ou plusieurs caractères, elle est **ordonnée**, on ne peut pas la modifier (elle est **immuable** ou *immutable*). Les caractères ne sont pas seulement [ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange) (un jeu limité de 127 caractères), mais [UTF-8](https://fr.wikipedia.org/wiki/UTF-8) donc universel. Une chaîne est immuable, cependant on peut créer une nouvelle chaîne à partir d'une autre.

Exemples à tester dans la console de *Spyder* :

```python
lst_vide = []  # une liste vide
eps = ""       # un mot vide
mot = "test"   # un mot ; 'test'
a = [mot]      # une liste contenant un objet : une chaîne `str`
b = ["test"]   # une autre liste, de même contenu !
lnp = [2, 3, 5, 7, 11]   # une liste de 5 éléments, les nombres premiers jusqu'à 11
lettres_de_bonjour = list("bonjour")
print(lettres_de_bonjour)
un_mélange = ['X270', 8, 4, 3.0] # mauvaises pratiques :
#  - accent à la variable,
#  - les types des éléments de la liste sont différents.
print(type(lnp)) # affiche le type de lnp
print(len(lnp))  # affiche la longueur de lnp
print(lnp[0])    # affiche l'élément lnp d'index 0
```

#### Points communs entre `list` et `str`

Avec `truc` qui est de type `list` ou de type `str`.

- `len(truc)` renvoie le nombre d'objets ou de caractères de `truc`. On le note $l$ ensuite. L'identifiant `len` vient de *<b>len</b>gth*, longueur en anglais.
- Les éléments de `truc` sont indexés de $0$ à $l-1$. **Il est très commode** de dire indexés de $0$ inclus à $l$ exclu.
- Si $l\neq0$, `truc[0]` est le premier élément,
- et `truc[l-1]` est le dernier élément,
- sinon ni `truc[0]` ni `truc[l-1]` n'existe.
- On peut itérer (comme dans la question 4 de l'exercice précédent).
  - `for bidule in truc: faire_avec(bidule)`
- On peut faire de la [concaténation](https://fr.wikipedia.org/wiki/Concat%C3%A9nation), ou concaténer. On a :
  - `"bon" + "jour" == "bonjour"`
  - `[2, 3, 5, 7] + [11] == [2, 3, 5, 7, 11]`
- On peut multiplier `truc` par un entier :
  - `"gla" * 3 == "glaglagla"`
  - `[0] * 10 == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]`
  - Ceci est utile pour initialiser une longue liste pleine de zéros.
- On peut utiliser l'ordre lexicographique (celui du dictionnaire) pour faire des tests.
Les exemples suivants sont évalués à `True` :
    - `"balle" < "bar"`
    - `[2, 3, 5, 7, 11] >= [2, 3, 4, 5, 6, 7]`
- On peut obtenir la copie d'une tranche (*slice*) de `truc` avec `truc[i:j]` du i^ème^ élément inclus, jusqu'au j^ème^ exclu.
Cette copie de tranche aura $j-i$ éléments, **c'est pratique** !
    - `lnp = [2, 3, 5, 7, 11, 13, 17]` ; une liste
    - `lnp[2:5] == [5, 7, 11]` ; de 5 inclus, jusqu'à 13 exclu.
    - `mot = "aimer"` ; une chaîne qui est un verbe.
    - `mot[0:3] == "aim"` ; l'extraction de son radical.

> **Remarque 1** : On peut donner des indices négatifs. Comme si la liste ou la chaîne était refermée sur un cercle, avant l'indice $0$, on a l'indice $-1$ qui correspond au dernier élément de `truc`.
Ainsi `truc[i]` est défini pour `i` allant de $-l$ inclus à $+l$ exclu.

```python
truc[l-1] == truc[-1]
truc[l-2] == truc[-2]
truc[1] == truc[-l+1]
truc[0] == truc[-l]
```

> **Remarque 2** : Ceci est valable aussi pour les tranches, on peut définir `truc[i:j]` avec `i` et `j` dans l'intervalle de $-l$ inclus à $+l$ exclu.

:fa-key: Expérimenter les différents cas où `i` et `j` sont de même signe ou non !

> **Remarque 3** : Pour les copies de tranches, on peut aussi ne pas spécifier `i` ou `j`.
> Avec `i` et `j` positifs :
> - `truc[:j]` correspond aux `j` premiers éléments d'une copie de `truc`.
> - `truc[i:]` correspond à une copie de tout `truc` sauf ses `i` premiers éléments.
> - `truc[:]` correspond à une copie de tout `truc`.

:fa-key: De même, traduire ce que réalisent les expressions suivantes avec `i` et `j` positifs :
- `truc[:-j]`
- `truc[-i:]`

> **Remarque 4** : Pour les copies de tranches, on peut aussi spécifier un pas `k`.
> `truc[i:j:k]` correspond à une copie des éléments de `truc` de l'index `i` inclus à l'index `j` exclu, par pas de `k`.
> Par exemple :
> - `truc[5:17:5]` donnera les éléments d'index 5, 10 et 15 de `truc`
> - `truc[11:20:3]` donnera les éléments d'index 11, 14 et 17 de `truc`, mais pas le 20.

:fa-key: Donner des écritures de tranches pour avoir une copie :
1. De tous éléments d'index pair de `truc`
2. De tous éléments d'index impair de `truc`
3. De tous les éléments de `truc`, mais rangés dans l'ordre inverse.
    - Aide : le pas peut être négatif.

#### :fa-key: Conjugaisons
1. Choisir un modèle de conjugaison de verbe. (Exemple : le verbe aimer)
2. Choisir un temps et un mode. (Exemple : le présent de l'indicatif)
3. Créer une fonction `ma_conjuguaison`
   - qui prend en paramètre `verbe` de type `str`,
   - qui s'auto-documente,
   - qui teste si `verbe` est bien un verbe qui correspond à votre modèle,
   - qui extrait le radical du verbe et l'affecte à la variable `radical`
   - qui conjugue `verbe` à votre temps et mode.
   - qui gère les cas où `verbe` commence par une voyelle ou non.


#### Différences entre `list` et `str`

La différence évidente entre `list` et `str` est que les éléments d'un objet de type `str` sont tous des caractères, alors que pour `list` on peut avoir **tout** type d'élément.

Mais la différence essentielle étant l'aspect muable de `list` et immuable de `str`. Cela n'empêche en aucun cas de construire de nouvelles chaînes à partir d'anciennes.

Exemples d'utilisations classiques :

```python {.line-numbers cmd="python3" output="text"}
truc = [0] * 5        # initialisation de 5 valeurs nulles
truc.append(4)        # on ajoute une valeur 4 à truc qui devient de longueur 6
truc[0] = 1           # on modifie truc[0]
truc[3] = truc[0] * 2 # on utilise truc[0] pour modifier truc[3]
print(truc)
maFonction = lambda x: x*x + 100
for x in truc:
    print(x, maFonction(x))
```

```python {.line-numbers cmd="python3" output="text"}
verbe = "manger" # un verbe du premier groupe
l = len(verbe)
radical = verbe[0:l-2]  # du début à la fin sauf les deux derniers
print("Je", radical+"e")
print("Tu", radical+"es")
pass # à vous de compléter...
print("Ils", radical+"ent")
```

### Avec un itérateur de type `range`

Le type `range`
: un objet de type `range` permet essentiellement d'itérer sur une liste d'entiers, en progression arithmétique, sans avoir à créer cette liste entièrement à l'avance.

Exemples à tester dans la console de *Spyder* :

```python {.line-numbers}
for une_variable in range(100):
    print("Cette punition est trop simple.")
```

```python {.line-numbers}
for ma_variable in range(10):
    print(ma_variable)
    # pour afficher ma_variable valant de 0 inclus à 10 exclu
```

```python {.line-numbers}
un_range = range(10)
print("un_range", un_range)
print("Bizarre ?")
ma_liste = list(un_range)
print("ma_liste", ma_liste)
```

```python {.line-numbers}
for ma_variable in range(100, 200, 20):
    print(ma_variable)
    # range s'écrit aussi avec deux ou trois paramètres, comme pour une tranche
```

```python {.line-numbers}
for ma_variable in range(20, -1, -1):
    print(ma_variable)
    # Anticiper le résultat avant de lancer le code !
```


### :fa-key: Obtenir et utiliser un tableau de valeurs d'une fonction

On considère la fonction numérique $f$ définie sur $\mathbb R$ par
> $x\mapsto f(x) = -0.3x^2 + 1.2x + 6.0$

1. Avec *Spyder*, créer un fichier `tableau_de_valeurs.py`
2. Afficher tous les nombres de $0.0$ inclus à $10.0$ exclu, par pas de $0.1$
3. Créer en Python, la fonction $f$ notée ensuite `f`.
4. Ajouter le code suivant pour afficher certaines valeurs

```python  {.line-numbers}
for x in [0.0, 1.7, 2.6, 3.1]:
    print("Pour x =", x, "   , on a f(x) =", f(x))
```

5. Exécuter votre code et l'analyser.
6. Modifier votre code pour afficher les valeurs $x$ et $f(x)$ pour $x$ allant de $0.0$ inclus à $10.0$ exclu, par pas de $0.1$.
7. Créer une fonction `tableau_de_valeurs` qui reçoit en paramètres :
   - une fonction `f` ; oui c'est possible
   - un nombre `a` ;
   - un nombre `b` ;
   - un entier `n` .
8. Compléter votre fonction pour qu'elle affiche $x$ et $f(x)$ pour $x$ allant de $a$ inclus à $b$ inclus, avec $n$ valeurs régulièrement espacées.
9. Tester et documenter votre fonction.

## :fa-bug: Apprendre à lire les erreurs

Lorsqu'on lance un script, il peut arriver une erreur.
- Le programme stoppe alors son exécution, et affiche un message.
- **Il faut lire ce message.**
  - La ligne est indiquée. Attention, cela peut être une parenthèse manquante à la ligne précédente !!!
  - Le type d'erreur est indiquée. En voici quelques-uns classiques, lorsqu'on débute.

### IndentationError

`IndentationError: expected an indented block`

Il s'agit d'une erreur d'indentation, Python attend un bloc indenté.
- L'indentation peut être faite avec des tabulations ou des espaces,
- La PEP-8 recommande d'utiliser 4 espaces.
- Un bon éditeur propose d'afficher les espaces et les guides d'indentation, cela aide beaucoup !

### SyntaxError

`SyntaxError: invalid syntax`

Il s'agit d'une erreur de syntaxe, un petit curseur pointe l'endroit où Python l'a trouvé.
Attention, cela peut venir du mot précédent !!!

### IndexError

`IndexError: list/string index out of range`

L'index pour votre chaîne ou liste est en dehors de l'intervalle. Erreur classique, si une liste `L` possède 10 éléments, alors `L[10]` provoque une erreur. `L[9]` est le dernier élément.

### NameError

`NameError: name 'favtorial' is not defined`

Probablement une erreur de frappe, l'identifiant est inconnu.
Ici, un v changé en c donne `factorial` qui semble plausible.

> **Conseil** : Avec *Spyder*, activer l'explorateur de variables et vérifier qu'il n'y a pas deux variables avec presque le même nom alors que ce n'est pas prévu. D'autre part, choisir des noms de variables longs et facilement distinguables sera très utile.

## :fa-key: Nombre d'écritures d'un entier comme une somme

Le nombre 4 peur s'écrire de 7 manières comme une somme d'entiers naturels non nuls.

- $4 = 1+2+1$
- $4 = 2+2$
- $4 = 1+1+2$
- $4 = 2+1+1$
- $4 = 1+3$
- $4 = 1+1+1+1$
- $4 = 3+1$

1. De combien de manières le nombre 10 peut-il s'écrire comme une somme d'entiers naturels non nuls ?
Faire un programme qui les affiche toutes.
2. :fa-shield: Sans tenir compte de l'ordre de la somme. $1+3$ et $3+1$ comptent pour la même somme.
4 possède alors 4 manières de s'écrire comme somme.
Combien y a-t-il de manières pour écrire 10 comme une somme ?

- $4 = 1+2+1$
- $4 = 2+2$
- $4 = 1+1+1+1$
- $4 = 3+1$

## :fa-question-circle: Structures conditionnelles

### Un premier exemple

```python {.line-numbers cmd="python3" output="text"}
def mersenne(p):
    "retourne le nombre de Mersenne p"
    return 2**p - 1

def test_divisible(n, k):
    "n est-il divisible par k ?"
    if n%k == 0:
        return True
    else:
        return False

m_5 = mersenne(5)
if 7*7 < m_5:
    print("TEST1 : 49 est inférieur à m_5")

m_11 = mersenne(11)
if test_divisible(m_11, 23):
    print("TEST2 : Confirmation, mersenne(11) n'est pas un nombre premier")
```

Explications :
- Lignes 1 à 3, on définit la fonction `mersenne` : $p\mapsto 2^p-1$
  - On l'a déjà vu précédemment, et on va s'en servir encore...
- Lignes 5 à 9, on définit une fonction `test_divisible`
  - on rappelle que `n%k` retourne le reste dans la division entière de `n` par `k`
  - si `n%k == 0`, cela signifie que la division tombe juste, et que `n` est divisible par`k`
- On remarque que le TEST1 ne s'affiche pas. (Rappel $M_5 = 31$)
  - En effet, `49 < 31` est faux, donc l'instruction ligne 14 n'est pas interprétée.
- On remarque que le TEST2 s'affiche. (Rappel $M_{11} = 2047$)
  - En effet, on a déjà vu que $2047 = 23\times89$
- Ligne 9: `else` signifie **sinon**.

### Définition complète

Les mots clés sont :

- `if` pour **si**, pour initier la structure conditionnelle.
- `else` pour **sinon**, pour la clore. *Partie facultative.*
- `elif` une contraction de `else: if`, pour **sinon si**
  - on peut inclure zéro, une ou plusieurs parties `elif`

La structure est donc :

`if` *{une condition}* `:`
: *{un bloc d'instructions}*

`elif` *{une condition}* `:`
: *{un bloc d'instructions}*

`elif` *{une condition}* `:`
: *{un bloc d'instructions}*

`else:`
: *{un bloc d'instructions}*

:fa-bolt: Remarques importantes :

- Ne pas oublier les deux points `:` après les conditions.
  - L'oublie de `:` provoque `SyntaxError`.
- On a déjà vu l'indentation pour la définition des fonctions, et dans les boucles.
  - chaque bloc doit être indenté,
    - une mauvaise indentation provoque `IndentationError`
  - chaque bloc doit contenir :
    - une ou plusieurs instructions,
    - comme des boucles ou d'autres structures conditionnelles,
      - dans ce cas, les sous parties sont indentées en conséquences.
    - pour mettre une instruction qui ne fait rien, on utilise `pass`

## :fa-key: Les diviseurs d'un entier

```python
def diviseurs(n):
    "à modifier"
    pass

def est_premier(n):
    "à modifier"
    pass
```

1. Compléter le code ci-dessus et l'inclure dans votre fichier `outils.py`
  1. La fonctions `diviseurs` doit retourner la liste des diviseurs de l'entier `n`
  2. La fonction `est_premier` doit retourner un booléen, sur la primalité ou non de `n`
2. Effectuer les tests suivants dans un nouveau fichier `test_outils.py` du même répertoire que `outils.py`.

```python {.line-numbers cmd="python3" output=txt}
from outils import *

# Test 1
premiers_jusqu_32 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for n in range(32):
    assert est_premier(n) == (n in premiers_jusqu_32), f"Échec du test 1 pour n = {n}"
print("Test 1 réussi.")

# Test 2
message_erreur_test2 = "Votre méthode ne trouve pas 25 nombres premiers inférieurs à 100 !"
premiers_jusqu_100 = [p for p in range(100) if est_premier(p)]
assert len(premiers_jusqu_100) == 25, message_erreur_test2
print("Test 2 réussi.")
```

**Si votre programme met trop de temps à finir un test, on peut l'arrêter avec** <kbd>Ctrl</kbd>+<kbd>C</kbd>

:fa-bolt: **Remarques**
- Ligne 1 : On importe nos fonctions créées.
- Ligne 4 : On utilise des valeurs connues, codées en dur (*hardcoded*) pour le test 1
- Lignes 6 et 12 `assert` permet de faire le test d'une condition.
  - Si la condition est vraie, le script se poursuit normalement,
  - sinon le script est interrompu, et l'objet suivant est affiché.
- Ligne 11 : Nous reverrons cette façon de construire une [liste *en compréhension*](https://fr.wikipedia.org/wiki/Liste_en_compr%C3%A9hension).
   - **C'est au programme de mathématiques en première**.
- Lignes 6 : `in` fait un test d'appartenance,
  - il retourne un booléen ...
  - qui est comparé à celui retourné par `est_premier(...)`
  - :fa-bolt: **ce n'est pas du tout le même** que le `in` aux lignes 5 et 11 !

> C'est une bonne pratique de tester (ou faire tester) ses programmes.
>   - Un professeur ne pourra pas toujours corriger votre code.
>   - Apprendre à fabriquer ses propres tests est une source de progrès.
>   - Il existe de nombreux outils en ligne pour tester automatiquement du code.
