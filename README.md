# reptangles
A simple tile based game of tangled turtles written in python.

This game is inspired by and meant to somewhat be a clone of [Entanglement](https://entanglement.gopherwoodstudios.com/) by [Gopherwood Studios](https://www.gopherwoodstudios.com/). A game that I find highly enjoyable and I recommend checking out. It is also [available on Steam](https://steamcommunity.com/app/719140).

This "clone" however while inspired by Entanglement is going to differ in several ways: 

* Its free and open source.
* Initially I am only programming it to have 4 sided square tiles.
* Its written in python using standard library.
* Initially it will not be as flashy in graphics and sound, but will have a more elementary look and feel.
* There will be actual players moving on the board (turtles).
* Focus will be on adding gameplay variations, online multiplayer, etc.
* It will run anywhere python runs.
  
ANY help developing this game would be greatly appreciated. As of right now the code is runnable but doesn't really do much of anything.

My future vision for this game includes the following gameplay ideas:

* Play with at least 3, 4, and 6 sided tiles (Triangle, Square, Hexagon).
* Start tile players start on can be either one tile all players start on or each player starts with their own tile.
* Start tile can be static or random.
* Swap tiles can be shown or not shown until swapped.
* Limit number of swaps.
* Start with predefined set of tiles and choose one to play one each turn.
* Limit or unlimted number of turns.
* Different board shapes and styles including infinite (unbordered).
* Play with pre-set tiles already on the board.
* Different scoring options and algorithms.
* Various AI computer opponents.
* A name generator for online play to add some amusement value while maintaining family friendly names.
* Background graphics, sounds, and animations.
* Possibly even play with odd shaped tiles that won't cleanly tesselate (like octogons or pentagons) by using pre-placed tiles that fill in the gaps.
* Invisible tiles, where the paths are only shown when you enter the tile.
* Possibly even 2.5d (think Qbert) or multi shaped tiles (hexagons made up of 6 triangle tiles for example).
* Different randomization modes such as client-side, server-side, pre-game, per-turn, etc.
* Possibly add alternate collision modes like drawing over a player's path rather than terminating upon colision (scoring mode difference).

Shown below are some example screenshots of what some tiles would look like made using my [PTSG](https://github.com/enveezee/ptsg) program:
![Square Tiles](SquareTiles.png?raw=true "Square Tiles")
![Triangle Tiles](TriangleTiles.png?raw=true "Triangle Tiles")

Screenshots of the Initial GUI design:
![Main Menu](MainWindow.png?raw=true "Main Menu")
![Game Options](GameOptions.png?raw=true "Game Options")
![Game Screen](GameWidow.png?raw=true "Game Screen")