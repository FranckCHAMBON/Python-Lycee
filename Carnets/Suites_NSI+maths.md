**Complément de cours inter-disciplinaire**

tags : première, maths, NSI, suites
# Suites et outils numériques
Pour le lycéen, en classe de première, en spécialité maths et NSI.  

## I] Définitions, premières propriétés
Une **suite** est une liste d'éléments, qu'on appelle **termes**.

Exemples :
* $a = (A, B, C, \cdots , Y, Z)$ est la suite ordonnée des lettres majuscules de l'alphabet latin, c'est une suite finie.
* $b = (1, 3, 5, 7, \cdots)$ est la suite ordonnée des entiers positifs impairs, elle est infinie.
* $F = (0, 1, 1, 2, 3, 5, 8, \cdots)$ est la suite débutant par $0$ puis $1$ et dont les termes suivants sont la somme des deux précédents. C'est la suite de Fibonacci.
* $h = (1, \frac12, \frac13, \frac14, \cdots)$, $h$ comme harmonique.

Vocabulaire :
* On dit qu'une suite est **numérique** quand ses termes sont des nombres.
* Les termes sont **indicés** avec des entiers dans $\mathbb N$.
    * $a_0 = A$, $a_1 = B$, ... $a_{25} = Z$
    * $b_0 = 1$, $b_1 = 3$, $b_2 = 5$, et pour tout $n\in\mathbb N$, $b_n = 2n+1$.
    * $F_0=0$, $F_1=1$, et $F_{n+2} = F_{n+1} + F_n$ pour tout $n\in\mathbb N$.
    * $h_n = \frac1n$ pour tout $n\in\mathbb N^*$, $h_0$ n'est pas défini !
* Il y a plusieurs notations pour une suite :
    * La suite $u$, son premier terme $u_0$.
    * La suite $(u)$, son dixième terme $u_9$.
    * La suite $(u_n)_n$, son $n$-ième terme $u_{n-1}$.
    * La suite $(u_n)_{n\in\mathbb N}$, son $(k+1)$-ième terme $u_k$.
    * On préfère les notations courtes, mais on utilise les longues pour lever des ambiguïtés.
* **Définir** une suite, c'est donner assez d'information pour pouvoir donner un sens à chaque terme. De manière simple, ce serait pouvoir calculer les termes, successivement, mais en vrai cela peut être plus délicat. Rendez-vous en post-BAC pour la _calculabilité_.
* En mathématiques, on choisit souvent une seule lettre pour le nom d'une suite, et en particulier la suite $(u_n)_{n\in \mathbb N}$ est la plus souvent choisie pour désigner une suite générique.
* En informatique, on pourra choisir un nom de variable à plusieurs lettres pour stocker les premiers termes d'une suite. On utilisera une structure de donnée itérable.
    * En C, on utilisera un tableau.
    * En Python, on utilisera une liste (_list_).
    * Avec un tableur, on utilisera des cellules contigües.

Il existe plusieurs façons de définir une suite :
- par une formule globale $u_n = f(n)$ pour $n \in I$, où $I$ est un intervalle de $\mathbb N$, et $f$ une fonction.
- par récurrence, on donne le ou les premiers termes, puis une méthode pour définir les suivants en fonctions des précédents. Comme avec l'exemple de la suite de Fibonacci.

### I.A] Suites arithmétiques
Ce sont les suites que l'on peut définir avec une fonction affine, ou de manière équivalente celles ou la différence entre deux termes consécutifs est constante.
* $(u)$ est arithmétique $\iff$ il existe $a, b \in \mathbb R$ tel que pour tout $n\in\mathbb N$, $u_n = a\times n + b$.
  > Dans ce cas, on a $u_0 = b$, et pour tout $n\in \mathbb N$,  
  $u_{n+1} - u_n = \left(a\times(n+1) + b\right) - (a\times n + b)$  
  $u_{n+1} - u_n = an + a + b -an -b$  
  $u_{n+1} - u_n = a$. On dit que la suite est arithmétique de raison $a$.
  
* On peut définir une suite arithmétique par la donnée de sa raison (souvent notée $r$) et de son premier terme $u_0$.
    > Dans ce cas, on a pour tout $n\in \mathbb N \quad u_{n+1} - u_n = r \quad \textrm{et} \quad u_n = u_0 + rn$.  
    On a aussi pour tout $n\in \mathbb N \quad u_{n+1} = u_n + r$
    
* Avec l'exemple du paragraphe précédent, on peut dire que $(b)$ est une suite arithmétique de premier terme $1$ et de raison $2$.


#### Exercice
> $(u)$ est une suite arithmétique telle que $u_{10} = 1757$ et $u_{100} = 5537$, déterminer $u_n$ en fonction de $n$.

**Réponse :**
$u$ est arithmétique, donc il existe des nombres $a$ et $b$ tels que pour tout $n\in \mathbb N \quad u_n = an+b$

On a $u_{100} = 100a +b = 5537$, et  $u_{10} = 10a +b = 1757$, par soustraction on obtient :  
$u_{100} - u_{10} = 100a - 10a = 5537 - 1757$, d'où l'on tire  
$90a = 3780$, et donc $a = 42$.  

On a donc, pour tout $n\in \mathbb N \quad u_n = 42n+b$, et avec $n=10$, on a:  
$u_{10} = 42\times10 + b = 1757$, d'où $b = 1757 - 420 = 1337$.  
On aurait également trouvé $b=1337$, de la même manière, en utilisant $u_{100} = 5537$.

_Conclusion_ : pour tout $n\in \mathbb N \quad u_n = 42n + 1337$.

> Remarque, culture _geek_
* $42$ est la réponse à la question universelle dans le livre H2G2.
* $1337$ est le nom d'un codage qui se prononce _Elite_, où l'on remplace les lettres par d'autres symboles.
    * L est remplacé par `1`, en anglais on prononce comme : elle
    * E est remplacé par `3`, en anglais on prononce comme : i
    * T est remplacé par `7`, en anglais on prononce comme : t
    * (elle, i, i, t) se prononce alors comme _elite_ en anglais.

### I.B] Somme de termes consécutifs d'une suite arithmétique
#### $S_n = 1+2+3+4+\cdots+n$
Notre objectif est d'établir une formule pour $S_n$. On l'écrit dans un sens, puis à l'envers, on ajoute les termes qui se correspondent de façon à obtenir $2S_n$ qui est la somme de $n$ termes tous égaux.

|$S_n$|$=1$|$+2$|$+3$|$\cdots$|$+(n-2)$|$+(n-1)$|$+n$|
|----:|----|----|----|--------|--------|--------|----|
|$+S_n$|$=n$|$+(n-1)$|$+(n-2)$|$\cdots$|$+3$|$+2$|$+1$|
|$=2S_n$|$=(n+1)$|$+(n+1)$|$+(n+1)$|$\cdots$|$+(n+1)$|$+(n+1)$|$+(n+1)$|

On tire $2S_n = n(n+1)$, il y avait $n$ termes égaux à $(n+1)$.
> **Conclusion** : pour tout $n\in \mathbb N \quad 1+2+3+4+\cdots+n = \dfrac{n(n+1)}2$.


### I.C] Suites géométriques
On a vu que pour une suite arithmétique $(u)$, on a pour tout $n\in \mathbb N$ : $u_{n+1} = u_n + r$, où $r$ est la raison.

De la même manière, on dira qu'une suite $(v)$ est géométique, si pour tout $n\in \mathbb N$ : $v_{n+1} = v_n \times q$, où $q$ est la raison.

Pourquoi $q$ ?
> $q$ comme quotient. Si les termes sont non nuls, on  a pour tout $n\in \mathbb N$ : $\dfrac {v_{n+1}}{  v_n } = q$.

Pourquoi $v$ ?
> On met ce qu'on veut.

Y a-t-il une formule pour le terme d'indice $n$ ?
> Oui.

On considère une suite géométrique de premier terme $v_0$ et de raison $q$. On a :
* $v_0 = v_0 = v_0\times q^0$
* $v_1 = v_0 \times q = v_0\times q^1$
* $v_2 = v_0 \times q\times q = v_0\times q^2$
* $v_3 = v_0 \times q\times q \times q= v_0\times q^3$

> Et de manière générale : pour tout $n\in\mathbb N$, on a $v_n = v_0 \times q^n$

### I.D] Somme de termes consécutifs d'une suite géométrique
#### avec premier terme égal à 1
On pose $q\neq1$, et on considère :
$S_n = 1+q+q^2+\cdots+q^{n-1}+q^n$

On a $qS_n = q+q^2+q^3\cdots+q^n+q^{n+1}$, 

### I.E] Variations d'une suite numérique

## II] Générations avec une fonction
Dans la suite, on prendra pour exemple la suite définie avec $u_n = f(n)$, où $f(x) = \sqrt{x^2+1} - x$

### II.A] Avec Python


```python
from math import sqrt

def u(x):
    return sqrt(x**2 + 1) - x

# exemple 1
for n in [10, 100, 1000]:
    print(n, u(n))
```

    10 0.049875621120889946
    100 0.004999875006248544
    1000 0.0004999998750463419


La première ligne permet d'utiliser _sqrt_, à partir du module _math_.
> _**sq**uare **r**oo**t**_ : la racine carrée, en anglais.

On définit ensuite la suite $(u_n)_{n\in \mathbb N}$ avec une fonction.

On calcule ensuite trois termes, et on les affiche.


```python
# exemple 2
U = []
for n in range(4):
    U.append(u(n))
print(U)
print()
print(U[3])
```

    [1.0, 0.41421356237309515, 0.2360679774997898, 0.16227766016837952]
    
    0.16227766016837952


On peut construire une liste vide, et ensuite y ajouter élément par élément, les 4 premiers termes de la suite.

On affiche ensuite la liste construite, puis le quatrième terme. $u_0$ en est le premier terme.


```python
# exemple 3
V = [u(n) for n in range(10)]
print(V)
print(V[3])
```

    [1.0, 0.41421356237309515, 0.2360679774997898, 0.16227766016837952, 0.12310562561766059, 0.09901951359278449, 0.08276253029821934, 0.0710678118654755, 0.06225774829854913, 0.0553851381374173]
    0.16227766016837952


Une variante où l'on construit la [liste en compréhension](https://fr.wikipedia.org/wiki/Liste_en_compr%C3%A9hension).


```python

```
