# PyQTMon

* Noé DELLOYE : noe.delloye@ensg.eu
* Sarah FORCIERI : sarah.forcieri@ensg.eu
* Fabien LÉPINAY : fabien.lepinay@ensg.eu

## Le Code :

Fichier à lancer : main.py

### Explication du jeu :

  Le but du jeu est de capturer le plus de Pokémons dans le monde qui est proposé au joueur. La majorité des pokémons sont répartis dans différentes zones de recontres (Voir ./images/zonages.png) et peuvent y être rencontrés soient dans les hautes herbes, soient dans le sable du désert, soit dans les grottes. Ils peuvent être également pêchés à proximité des pontons de pêche. D'autres pokémons (les légendaires) sont uniques et ont des interactions sur la carte.
  Les pokémons sont capturés automatiquement lorsqu'ils sont vaincus.

  Le joueur possède une équipe de 6 Pokémons maximum et a également un PC où il peut stocker et agencer tous les pokémons supplémentaires. Il peut également agencer les Pokémons de son équipe dans le menu Equipe. Il peut enfin soigner ses pokémons au centre pokémon. 

  Les combats se font au tour par tour. Le pokémon le plus rapide attaque en premier. Il se finit lorsque les PVs du pokémon adverse sont à zéro, ou bien si le joueur n'a plus aucun pokémon apte au combat. 

### Interactions :

#### Initialement :
  - Obtenir ses premiers pokémons auprès du prof Chen (Barre Espace)

##### Sur la carte :

Le joueur peut :
- Se déplacer en appuyant sur les touches directionnelles.
- Changer de zone en se déplaçant vers une porte.
- Pêcher en appuyant sur Espace sur un ponton en face d'une case d'eau.
- Interagir avec un pokémon légendaire, en appuyant sur Espace en face d'un pokémon légendaire.
- Entrer dans le menu de gestion d'équipe en appuyant sur Entrée (Celui du pavé numérique)
- Soigner ses pokémons en appuyant sur Espace en face de l'infirmière du centre Pokémon.
- Ouvrir son PC en appuyant sur Espace en face du PC dans le centre pokémon.

##### En combat :
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

##### Dans le PC : 
  - Agencer son équipe ou son PC avec les boutons ajouter et déposer.

##### Dans le menu Equipe :
  - Agencer son équipe en cliquant sur le pokémon à mettre en première position.

### Explication des répertoires :

* Le répertoire est arrangé ainsi
  1. main.py : Fichier principal qui execute tout le code. 
  2. CarteEtSprite.py : Interface qui gère tout ce qui a attrait à la carte, 
  3. Deplacement.py : Gère tous les déplacements du joueur sur la carte.
  4. CombatUI.py : Gère l'interface de combat.
  5. Menus.py : Gère le menu de Gestion d'Equipe
  6. PC.py : Gère l'interface du PC
  7. Intro.py : Sert à l'affichage du bloc d'interface dédié au prof chen. 
  8. GestionCombat : Gère les mécaniques du PC et de l'équipe
  9. Mecaniques : Gère la création de Pokémons, les attaques...etc.
  10. Conversion_Image_Collison.py : Un outil qui permet de facilement convertir une carte en matrice de collision.
  11. Gestion_Son.py : Objet pour gérer les changements de musiques. 
  12. Animation/Temp/Images/Map/Audio : Des dossiers contenant les sprites/cartes/fichiers audios...etc nécessaire à l'affichage graphique. 
  13. data/documents : Dossiers contenant la matrice de collision et les données initiales (Pokédex notamment)
