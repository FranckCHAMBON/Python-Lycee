---
export_on_save:
  html: true
---

# Découverte de la dichotomie

## Un exemple

```python
>>> 2**(2**12) + 1 >= 10**1200
True
>>> 2**(2**12) + 1 >= 10**1300
False
```

Explications
- $F_{12} = 2^{2^{12}} + 1$ est un nombre très grand.
- $2^{10} = 1024 > 1000 = 10^3$, on déduit que
- $2^{12} > 4×1000$, et que
- $F_{12} > 2^{4000} = 2^{10×400} = (2^{10})^{400} > (10^3)^{400} = 10^{1200}$
- Ceci explique le test `2**(2**12) + 1 >= 10**1200` qui renvoie `True`.
- Le test suivant est simplement choisi au hasard.
- On déduit que $F_{12}$ possède de $1201$ à $1300$ chiffres.
   - Comme par exemple si $10^3 \leqslant n \lt 10^4$, alors $n$ a $4$ chiffres, et réciproquement.

- Pour tous les entiers $n<1200$, on aura $F_{12} \geqslant 10^n$
- Pour tous les entiers $n>1300$, on aura $F_{12} \lt 10^n$

Pour trouver un encadrement plus fin, on choisit le milieu entre $1200$ et $1300$, **et on recommence**... On ne travaille qu'avec des entiers, à la fin on se retrouve avec deux entiers consécutifs.

- Si $F_{12} \geqslant 10^{1250}$, alors on cherche entre $1250$ et $1300$.
- Sinon, on cherche entre $1200$ et $1250$.
- Et on recommence.

## Exercice

<iframe src="https://console.basthon.fr/?script=eJx9j0FOw0AMRfcjzR2-wqYJVZSEHRLZkQNUiC0NyS-MlHhad6biSpyDizFtVAkhwcKW5f9sf2dZZs0NHj-ogxtoDQBr6hLPX5_qdo56aWHJbduiW9VNjvYBdVUUdVNVi_SkkX9Bd1eo66cjrwubMg35eKKuse8VoxveffCz49qaidhP8Yg37WUEJSQn2MoWgRMOkf-6kp-WrMnOP1ozcpcwye8X9dI9FxvKyTsinRQ_vyoxEh117gO6Fyl_4coQVdAUxSqF5LhFvSjfYW9MKg
" width="1000" height="700"></iframe>

<details>
   <summary>Solution</summary>
<pre>>>> F(12) >= 10**1200
True
>>> F(12) >= 10**1300
False
>>> F(12) >= 10**1250
False
>>> F(12) >= 10**1225
True
>>> F(12) >= 10**1237
False
>>> F(12) >= 10**1231
True
>>> F(12) >= 10**1234
False
>>> F(12) >= 10**1232
True
>>> F(12) >= 10**1233
True
</pre>

L'entier cherché est 1233, trouvé en peu d'étapes.
</details>


## :boom: ==Défi==

> Encadrer $F_{12}$ entre deux nombres de Mersenne consécutifs.


---

:arrow_backward: [Retour au sommaire](python-maths-1.html)

---

:arrow_forward: Cours  [Les variables](C_variables.html)

