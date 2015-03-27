from VectorSpace import VectorSpace
from pprint import pprint
import os

fileName = "testInput.txt"
try:
    file = open(fileName, "r")
except IOError:
    print "Could not open file wsm_essays_small.txt."

documents = []
for line in file:
    documents.append(line)
vectorSpace = VectorSpace(documents)
query = raw_input("Please input a query:")
print "Processing..."
print query.split()
Query = []
Query.append(query)
print
print
print "Question 1. Term Frequency (TF) Weighting + Cosine Similarity:"
print "\t\tDocID\tScore"
print(vectorSpace.search(Query))
print
print "Question 2. Term Frequency (TF) Weighting + Jaccard Similarity:"
print "\t\tDocID\tScore"
pprint(vectorSpace.search(Query))
print
print "Question 3. TF-IDF Weighting + Cosine Similarity:"
print "\t\tDocID\tScore"
pprint(vectorSpace.search(Query))
print
print "Question 4. TF-IDF Weighting + Jaccard Similarity:"
print "\t\tDocID\tScore"
pprint(vectorSpace.search(Query))
file.close()
###########################################
