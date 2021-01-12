
<p  align="center">
<h1  align="center">Little Sister</h3>
</p>

## Sommaire

*  [Contexte du projet](#contexte-du-projet)

*  [Commencer](#commencer)

*  [Utilisation](#utilisation)

*  [Auteurs](#auteurs)


## Contexte du projet


La société "Little Sister" souhaite développer un nouveau type de caméras de surveillance pour l'espace publique.

Elle souhaite mettre en avant une fonctionnalité de reconnaissance d'éléments sur une image afin de pouvoir identifier des cas, des situations qui peuvent survenir dans la vie de tous les jours. Pour se faire,  **elle possède une banque d'images de références qui peuvent servir à entrainer l'IA** (Ciphar 100) .

Le but est de  **fournir un livrable**  qui pourra être  **intégré dans leur système embarqué qui est écrit en Microsoft .NET (dotnet 5).**  La société vous laisse libre quant au choix du format de fichier à exploiter, tant que celui-ci est compatible avec son système.

## Commencer

Pour avoir une copie locale et lancer le programme, suivez ces étapes.

### Installation

1. Cloner le répertoire
```git
git clone https://github.com/Nicolas-Malgat/Reco_image.git
```
2. Créer un environnement conda avec
```bash
conda create --name <env> --file environment.txt
```
## Utilisation

- Lancer [main.ipynb](https://github.com/Nicolas-Malgat/Reco_image/blob/main/main.ipynb "main.ipynb")
	- Ce notebook va générer le modèle ( [model.h5](https://github.com/Nicolas-Malgat/Reco_image/blob/main/model.h5 "model.h5") ) pour l'évaluation des images.

- Lancer [prediction_image.ipynb](https://github.com/Nicolas-Malgat/Reco_image/blob/main/prediction_image.ipynb)
	- Ce notebook charge une image dans la première cellule et effectue quelque tests,
	   puis se découpe en deux parties:
		- La première d'ajuster les filtres sur l'image 
		- La seconde donne une prédiction sur l'image

## Auteurs

Maxime Veysseyre

Nicolas Malgat
