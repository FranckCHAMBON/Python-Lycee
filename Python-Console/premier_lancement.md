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

On pourra aussi avantageusement utiliser *Spyder* qui dispose également d'une console plus pratique pour les débutants.

### :fa-android: Avec une tablette Android

On installe et lance l'application [*Termux*](https://play.google.com/store/apps/details?id=com.termux&hl=fr). On obtient également une invite de commande `bash`, comme sous Linux. Si on entre `python` la première fois, il indique comment l'installer. Suivre les instructions.

```bash
$ python
(... TODO ... please type ...)
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

### :fa-windows: Avec Windows

Pour commencer, en ayant installé la distribution [*Anaconda*](https://www.anaconda.com/distribution/#download-section), *Spyder* est directement accessible, il dispose d'une console, on peut donc tester immédiatement quelques instructions.

```bash
Python 3.7.5 (default, Oct 25 2019, 15:51:11)
Type "copyright", "credits" or "license" for more information.

IPython 7.9.0 -- An enhanced Interactive Python.

In [1]:
```

*Spyder* offre de très nombreux avantages pour utiliser Python les premières fois, comme ensuite de manière intensive. *Jupyter* sera très utile pour la partie intermédiaire et pour proposer des supports de cours de sciences.
