---
export_on_save:
  html: true
---

<!-- @import "../assets/python-java.jpg" title="Extrait de https://twitter.com/martinrenaud/status/511606415837110272" -->

# Découverte de Python en console {ignore=true}

## Sommaire {ignore=true}

[TOC]

:fa-key: désigne un exercice.
:fa-shield: désigne une question plus difficile.

## :fa-terminal: Premier lancement

### :fa-linux: Avec GNU/Linux

On ouvre un terminal (ou une console), avec <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>, ou bien en cliquant sur une icône (souvent noire), qui peut ressembler à <kbd>:fa-terminal:</kbd> ou <kbd> $_ </kbd>.

![Un terminal bash](../assets/terminal.png)

On obtient alors une invite de commande `bash` qui finit par `~$ `, dans laquelle on tape `python3` (ou simplement `python` dans les distributions modernes). La version 3 ou supérieure est la version des programmes de l'Éducation Nationale.

On obtient le numéro de la version prête à être utilisée, et une invite de commande python `>>>`. Ci-dessous, on a un exemple où Python 3.7.4 est prêt à interpréter des instructions.

```bash
(base) francky@X270:~$ python
Python 3.7.5 (default, Oct 25 2019, 15:51:11)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

En guise de premier calcul, on peut tester :

```python
>>> pow(2, 82_589_933, 10_000_000_000) - 1
5217902591
```

Il s'agit du calcul des dix derniers chiffres du [plus grand nombre premier connu](https://fr.wikipedia.org/wiki/Plus_grand_nombre_premier_connu) à la fin de l'année 2018.

Ou alors un calcul plus simple :

```python
>>> 2 + 2
4
```

> **Pour quitter une console**
>
>- On appuie sur <kbd>Ctrl</kbd>+<kbd>D</kbd> pour quitter la console python,
>- et encore une fois <kbd>Ctrl</kbd>+<kbd>D</kbd> pour quitter le terminal.
>
>> Il s'agit d'envoyer le caractère EOF (*End Of File*)

On pourra aussi avantageusement utiliser *Spyder* qui dispose également d'une console.

### :fa-android: Avec une tablette Android

On lance l'application [*Termux*](https://play.google.com/store/apps/details?id=com.termux&hl=fr). On obtient également une invite de commande `bash`, comme sous Linux. Si on entre `python` la première fois, il indique comment l'installer.

```bash
$ python
(...please type...)
pkg install python
```

Il faut donc entrer à la suite la commande `pkg install python`

```bash
$ pkg install python
```

À la fin de l'installation, on peut alors lancer `python` directement :

```bash
$ python
Python 3.7.4 (default, Jul 28 2019, 22:33:35)
[Clang 8.0.7 ... on linux]
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Ensuite, on peut tester un premier calcul :

```python
>>> 1 + 2*3
7
```

TODO : ajouter pkg install jupyter

### :fa-windows: Avec Windows

Pour commencer, en ayant installé la distribution *Anaconda*, *Spyder* est accessible, il dispose d'une console, on peut donc tester immédiatement quelques instructions.

```bash
Python 3.7.5 (default, Oct 25 2019, 15:51:11)
Type "copyright", "credits" or "license" for more information.

IPython 7.9.0 -- An enhanced Interactive Python.

In [1]:
```

*Spyder* offre de nombreux avantages pour utiliser Python les premières fois.


## :fa-calculator: La console Python comme calculatrice

### Travail avec des entiers

Python est capable de travailler avec des nombres aussi grands que la mémoire du système d'exploitation le permet.

> :fa-bolt: Attention, l'affichage de nombres très grands peut prendre beaucoup de temps. Les calculs en représentation binaire peuvent être très rapides en revanche !

#### Opérations élémentaires  `+` `-` `*`

Rien de particulier à signaler, si ce n'est que :

- les priorités sont respectées,
- on peut aussi utiliser des parenthèses,
- les multiplications doivent être explicites.

#### Division entière et modulo `//` `%`

Commençons à travailler avec des entiers.

- L'opérateur du quotient de la division entière est `//`
- Pour obtenir le reste dans la division entière, on utilise l'opérateur modulo `%`

```python
In [1]: 1984 % 100
Out[1]: 84

In [2]: 1984 // 100
Out[2]: 19
```

> :fa-bolt: Il ne faut pas oublier de doubler le caractère /
> Sinon, l'opération donnera un flottant. (Voir ensuite)

#### Puissance `**`

Exemple du calcul de un milliard sept.

```python
In [3]: 10**9 + 7
Out[3]: 1000000007
```

#### :fa-key: Chiffres d'une puissance d'entiers

> - Quels sont les trois derniers chiffres de $456^{78}$ ? (*Ne faire afficher que ceux-là !*)
> - :fa-shield: Quel est le 50^ième^ chiffre en partant des unités de 1337 à la puissance 42 ?
>
>> :fa-bolt: Le calcul modulaire est massivement employé en informatique, en particulier en sécurité comme la cryptographie.

#### Comparaisons `<` `<=` `==` `<>` `!=` `>=` `>`

On a les opérateurs de comparaison :

- `<` strictement inférieur à
- `<=` inférieur ou égal à
- `==` égal à
- `<>` différent de
- `!=` différent de (*variante*)
- `>=` supérieur ou égal à
- `>` strictement supérieur à

> Exemples, avec une identité remarquable et un calcul de factorielle avec un résultat très grand.

```python
In [4]: (50 + 3)**2 == 50**2 + 2*50*3 + 3**2
Out[4]: True

In [5]: from math import factorial

In [6]: factorial(2019) < 10**5000
Out[6]: False
```

> :fa-info: **La factorielle** (*factorial*  en anglais) d'un entier $n$ est le produit $1\times 2\times 3\times 4\times \cdots \times n$. On la note $n!$
>> Exemple : $5! = 1\times 2\times 3\times 4\times 5 = 120$.
>
> `from math import factorial` , cette ligne importe la fonction factorielle depuis le module math.
> On constate ici que $2019!$ possède plus de 5000 chiffres.

### Travail avec les flottants

> :fa-bolt: Les [flottants](https://fr.wikipedia.org/wiki/IEEE_754) sont presque des nombres à virgules, mais n'en sont pas du tout !

#### Les choses simples avec les flottants

- Le point est le séparateur décimal du nombre affiché.
- Ces nombres sont stockés en binaire (et non en décimal) avec une précision un peu meilleure qu'avec une calculatrice, mais pas arbitraire non plus.
- On peut entrer directement un nombre en écriture scientifique en utilisant la notation [e](https://en.wikipedia.org/wiki/Scientific_notation#E-notation)
  - exemple : `-1.602e-19` pour $-1,602 \times 10^{-19}$, la charge en coulomb d'un électron.

```python
In [7]: from math import pi

In [8]: pi / 2
Out[8]: 1.5707963267948966

In [9]: 1.2**1000
Out[9]: 1.5179100891722457e+79

In [10]: 7.3 + 2
Out[10]: 9.3

In [11]: 21 / 3
Out[11]: 7.0

In [12]: 18 / 6.02e23
Out[12]: 2.990033222591362e-23
```

> Une approximation de $\frac \pi 2$ donnée avec une quinzaine de chiffres décimaux significatifs.
> La [division](https://fr.wikipedia.org/wiki/Division) entre flottants s'obtient avec l'opérateur `/`
> Un calcul d'une puissance d'un flottant. Le résultat est donné en écriture scientifique $\approx 1,\!5179\times10^{79}$
> On peut mélanger les entiers et flottants  dans les opérations, le résultat sera en flottant.
> Si on utilise l'opérateur `/`, le résultat sera un flottant, même si la division entière a un reste nul.
> Le dernier exemple donne [le calcul du volume moyen d'une molécule d'eau](https://en.wikipedia.org/wiki/Avogadro_constant) en ml, soit environ  30 Å^3^.

#### Les points plus délicats

On retrouve comme sur de nombreuses calculatrice (et c'est normal) les points suivants :

- Il existe des limites aux nombres flottants, avec un plus petit strictement positif, un plus grand positif, et de même avec les négatifs.
- Le nombre affiché n'est souvent pas égal au nombre représenté en machine !
- Pour simplifier, il y a, en gros, une quinzaine de chiffres significatifs, et des exposants entre -1000 et +1000, environ.

```python
In [13]: 0.5**1000
Out[13]: 9.332636185032189e-302

In [14]: 0.5**2000
Out[14]: 0.0

In [15]: 2.0**1000
Out[15]: 1.0715086071862673e+301

In [16]: 2.0**2000
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

OverflowError: (34, 'Numerical result out of range')
```

> La première opération donne un résultat très petit.
> La deuxième, tellement petit, qu'il est assimilé à zéro.
> La troisième donne un résultat très grand, écrit en écriture scientifique.
> La quatrième provoque une erreur, le résultat étant trop grand. Notons que `2**2000` ne provoque pas d'erreur.

#### Les points techniques

À aborder en seconde lecture.
> [La cinquième va vous étonner.](http://www.legorafi.fr/2017/10/17/7-proverbes-de-sagesse-chinoise-que-nous-navons-pas-su-traduire/)

```python
In [17]: 0.1 + 0.2 == 0.3
Out[17]: False
```

> - $0.1$ est stocké en machine par un nombre qui n'est pas exactement égal à $0.1$, mais par un nombre en binaire très proche. De même pour $0.2$ et $0.3$.
> - Le test d'égalité est réalisé sur les nombres binaires, pas sur les nombres affichés en décimal !
> - Une calculatrice a normalement le même comportement, sauf si elle travaille avec les nombres réellement décimaux.

```python
In [18]: type(1)
Out[18]: int

In [19]: type(1.)
Out[19]: float

In [20]: 1. is 1
Out[20]: False

In [21]: 1. == 1
Out[21]: True
```

> :fa-bolt: Explication
>
> - `1` est de type entier, (*<b>int</b>eger*)
> - `1.` ou bien `1.0` est de type flottant, (*<b>float</b>ing point number*)
> - Ce **ne sont pas** les mêmes objets en interne pour Python. *is* répond alors *False* pour faux.
> - À la comparaison, il se passe un phénomène de changement de type (transtypage). Pour être comparé à un flottant, un entier est automatiquement changé en flottant. Et là, la comparaison s'avère égale, donc le test d'égalité renvoie *True* (pour vrai).

Les opérateurs de Python travaillent avec différents objets, de type différent. En fonction du type utilisé, l'opération effective sera différente. Ainsi, on retrouvera les opérateurs `+` `-` `*` `**` `<` `<=` `==` `<>` `!=` `>=` `>` qui fonctionnent aussi avec les flottants. On y ajoute `/` pour la division, faite en binaire, .

```python
In [22]: 0.1 + 0.0045
Out[22]: 0.1045

In [23]: 5.4 + 2.7
Out[23]: 8.100000000000001

In [24]: 5,4 + 2,7
Out[24]: (5, 6, 7)
```

- Le premier exemple montre ce qu'il se passe fréquemment, l'affichage décimal de la somme de deux représentations binaires de flottants (issus de décimaux) est égal à la somme des décimaux d'origine. Cette phrase était complexe. Dit autrement : l'addition de deux décimaux, provoque en machine l'addition de deux nombres binaires qui ne sont pas égaux aux décimaux, mais la somme calculée (qui sera un nombre en binaire) peut s'écrire en décimal comme la somme des décimaux d'origine.
- Dans le second exemple, on constate que ce n'est pas une généralité.
- Dans le troisième exemple, Python a affiché les trois éléments d'un *tuple*, le second étant 4+2, égal à 6. Nous verrons les tuples plus tard. Ici, il n'y a pas d'erreur à l'exécution, on parlera éventuellement d'erreur sémantique.

#### :fa-key: Nombre de particules dans l'Univers visible

Cet exercice résolu a pour but de montrer quelques bonnes pratiques et possibilités.

- On utilise des noms de variables longs.
- On peut utiliser les écritures scientifiques.

---

On fera les approximations suivantes :

- notre Soleil est une étoile moyenne, de masse 2×10^33^ g.
- un proton (constituant essentiel des étoiles) a une masse de 1,7×10^-24^ g.
- Notre propre Galaxie (la Voie Lactée, une galaxie moyenne) contient environ 100 milliards d'étoiles.
- La masse d'une galaxie provient essentiellement des étoiles.
- On estime à mille milliards le nombre de galaxie de l'Univers visible.

> Quel est l'estimation du nombre de protons de l'Univers visible ?

---

Une solution :

```python
In [29]: masse_soleil = 2e33

In [30]: masse_proton = 1.7e-24

In [31]: nb_proton_par_étoile = masse_soleil / masse_proton

In [32]: nb_étoile_par_galaxie = 100e9

In [33]: nb_proton_par_galaxie = nb_proton_par_étoile * nb_étoile_par_galaxie

In [34]: nb_galaxie_de_Univers = 1000e9

In [35]: nb_proton_de_Univers = nb_proton_par_galaxie * nb_galaxie_de_Univers

In [36]: nb_proton_de_Univers
Out[36]: 1.1764705882352941e+80

In [37]: f"Il y a environ {nb_proton_de_Univers:.2e} protons dans l'Univers visible."
Out[37]: "Il y a environ 1.18e+80 protons dans l'Univers visible."
```

> **Commentaires :**
>
> - Nous voyons l'intérêt d'utiliser des variables avec un nom qui a du sens. C'est l'objet de notre prochaine partie.
> - La dernière instruction montre une façon moderne d'afficher les variables au sein de texte formaté, les *f-string*. **Il faudra d'abord étudier les chaînes de caractères simples**. La précision à trois chiffres significatifs n'est donnée uniquement que pour montrer la syntaxe.
> - Raisonnablement la réponse étant un ordre de grandeur comparable à 10^80^.

### Variables et affectation

#### Présentation de l'affectation

Nous avons vu que l'on pouvait utiliser des variables avec des noms plus longs qu'une lettre à l'opposé de ce que l'on voit souvent en maths ou en sciences. C'est une bonne pratique.

Variable
: - Une variable possède un nom.
  - Une variable pointe vers un objet, (une donnée) (*cet objet est peut être partagé*).
  - L'objet possède parfois une valeur (ou plusieurs, et des méthodes).
  - Par abus de langage on dit souvent qu'elle a une valeur. C'est pourtant faux en Python !
  - Dans d'autres langages c'est vrai, d'où la confusion.

Affectation
: - L'opérateur `=` réalise l'affectation, il n'est pas symétrique.
  - En pseudo-code `a = 5` se note $a \leftarrow 5$.
  - L'affectation désigne ce vers quoi la variable pointe.
  - Dans une affectation simple :
    - le membre de gauche doit être une variable,
    - le membre de droite est d'abord évalué,
    - puis le résultat est affecté à la variable.

```python
In [40]: a = 3         #  un entier de valeur 3 est affecté à a,

In [41]: x = 20 - a*5  # 5 est affecté à x (plus simplement)

In [42]: x = 2*x + 1   # 11 est affecté à x

In [43]: y = x*x - 1

In [44]: y
Out[44]: 120
```

> Remarques :

- Par abus de langage on pourra souvent dire que la valeur de `y` est 120. Avec plus de rigueur, on dira que `y` pointe vers un entier de valeur 120.
- Dans la troisième instruction, l'ancienne valeur de `x` est utilisée dans le calcul du membre de droite. Le résultat du membre de droite est stocké, la variable `x` pointe alors vers ce résultat.
- En console, une affectation ne produit pas d'affichage.
- On peut faire des commentaires dans une instruction en commençant par le **croisillon** `#`.
  - Croisillon n'est pas un dièse, et en anglais on dit *sharp*, ou aussi parfois *hash*.
  - Un commentaire n'est pas interprété par Python.

#### Affectation plus précisément

Pour une seconde lecture

Affectation
:  - Le membre de gauche doit être une ou plusieurs variables.
   - Le membre de droite est soit :
      - un littéral (*une donnée écrite dans le code*)
      - une instruction que l'on peut évaluer
      - une autre affectation
   - Le membre de droite est interprété en premier.
   - Le ou les résultats sont affectés à la ou aux variables :
      - s'il n'y a qu'une variable et plusieurs résultats, le tuple des résultats est affecté à la variable ;
      - s'il y a autant de variables que de résultats, dans l'ordre chaque résultat est affecté à une variable ;
      - sinon, une `ValueError` se produit.
      - Pour les utilisateurs avancés, il y a encore plus général, à coup de *pack/unpack* ; voir l'exemple 56, bien plus technique (et totalement hors programme NSI). Le *unpack* existe aussi pour les dictionnaires, souvent écrit `**kwargs`.

Exemples :

```python
In [50]: a, b = 2, 3, 4
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: too many values to unpack (expected 2)

In [51]: a, b, c, d = 2, 3, 4
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: not enough values to unpack (expected 4, got 3)

In [52]: a, b, c = 2, 3, 4

In [53]: a + b*c
Out[53]: 14

In [54]: a = 2, 3, 4

In [55]: a[0], sum(a), a
Out[55]: (2, 9, (2, 3, 4))

In [56]: a, b, *c, d = 1, *a, 5, 6; print(a, b, c, d)
Out[56]: 1 2 [3, 4, 5] 6
```

Il est alors possible, en Python, de faire de [l'affectation parallèle](https://fr.wiktionary.org/wiki/affectation_parall%C3%A8le).
> C'est particulièrement pratique pour échanger le contenu de deux variables.

```python
temp = x
x = y
y = temp
```

Le code ci-dessus peut être remplacé par :

```python
x, y = y, x
```

>Il est possible aussi, en Python, de faire de [l'affectation multiple](https://fr.wiktionary.org/wiki/affectation_multiple) `c = b = a`

#### Le nom d'une variable

On ne peut pas choisir n’importe quel nom pour une variable.
De manière synthétique, on a :

- **Conseil important :** N’utiliser que les caractères : `a→z`, `A→Z` , `0→9` et `_`
- **Obligatoire :** Ne pas débuter par un chiffre
- **Conseil :** `choisir_un_nom_de_variable_lisible`, `choisirUnNomDeVariablePlusLisible`, `nepaschoisirunnomdevariableillisible`, `JE_SUIS_UNE_JOLIE_CONSTANTE`
- *Exemples :* `nombre_dOr`, `a15` sont valides et lisibles.
- *Attention :* `niter`, `nIter`, `NITER` sont trois variables différentes, la seconde étant la plus lisible des trois.
- *Remarque :* les lettres Unicode sont autorisées comme `Çå_Ãĺòŕš`, mais non conseillées.
- *Conseil :* ne pas débuter par `_`, sauf si vous savez/voulez travailler avec des variables cachées.
- [Pour en savoir plus sur le snake_case et ses variantes](https://fr.wikipedia.org/wiki/Snake_case).


:fa-bolt: **Exemple méchant authentique**
```python {.line-numbers cmd="python3" output="text"}
value = 42
valuе = 1000
print(value)
# on s'attend à un affichage de 1000, logique ! Et NON !!!
```

**Explication :**
- le premier `value` est écrit avec des caractères directement accessibles au clavier, la dernière lettre est un 'e' latin dont le code est 101.
- le second `valuе` se termine par un 'е' cyrillique dont le code est 1077. Visuellement identique, ce n'est pas le même caractère, et donc il y a deux variables différentes.
- le 'print' agit sur la première variable... **Le piège est redoutable et totalement invisible.**

*Further reading : [WTFPython](https://github.com/satwikkansal/wtfpython)*

#### Les mots réservés de Python3

Il y a **35 mots réservés** (dont deux récents) qui ne peuvent pas être utilisés pour des variables.

> |           |           |           |           |         |
> |:----------|:----------|:----------|:----------|:--------|
> |`False`    |`class`    |`finally`  |`is`       |`return` |
> |`None`     |`continue` |`for`      |`lambda`   |`try`    |
> |`True`     |`def`      |`from`     |`nonlocal` |`while`  |
> |`and`      |`del`      |`global`   |`not`      |`with`   |
> |`as`       |`elif`     |`if`       |`or`       |`yield`  |
> |`assert`   |`else`     |`import`   |`pass`     |`async`        |
> |`break`    |`except`   |`in`       |`raise`    |`await`         |
>
> *Remarque* : Seuls `False`, `None` et `True` commencent ici avec une majuscule.

Nous avons déjà vu :

- `False` et `True` : les booléens faux et vrai.
- `from` et `import` : pour importer **à partir** d'un module.
- `is` : test d'identité entre objets.

Nous allons bientôt voir :

- `None` : pour une donnée 'sans valeur' ; zéro étant un entier possédant une valeur.
- `del` : pour détruire (*<b>del</b>ete*) une variable et/ou des données.
- `and`, `or`, `not` : opérateurs sur les booléens : **et**, **ou**, **non**.
- `def` ou `lambda`, `return` : pour définir une fonction.
- `pass` : pour une instruction qui ne fait rien.
- `if`, `elif`, `else` : pour les structures conditionnelles.
- `for`, `while` : pour créer des boucles.
- `break`, `continue` : pour des boucles plus complexes.
- `in` : pour un test d'appartenance.

Nous verrons plus tard certains mots réservés parmi ceux qui restent.

- `assert` : pour le débogage facile.
- `try`, `except`, `raise` : pour la gestion des erreurs.
- `with`, `as` : pour la lecture de module ou de fichier.

## :fa-globe: En informatique, on utilise massivement l'anglais

| *English*       | Français |
| ---------------:|:---------|
| *print*         | affiche |
| *assignement*   | affectation |
| *coma*          | virgule |
| *to the power*  | à la puissance |
| *integer*       | entier |
| *digit*       | chiffre |
| *sharp* (#)   | croisillon (#) |
| *library*     | bibliothèque |

Attention aux faux amis, en informatique :

- On ne dit pas 'assignation', mais 'affectation' ; assignation est un terme juridique.
- On ne dit pas 'digital', mais 'numérique' ; digital est en rapport avec les doigts de la main.
- On ne dit pas 'librairie', mais bibliothèque ; un ensemble de fichiers contenant des morceaux de codes utilisés souvent. 'Librairie' se traduit par '*(UK) Bookshop*' ou '*(US) Bookstore*'.
- On ne devrait pas dire 'hashtag', ni 'dièse' pour #, mais '*sharp*' ou 'croisillon'.

D'un autre côté, certains anglicismes sont très répandus.

- Certains sont parfois [moqués](https://linuxfr.org/users/joalland/journaux/vive-l-insertion-digitale), comme ~~digital~~. On dira numérique.
- D'autres sont répandus comme ~~librairie~~ au lieu de bibliothèque.

## :fa-key: Émissions de CO~2~ associées à un plein de carburant

- On suppose qu'un réservoir contient 60 L de carburant de densité 0,8 et dont les atomes de carbone représentent 85% de la masse.
- On suppose que la combustion de ce carburant conduit chaque atome de carbone à produire une molécule de CO~2~ rejetée dans l'atmosphère.
- On rappelle qu'une mole d'atomes de carbone a une masse de 12 g.
- On rappelle qu'une mole d'atomes d'oxygène a une masse de presque 16 g.
- On considérera que le CO~2~ rejeté est un gaz dont la densité est 22.4 l.mol^-1^

> Quelle est la masse de CO~2~ rejetée associée à un plein ?
> D'après vous, quelle proportion cela représente-t-il, en masse, de l'ensemble des déchets directs d'un adulte ? (C'est une question très ouverte, à l'échelle d'une vie, ou de la partie vie active, ou autre au choix.)
> Quel volume de gaz cela représente-t-il ? Et sur la vie d'un véhicule qui aura fait 300000 km en consommant, en moyenne, 6 l de carburant pour 100 km ?
>
>> **Commentaire** : Ce genre de problèmes, sans véritable algorithme peut être résolu en console Python. C'est l'occasion d'utiliser des variables bien nommées. Vous êtes libres de faire cet exercice, ou bien d'autres liés à l'énergie, c'est toujours instructif.
