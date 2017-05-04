import Markov_Example

lines = list()

for line in open("Midlake_Provider.txt"):
    line = line.strip()
    lines.append(line)

print "\n".join(Markov_Example.word_level_generate(lines, 1, count=1))
print " "
print "\n".join(Markov_Example.char_level_generate(lines, 5, count=15))
