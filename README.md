# Food Planning
Planning de repas pour une semaine

![](https://cdn.discordapp.com/attachments/635731474104057857/651094880671629323/sc01.png)

Suite à un sondage réalisé et portant sur la question “Préférez-vous organiser votre planning de
repas pour la semaine ou préférez-vous vous organiser au jour le jour et comment faites-vous
cela ?”, 8 personnes sur 10 préfèrent organiser leur repas pour la semaine entière et utilise une
feuille et un stylo pour réaliser leur planning.
J’ai donc décidé de créer une application web qui permettrait au gens d’organiser leur planning
de repas de la semaine en remplissant un tableau qui contient 7 colonnes, une pour chaque
jour de la semaine.

## Objectif

L’objectif de l’application est de fournir à l’utilisateur un moyen d’organiser son planning de
repas pour la semaine. Il pourra ensuite le consulter et/ou le modifier depuis un navigateur web
(téléphone portable, tablette ou ordinateur).

## Le principe de fonctionnement

L’application fonctionne sur le principe qu’elle est, multi-utilisateurs. Cela veut dire que chaque
utilisateur devra se créer un compte s’il veut avoir accès aux fonctionnalités.

## Les fonctionnalités

- Création d’un compte
- Connexion à un compte
- Création d’un planning
- Modification d’un planning
- Visualisation de son planning
- Visualisation d’un autre planning (système de groupe et de permission)
- Programmation de notification (envoi de SMS à une certaine date et heure)
- Ajout de plat dans la base de données
- Suppression de plat dans la base de données
- Consultation de plat dans la base de données
- Gestion de son compte utilisateur (changement d’informations personnelles, activation ou non des notifications par SMS et suppression de son compte)

#### Note:
*Le système d'envoi de notification par SMS utilise l'API de [Callr](https://www.callr.com/).
/ [Documentation de Callr](https://www.callr.com/pricing/) / 
[Tarifs de Callr](https://www.callr.com/docs/)*

*Si vous déployer l'application, vous devez vous créer un compte sur Callr et renseigner vos identifiants de connexion dans les variables d'environnement.*

*La procédure de mise en production est détaillé dans le fichier "Dossier d'exploitation de l'application Foodplanning" dans le dossier "doc".*
