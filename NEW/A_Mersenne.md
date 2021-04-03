---
export_on_save:
  html: true
---


# Découverte des nombres de Mersenne

## Définition

Les [nombres de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier) sont de la forme : $M_n = 2^n -1$, pour $n$ un entier non nul. 


### Exemples

- $M_1 = 2^1 -1 = 1$, n'est pas premier, par définition
- $M_2 = 2^2 -1 = 3$, est **premier**, 2 aussi
- $M_3 = 2^3 -1 = 7$, est **premier**, 3 aussi
- $M_4 = 2^4 -1 = 15$, n'est pas premier, $3\times5$
- $M_5 = 2^5 -1 = 31$, est **premier**, 5 aussi
- $M_6 = 2^6 -1 = 63$, n'est pas premier, $3\times3\times7$
- $M_7 = 2^7 -1 = 127$, est **premier**, 7 aussi
- $M_8 = 2^8 -1 = 255$, n'est pas premier, $3\times5\times17$
- $M_9 = 2^9 -1 = 511$, n'est pas premier, $7\times73$
- $M_{10} = 2^{10} -1 = 1023$, n'est pas premier, $3\times11\times13$
- $M_{11} = 2^{11} -1 = 2047$, n'est pas premier, $23\times89$, **pourtant 11 est premier**
- $M_{12} = 2^{12} -1 = 4095$, n'est pas premier, $3\times3\times5\times7\times13$

> Le plus grand nombre premier connu a souvent été un [nombre de Mersenne](https://fr.wikipedia.org/wiki/Nombre_de_Mersenne_premier).
> - Nous présentons quelques aspects historiques, et ce sera l'occasion de découvrir le langage Python.


## Aspect historique

### Au XVII^e^ siècle

Au début du XVII^e^ siècle, [Marin Mersenne](https://fr.wikipedia.org/wiki/Marin_Mersenne), moine de l'ordre des Minimes, pense et démontre peut-être que « Si $M_n$ est premier alors $n$ aussi ». La réciproque est fausse, comme le montre $n = 11$.

> Marin Mersenne fournit aussi une liste des nombres premiers « de Mersenne » jusqu’à l'exposant 257. Cette liste contenait des erreurs ; il y a de vraies difficultés, comme nous le verrons par la suite.


### Au XVIII^e^ siècle

En 1772, [Leonhard Euler](https://fr.wikipedia.org/wiki/Leonhard_Euler) prouve que $M_{31}$ est un nombre premier. Il lui a suffit de poser $372$ divisions pour cela.


> Avec Python, on peut calculer $M_{31}$ ainsi :

```python
>>> 2**31 - 1
2147483647
```

> Le nombre $2\,147\,483\,647$ est resté le plus grand nombre premier connu jusqu'en 1867. 

### Au XIX^e^ siècle

[Édouard Lucas](https://fr.wikipedia.org/wiki/%C3%89douard_Lucas) a inventé un test de primalité, qui lui a permis de prouver en 1876 que $M_{127}$ est premier.

Ce nombre a gardé le record jusqu'en 1951, le début de l'ère moderne des ordinateurs.

### Au XX^e^ siècle

En 1952, [Raphael Robinson](https://fr.wikipedia.org/wiki/Raphael_Robinson) prouve que $M_{521}$ est premier à l'aide d'un ordinateur. Depuis, le record est presque toujours détenu par un nombre de Mersenne.

> ==Remarque==
> Python peut faire des calculs avec des entiers aussi grands que la mémoire de l'ordinateur le permet. Concrètement, **Python peut travailler** avec des nombres qui ont des millions de chiffres. En revanche, **Python ne peut pas afficher** de tels nombres. Ce n'est pas une histoire d'écran, c'est une histoire de conversion binaire vers décimal.
- Avec un émulateur en ligne comme [Basthon](https://console.basthon.fr/), on peut encore afficher $M_{216\,091}$ qui a $65\,050$ chiffres.
- Le dernier record du XX^e^ siècle, $M_{6\,972\,593}$ peut encore être affiché raisonnablement avec Python installé sur poste fixe, il a $2\,098\,960$ chiffres.


### Au XXI^e^ siècle

- [GIMPS](https://fr.wikipedia.org/wiki/Great_Internet_Mersenne_Prime_Search) est un projet de calcul partagé, fondé par George Woltman. Ce projet a permis de trouver les plus grands nombres premiers récents.
- Les derniers records ont plus de 20 millions de chiffres, et sont difficiles à afficher avec Python.

> Même si on ne peut pas afficher un nombre très grand, on peut travailler avec et, par exemple, calculer un résidu modulaire.


## Exercice

<iframe src="https://console.basthon.fr/?script=eJxTUlLi5VJWcK1ILUrOTE5VsOLl4uVyTsxJLs1JLVLwjTc0MlewUjBSOLxAISdRoaA0s7g4MQ-oDiiuo1CQU1qsYAjSoQQyBgAM1hPP" width="1000" height="700"></iframe>

<details>
   <summary>Cliquer ici pour voir la solution</summary>
   Dans la console, on entre et on obtient
<pre>>>> 2**127 - 1
170141183460469231731687303715884105727
</pre>
</details>


---

:arrow_backward: [Retour au sommaire](python-maths-1.html)


---

:arrow_forward: Cours [Division entière et modulo : `//` `%`](C_division_modulo.html)

