---
export_on_save:
  html: true
---


# Découverte des nombres de Fermat


## Les nombres de Fermat

## Définition

Les [nombres de Fermat](https://fr.wikipedia.org/wiki/Nombre_de_Fermat) sont de la forme $F_n = 2^{2^n} + 1$, pour $n$ entier.

## Exemples

|$F_0$|$F_2$|$F_2$|$F_3$|$F_4$|
|:---:|:---:|:---:|:---:|:---:|
| $3$ | $5$ | $17$|$257$|$65537$|

* $F_0$, $F_2$, $F_2$, $F_3$, $F_4$ sont des nombres premiers.
* [Pierre de Fermat](https://fr.wikipedia.org/wiki/Pierre_de_Fermat) a conjecturé en 1640 que tous les nombres $F_n$ sont premiers.

1. Au sujet de $F_5$. *Faisable avec une calculatrice.*
    1. Calculer $F_5$.
    2. Vérifier que le reste dans la division de $F_5$ par $641$ est zéro.
    3. Donner le quotient de $F_5$ par $641$.
    4. [**Remarque**](https://fr.wikipedia.org/wiki/Nombre_de_Fermat#Histoire) : En 1732, le jeune Leonhard Euler, à qui Christian Goldbach avait signalé cette conjecture trois ans auparavant, la réfute : $F_5$ est divisible par $641$. Il ne dévoile la construction de sa preuve que quinze ans plus tard. Il y utilise une méthode similaire à celle qui avait permis à Fermat de factoriser les nombres de Mersenne $M_{23}$ et $M_{37}$.
2. Au sujet de $F_6$. *Là, Python devient très utile.*
    1. Calculer $F_6$.
    2. Vérifier que le reste dans la division de $F_6$ par $274\,177$ est zéro.
    3. Donner le quotient de $F_6$ par $274\,177$.
    4. **Remarque** : En 1855, [Thomas Clausen](https://fr.wikipedia.org/wiki/Thomas_Clausen_(astronome)) obtient avec ce quotient le plus grand nombre premier connu à cette époque.

[==**Culture**== _(en)_](http://www.prothsearch.com/fermat.html) : Au sujet des suivants, on constate une difficulté très importante pour progresser.
1. $F_7$ est divisible par $59\,649\,589\,127\,497\,217$. *Factorisation de $F_7$ obtenue en 1970.*
2. $F_8$ à $F_{11}$ ont pu être entièrement factorisés. *Factorisation de $F_{11}$ obtenue en 1988.*
3. En 2021, $F_{12}$ n'est toujours pas factorisé entièrement.

## Exercice

<iframe src="https://console.basthon.fr/?script=eJxtkE1OwzAQhfeRcoensGlLsZSQtoIdEvQAvQBynbFqKXXC2Im4Us6RizFOywaxm59v3nuaoijy7AEf38TGGcJrngHIs1LhRNe-1YYYSin0mlFtNivZrvGIcruAeAJFmE7IeYrEKs8qJWrzZAZp0RKCYddHWTwrvGsf0Go58KFraYtxnthZJ-TX8GsOrXBc7dagENG40QV3Fp0UYF-X6sacE7P_j6kOdXk4CFZLEI9mnprBMaGhAKtNpIGDNHeLuMgIvVN4s9aZy5I64EUY9pIswFyctUz3q7JKeJ4V6XN51pCVoV_fsy_TVJzIj52j9AHfXc9LAByJr1osP736gzPFgX369K3_Af40b1U" width="1000" height="600"></iframe>

<details>
   <summary>Cliquer ici pour voir la solution</summary>
Dans le script <code>return 2**(2**n) + 1</code>

On clique sur <code>⚙ Exécuter</code>

Dans la console :
<pre>>>> F(5) % 641
0
>>> F(6) % 274177
0
>>> F(5) // 641
6700417
>>> F(6) // 274177
67280421310721
>>> F(12) % 10**9
154190337
</pre>
</details>


==**À savoir**==

- `def` permet de **déf**inir une fonction, ici avec un paramètre.
- `>>> F(5)` est un appel de fonction qui renvoie $F_5$ à la console, qui l'affiche.
- **Attention**, ce n'est pas la fonction qui affiche $F_5$, la fonction **renvoie** $F_5$.
- C'est la console qui **affiche**.
- On le reverra :wink: .


## 💥 ==Défi==
> Quel est le 2021^e^ chiffre en partant des unités de $F_{13}$ ?

<details>
<summary>Cliquer ici pour voir la solution</summary>
<pre>
>>> F(13) // (10**2020) % 10
1
</pre>

Explication : pour avoir le 4<sup>e</sup> chiffres de <code>123456789</code> en partant des unités, on divise par 10<sup>3</sup>, on obtient <code>123456</code>, puis on prend le reste dans la division par 10, pour obtenir 6.
</details>

---

:arrow_backward: [Retour au sommaire](python-maths-1.html)

---

:arrow_forward: Cours [Comparaisons : `<` `<=` `==` `!=` `<>` `>=` `>`](C_comparaison.html)

