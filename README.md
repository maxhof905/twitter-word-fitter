# Masomo Studios

Language Technology and Web Applications  
Fall Semester 2021

Code for team project

---

URL of website: not active anymore

Database Connection URI: not active anymore

---

## How to play
Once you open the link above, you'll be presented with a selection of three different
game modes and their descriptions. Choose the one you like best by pressing the play button
below it.

### Word guessing
Within the game modes *Missing words* and *#nofilter* you can choose which type of word[^1] you 
would like to guess:
- Nouns (default)
- Verbs
- Adjectives

Just press the labeled buttons to switch between these modes. Press the green check button to submit your input,
and you will receive a score between 0 and 10 as well as the solution.


### Emoji guessing
In this mode you will be presented with a choice of four different emojis. Click the one 
you think is right. In this mode you can only be right 
or wrong, so you will receive a yay or nay as feedback together with the solution.

## Stats and technical info
The full database available stores a total of about 3'000 tweets, they are accessible in the *#nofilter* game mode. We 
filtered these with the following methods to retain only the safe for work and fun tweets:
- containing emojis (generally more lighthearted topics)
- not containing profanities
- hand selection for appropriate subjects

After these steps only about 90 suitable tweets remained, which are the basis for the standard *missing words* and
*missing emojis* game modes.

The scoring is done by a combination of the Levensthein distance, to account for slight differences in spelling as well 
as typos, the spaCy similarity measure of the large english corpus and finally the dice coefficient as a fallback in 
case spaCy isn't able to recognize either the users solution or the real word. 


---
##### Footnote:
[^1]: Please note the POS-tagging was done automatically by spaCy and may not always be correct
