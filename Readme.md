![chess_club](img/logo-chess-tournament.JPG)

<h1 align="center">Développez un programme logiciel en Python</h1>

<p align="center">
    <a href="https://www.python.org">
        <img src="https://img.shields.io/badge/Python-3.12+-3776AB?style=flat&logo=python&logoColor=white" alt="python-badge">
    </a>
    <a href="https://flake8.pycqa.org/en/latest/">
        <img src="https://img.shields.io/badge/Flake8-6.1+-d71b60?style=flat" alt="Flake8">
    </a>
    <a href="https://tinydb.readthedocs.io/en/latest/">
        <img src="https://img.shields.io/badge/TinyDb-4.8+-00838f?style=flat" alt="TinyDb">
    </a>
</p>

# A propos du projet

***Livrable du Projet 4 du parcours D-A Python d'OpenClassrooms : Développez un programme logiciel en Python***

_Testé sous Windows 10 - Python version 3.12.3_


## Table des matières

1. [Initialisation du projet](#id-section1)
    1. [Windows](#id-section1-1)
    2. [MacOS et Linux](#id-section1-2)
    3. [Générer un rapport flake8](#id-section1-3)
2. [Options des menus](#id-section2)
    1. [Menu principal](#id-section2-1)
    2. [Menu des tournois](#id-section2-2)
    3. [Menu des joueurs](#id-section2-3)
    4. [Menu des rapports](#id-section2-4)



<div id='id-section1'></div>

## 1. Initialisation du projet

<div id='id-section1-1'></div>


#### i. Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.
###### Récupération du projet

    $ git clone https://github.com/Gaiden92/P4OC.git

###### Activer l'environnement virtuel
    $ cd P4OC
    $ python -m venv env
    $ ~env\scripts\activate
    
###### Installer les paquets requis
    $ pip install -r requirements.txt

###### Lancer le programme
    $ python main.py


<div id='id-section1-2'></div>

---------

#### II. MacOS et Linux :
Dans le terminal, naviguer vers le dossier souhaité.
###### Récupération du projet

    $ git clone https://github.com/Gaiden92/P4OC.git

###### Activer l'environnement virtuel
    $ cd P4OC 
    $ python3 -m venv env 
    $ source env/bin/activate
    
###### Installer les paquets requis
    $ pip install -r requirements.txt

###### Lancer le programme
    $ python3 main.py


<div id='id-section1-3'></div>

----------

#### III. Générer un rapport flake8

    $ flake8 --format=html --htmldir=flake8_report

**Vous trouverez le rapport dans le dossier _'flake8-report'_.**

_Dernier rapport exporté :_

![latest_report](img/flake8-report.JPG)

<div id='id-section2'></div>

## 2. Option des menus

<div id='id-section2-1'></div>

#### I. Menu principal

![main_menu](img/main-menu.JPG)

<div id='id-section2-2'></div>

#### II. Menu des tournois

![tournaments_menu](img/tournaments-menu.JPG)

<div id='id-section2-3'></div>

#### III. Menu des joueurs

![players_menu](img/players-menu.JPG)

<div id='id-section2-4'></div>

#### IV. Menu des rapports

![reports_menu](img/reports-menu.JPG)

###### Exemples de rapports :

![reports_example](img/example-report1.JPG)

![reports_example](img/example-report2.JPG)

![report_tournament](img/tournament-report.JPG)