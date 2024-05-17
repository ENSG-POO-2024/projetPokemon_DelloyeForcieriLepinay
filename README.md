# PyQTMon

* Noé DELLOYE noe.delloye@ensg.eu
* Sarah FORCIERI sarah.forcieri@ensg.eu
* Fabien LÉPINAY fabien.lepinay@ensg.eu

## Le Code :

### Explication du jeu :

  Le but du jeu est de capturer le plus de Pokémons dans le monde qui est proposé au joueur. La majorité des pokémons sont répartis dans différentes zones de recontres (Voir ./images/zonages.png) et peuvent y être rencontrés soient dans les hautes herbes, soient dans le sable du désert, soit dans les grottes. Ils peuvent être également pêchés à proximité des pontons de pêche. D'autres pokémons (les légendaires) sont uniques et ont des interactions sur la carte.
  Les pokémons sont capturés automatiquement lorsqu'ils sont vaincus.

  Le joueur possède une équipe de 6 Pokémons maximum et a également un PC où il peut stocker et agencer tous les pokémons supplémentaires. Il peut également agencer les Pokémons de son équipe dans le menu Equipe. Il peut enfin soigner ses pokémons au centre pokémon. 

  Les combats se font au tour par tour. Le pokémon le plus rapide attaque en premier. Il se finit lorsque les PVs du pokémon adverse sont à zéro, ou bien si le joueur n'a plus aucun pokémon apte au combat. 

#### Interaction — Wikipédia avec le monde.
#### Initialement :
  - Choisir son pokémon de départ avec les fléches directionnelles et la barre espace.

##### Sur la carte :

Le joueur peut :
- Se déplacer en appuyant sur les touches directionnelles.
- Changer de zone en se déplaçant vers une porte.
- Pêcher en appuyant sur espace sur un ponton en face d'une case d'eau.
- Interagir avec un pokémon légendaire, en appuyant sur Espace en face d'un pokémon légendaire.
- Entrer dans le menu de gestion d'équipe en appuyant sur Entrée (Celui du pavé numérique)
- Soigner ses pokémons en appuyant sur Espace en face de l'infirmière du centre Pokémon.
- Ouvrir son PC en appuyant sur espace en face du PC dans le centre pokémon.

##### En combat
Le joueur peut :
- Naviguer dans les menus avec les fléches directionnelles.
- Choisir son action, avec Espace
  Dans le menu choix :
    * Attaquer (Ouvre le menu combat)
    * Changement (Ouvre le menu de gestion d'équipe)
    * Potion (Soigne le pokémon de 150PVs mais le pokémon adverse attaque)
    * Fuite (Finit le combat sans capturer de Pokémon.
  Dans le menu Attaque :
    - Choisir son attaque (Le tour se résout -> Le pokémon le plus rapide attaque)
  Dans le menu Gestion Equipe :
    - Cliquer sur le Pokémon à passer en première position (Change le pokémon que le pokémon adverse attaque)
 
##### Dans le PC :
  - Agencer son équipe ou son PC avec les boutons ajouter et déposer.

##### Dans le menu Equipe :
  - Agencer son équipe en cliquant sur le pokémon à mettre en première position.

### Explication des répertoires:

* Le répertoire est arrangé ainsi
  1. main.py : Fichier principal qui execute tout le code. 
  2. CarteEtSprite.py : Interface qui gère tout ce qui a attrait à la carte, 
  3. `Type 1` : le type du pokemon
  4. `Type 2` : le second type du pokemon (s'il en possède un deuxième)
  5. `Total` : le nombre total de points d'attributs (HP + Attack + Defense + Sp. Attack + Sp. Def + Speed)
  6. `HP` : le nombre de point de vie de départ
  7. `Attack` : le nombre de point d'attaque (coefficient pour les dégats infligés)
  8. `Defense` : le nombre de point de défense (coefficient pour les dégats reçus)
  9. `Sp. Atk` : le nombre de point d'attaque spéciale (coefficient pour les dégats infligés)
  10. `Sp. Def` : le nombre de point de défense contre une attaque spéciale (coefficient pour les dégats reçus)
  11. `Speed` : la vitesse du pokemon (détermine qui joue en premier)
  12. `Generation` : la génération du pokemon (ici la première)
  13. `Legendary` : rareté du pokemon, les légendaires sont normalement uniques

* Un fichier csv contenant une liste de pokemons avec des coordonnées géographiques.

## Comment créer votre dépôt github ?

1. Se créer un identifiant github
2. Demander à un enseignant de vous ajouter dans l'organisation **ENSG-POO-2024**
3. *Forker* (copier) le projet **projetPokemon** et choisissez un nom très personnalisé !
4. Pour voir comment établir une connexion ssh entre votre ordinateur et github, voir documents/sshConnexion.md
