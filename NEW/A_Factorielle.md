---
export_on_save:
  html: true
---


# Découverte de la fonction factorielle


## Structures conditionnelles

==**À savoir**==


Avec Python, on a les constructions suivantes possibles :

```python
"""
`action()` n'est exécutée que si condition est évalué à `True`
"""
if condition:
    action()
```

```python
"""
`action()` n'est exécutée que si condition est évalué à `True`
sinon, c'est `autre_action()` qui est exécutée.
"""
if condition:
    action()
else:
    autre_action()
```

```python
"""
`elif` est la contraction de `else if`, pour « sinon si ».
Il peut y avoir autant de blocs `elif` que l'on souhaite.
On peut terminer, par un bloc `else` pour les cas non traités.
"""
if condition_1:
    action_1()
elif condition_2:
    action_2()
elif condition_3:
    action_3()
else:
    action_autres_cas()
```

Exemple

La suite de Syracuse d'un entier $N>0$ est définie par récurrence, de la manière suivante :
- $u_0 = N$
- pour tout entier naturel $n$ : $u_{n+1} = \begin{cases}\dfrac{u_n}{2}&\text{si } u_n \text{ est pair,}\\3×u_n + 1&\text{si } u_n \text{ est impair.}\end{cases}$

On peut alors définir la fonction `terme_suivant`

```python
def terme_suivant(u_n):
    """ Renvoie le terme suivant `u_n` dans une suite de Syracuse.
    """
    if u_n % 2 == 0:
        return u_n // 2
    else:
        return 3 * u_n + 1
```


## La fonction factorielle

### Définitions et exemples

La factorielle d'un entier $n$ se note $n!$ et est égale au produit des entiers de $1$ jusqu'à $n$.

- $5! = 1×2×3×4×5 = 120$
- $4! = 1×2×3×4 = 24$
- $3! = 1×2×3= 6$
- $2! = 1×2= 2$
- $1! = 1$
- $0! = 1$, comme un produit vide.

On remarque que $5! = 4! × 5$, et de manière générale :
$$n! = \begin{cases}1 &\text{si } n = 0\\(n-1)! × n &\text{si } n\geqslant 1\end{cases}$$

### Exercice


<iframe src="https://console.basthon.fr/?script=eJytUtFq1EAUfQ_kH07jgxsbw2ZbrRZ2QdQ3H8TXImyc3JGB7J04M1kU6b_46H5Hfqx3krVNaREEA4E7d845957DZFmWJk_w_js5ZRSlCYA0qUq8tbuuHQ6BHNoazXDQhk0wluGGg-qdN3tCQ9jqWgXrDLUtbUc6nsO08L3WJkSEI1GqlQiVZYmudlCEb72Bsrw3xKGcaGmyKmWRqD5OJXjlTBdAAfvh4Iw25NJkAm82G8wmL17kU79aLSPkrMSHmtW0vLasxs23O_K-_krbKBnLHwKQDQWjxK4jbhyV8xFHwiKPzSxmlSYN6XujOb-cCHKPT8R7awh8UkQHnbNNb4KXKR5iVRzEGhWGX-DyljcVRoOxXmN5FIyfo9A7RjV1qPX08HK-jWSc41mM-s-utx6OxM4ZDovs3dO6c8NvjzfL5er1qxUus2OG2jrZwzCuzgqcF3hZ4KKQZOU__zybPgnp7KPtI2GNn3xdQHKu77TmuPHAJ_I-qgi-n2HsXo_PgnxAz2C7--JigrST1B7q5XM3-d-sVY9ZW4qbAuJJPFaxuvgf1k4ftXb679ZuAG2K_YE" width="1000" height="600"></iframe>

<details>
   <summary>Solution</summary>
Dans le script :
<code>        return factorielle(n - 1) * n
</code>

Quelques pistes pour <code>message()</code>.
<ul>
<li><code>message()</code> ne prend aucun paramètre, il faut toutefois des parenthèses vides pour en faire une fonction.</li>
<li><code>print</code> est une fonction Python pour <strong>afficher</strong>.</li>
<li><code>for ... in ... :</code> est la construction pour répéter en boucle des instructions.</li>
<li>Le décalage (l'<strong>indentation</strong>) est indispensable pour indiquer le début et la fin d'un bloc d'instructions, pour les fonctions, comme pour les structures conditionnelles, comme pour les boucles.</li>
</ul>
</details>

## :boom: ==Défi==

On rappelle que $100! = 1×2×3×4×5...×98×99×100$

> En s'inspirant de l'activité précédente,
- justifier que $10^{30} \leqslant 100! \leqslant 10^{300}$, puis
- par dichotomie, trouver un meilleur encadrement,
- en déduire le nombre de chiffres de $100!$.

---

:arrow_backward: [Retour au sommaire](python-maths-1.html)


---

:arrow_forward: Cours [Structures de boucle](C6_boucles.html)