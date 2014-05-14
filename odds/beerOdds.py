# what are the odds of two people choosing four distinct numbers out of
# 103 numbers, and their two selections having an overlap of two numbers?
from random import sample

numBeers = 103
numPeople = 2
selectNum = 4
overlap = 2
print "there are {0} beers!".format(numBeers)
print "there are {0} people.".format(numPeople)
print "they all make a selection of {0} beers".format(selectNum)
print "what are the odds that {0} beers overlap?".format(overlap)

top = 1.0;
bottom = 1.0;
def f(a):
    if(a < 2):
        return 1
    else:
        return a * f(a-1)
def c(fro, ch):
    a = f(fro) / (f(ch) * f(fro - ch))
    return a

top *= c(selectNum, overlap)
top *= c(numBeers - selectNum, selectNum - overlap)
bottom *= c(numBeers, selectNum)

probability = top * 1.0/bottom
percent = probability * 100
print
print "according to combinatoric calculations:"
print "  probability is {0} over {1}, or {2:0.09f}%".format(top, bottom, percent)
against = 1 - probability
odds = against / probability
print "  odds are {0:0.3f} to one against".format(odds)

print

# monte carlo approach
total_attempts = 1000000
print "making {0} beer selection simulations".format(total_attempts)
print

choices = range(1, numBeers + 1)
numMatchRequirements = 0
for attempt in range(0, total_attempts):
    selections = [sample(choices, selectNum) for person in range(0, numPeople)]
    matches = sum([all([(firstSelection in y) for y in selections[1:]]) for firstSelection in selections[0]])
    if(matches == overlap):
      numMatchRequirements += 1

print
print "according to my simulations:"
print "  {0} out of {1} selections had {2} beers overlapping".format(numMatchRequirements, total_attempts, overlap)
probability = numMatchRequirements * 1.0 / total_attempts
percent = probability * 100
print "  percent is {0:0.3f}%".format(percent)
against = 1 - probability
odds = against / probability
print "  odds are ~ {0:0.3f} to one against".format(odds)
