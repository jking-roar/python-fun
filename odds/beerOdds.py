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

print

# monte carlo approach
total_attempts = 200000

choices = range(1, numBeers + 1)
numMatchRequirements = 0
for attempt in range(0, total_attempts): 
    selections = [sample(choices, selectNum) for person in range(0, numPeople)]
    matches = sum([all([(firstSelection in y) for y in selections[1:]]) for firstSelection in selections[0]])
    if(matches == overlap):
      numMatchRequirements += 1


print "there were {0} out of {1} samples where {2} beers were overlapping with all the selections".format(numMatchRequirements, total_attempts, overlap)
print "that is {0:0.3f}%".format(numMatchRequirements * 100.0 / total_attempts)
