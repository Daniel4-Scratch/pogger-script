# Examples

## Number guess
This is a simple number guessing game where the user has to guess a number between 0 and 10. The game will save the state of the game using `memSave` and `memLoad`.
The game will also ask the user if they want to play again after winning or losing.
This game can also be used to demonstrate the capability of archive/executable files.
### Structure
```
numberGame.pogx
├── main.pog
├── win.pog
├── loose.pog
└── no.pog
```
### Code
main.pog
```
int:number:0
rnd:0:10:number
inp:guess:Enter a number between 0 and 10> 
cnv:(guess):int:guess
memSave:numberGameData
if:(guess):==:(number):win.pog:loose.pog
```
win.pog
```
yap:You won!
inp:input:Do you want to play again? (yes/no)
if:(input):==:yes:main.pog:no.pog
```
loose.pog
```
memLoad:numberGameData
yap:You lost! The number was
yap:(number)
inp:input:Do you want to play again? (yes/no)
if:(input):==:yes:main.pog:no.pog
```
no.pog
```
yap:Bye!
```