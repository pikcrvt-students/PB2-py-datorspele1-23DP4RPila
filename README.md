# Akmens, šķēres, papīrīts 
 Spēles valoda - Angļu

Spēlētāji: Lietotājs pret datoru

Spēles kārtība:

1. Izvada ziņojumu `input` ar iespēju ievadīt atbildi - spēlēt spēli: akmens, šķēres, papīrīts, 
ievadīt kādu no derīgajiem `str` elementiem. - `rock`, `paper`, `scissors`.
2. Pēc ievades un `Enter` nospiešanas, tiek izvadīts lietotāja ASCII art seja ar atbilstošo lietotāja izvēlēto objektu ASCII art stilā - akmens, šķēres vai papīrīts.
Tiek izvadīta robota ASCII art seja ar atbilstošo ASCII art elementu
3. Tiek izvadīts spēles iznākums - uzvara, zaudējums vai neizšķirts (`win`, `loss` vai `draw`)
4.  Spēle atkārtojas vēl 4 reizes un beigās tiek izvadīts Uzvaru, zaudējumu, neizšķirtu rezultātu un, ja tādi ir, tad izvada arī nederīgu rezultātu skaits.

Programmas kārtība:


# Spēles ASCII art elementi:
```
Spēlētāju izskats:

Lietotājs(cilvēks):

  O O
   -
\_____/  

Dators(robots):
  -------
 /        \
|  O   O  |
|         |   
 \  ---  /
  -------

Spēles elementu izskats:

Akmens:
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)

Papīrs:
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)

Šķēres:
         _______        
     ---'   ____)____         
               ______)            
            __________)              
           (____)          
     ---.__(___)           

Spēles iznākumu ASCII art:

Uzvara
 __      _____ _  _
 \ \    / /_ _| \| |
  \ \/\/ / | || .` |
   \_/\_/ |___|_|\_|

Zaudējums: 
  _    ___  ___ ___
 | |  / _ \/ __/ __|
 | |_| (_) \__ \__ \
 |____\___/|___/___/

Neizšķirts
     ___  ___    ___      __
    |   \| _ \  /_\ \    / /
    | |) |   / / _ \ \/\/ /
    |___/|_|_\/_/ \_\_/\_/
```