**OVERVIEW**

[Midlake](https://www.facebook.com/midlakeband/) is one of my favorite bands and their fourth album [Antiphon](http://pitchfork.com/reviews/albums/18696-midlake-antiphon/) is generally on repeat two weeks out of a given month. The second song on that album, "Provider", has always struck me as incredibly beautiful, particularly lyrically, so I wanted to use it as my source for this assignment. 

With Provider_Markov, I experimented with Markov chains. I used [a model](https://github.com/NatePadgett/Provider_Markov/blob/master/Markov_Model.py) previously written by Allison Parrish and based my script for re-organizing the text on her word and character level processing [examples](http://www.decontextualize.com/teaching/rwet/n-grams-and-markov-chains/).

**CODE**

With the exception of the Markov Model written by Allison, the code for this project is quite simple. In my main script, [Organized_Provider.py](https://github.com/NatePadgett/Provider_Markov/blob/master/Organized_Provider.py) I strip out each line of my source text [Midlake_Provider.txt](https://github.com/NatePadgett/Provider_Markov/blob/master/Provider_by_Midlake.txt) and add them to a list. 

```lines = list()

for line in open("Midlake_Provider.txt"):
    line = line.strip()
    lines.append(line)
```
    
Once I have populated the list with all of the lines from the source text, I print the title and body of the poem. 

The title is achieved by printing the results of a call to function `Markov_Example.word_level_generate`. 

```print "\n".join(Markov_Example.word_level_generate(lines, 1, count=1))```

I use `.join` to make the result a string. 

This produces a higher level n-gram, which consistently produces more readable texts than a lower level n-gram like `char_level_generate`. 

For the body of the poem, I join the results of a call to function `Markov_Example.char_level_generate` along new line breaks.

```print "\n".join(Markov_Example.char_level_generate(lines, 5, count=15))```

I can tweak the n-gram lengths and number of lines to return to get different results. I have uploaded three of my favorite results. 

[Winter Came as I Was Old and Alone](https://github.com/NatePadgett/Provider_Markov/blob/master/Winter_came_and_I_was_old_and_alone.txt)

[Far From The Golden Age](https://github.com/NatePadgett/Provider_Markov/blob/master/Far_from_the_golden_age.txt)

[Don't Delay](https://github.com/NatePadgett/Provider_Markov/blob/master/Dont_Delay.txt)

