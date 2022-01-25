# wordle_bot
bot that solves wordle, i dont know what else to tell you

python script to solve/help solve wordle given initial guess(es)

Usage:
python wordlebot.py

Example uses Wordle word = TANGY
```
> How many words used so far?: 
>  2
>   
> Word used: 
>   NOTES
>   
> Enter G/O (green/orange), letter used, and position in the word (1-5). Enter Q if complete:
>   O N 1
>   O T 3
>   Q
>   
> Word used:
>   ACRID
>   
> Enter G/O (green/orange), letter used, and position in the word (1-5). Enter Q if complete:
>   O A 1
>   Q
>   
>   Results
> 1: TANGA
> 2: TANKA
> 3: TANTA
> 4: TANYA
> 5: TANGY
> 6: TAUNT
> 7: TAWNY
> 8: MANTA
> 9: BANTU
> 10: PANTY
> 11: MANAT
> 12: GAUNT
> 13: HAUNT
> 14: JAUNT
> 15: VAUNT
> 16: THANA
> 17: TWANG
> 18: THANH
> 19: THANK
> 20: THANT
> 21: UNAPT
> 22: PLANT
> 23: QUANT
> 24: JUNTA
> 
> Enter spaced digits of words to take through: # (i.e. which ones look like they could realistically be the answer, cause who tf heard of 'THANH')
>   5 6 7 10 12 13 14 17 19 22 23
>   
> CHOSEN: TANGY
> CHOSEN: TAUNT
> CHOSEN: TAWNY
> CHOSEN: PANTY
> CHOSEN: GAUNT
> CHOSEN: HAUNT
> CHOSEN: JAUNT
> CHOSEN: TWANG
> CHOSEN: THANK
> CHOSEN: PLANT
> CHOSEN: QUANT
> 
> Best words to use next:   # These words are the most effective at deducing the correct word on the next go
> ['TANGY', 'GAUNT', 'TWANG']
> Not guaranteed to confirm correct word in the next go.
```
