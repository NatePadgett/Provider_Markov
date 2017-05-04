import sys
import Markov_Example
import re

def split_upper(s):
    return filter(None, re.split("([A-Z][^A-Z]*)", s))

text = sys.stdin.read()
model = Markov_Example.build_model(split_upper(text), 6) #text.split(), )
generated = Markov_Example.generate(model, 6)
print ' '.join(generated)
