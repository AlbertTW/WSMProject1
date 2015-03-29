from VectorSpace import VectorSpace
from pprint import pprint
from Parser import Parser

import os
import util

fileName = "wsm_essays_small.txt"
try:
    file = open(fileName, "r")
except IOError:
    print "Could not open file wsm_essays_small.txt."

documents = []
for line in file:
    documents.append(line)
vectorSpace = VectorSpace(documents)

def searchWithJaccardSimilarity(query):
    parser = Parser()
    ratings = []
    queryWords = parser.tokenise(query)
    queryWords = parser.removeStopWords(queryWords)
    queryWords = util.removeDuplicates(queryWords)
    for document in documents:
        documentWordList = parser.tokenise(document)
        documentWordList = parser.removeStopWords(documentWordList)
        uniqueDocumentWordList = util.removeDuplicates(documentWordList)
        intersection = set(queryWords).intersection(uniqueDocumentWordList)
        union = set(queryWords).union(set(uniqueDocumentWordList))
        ratings.append(float(len(list(intersection)))/float(len(list(union))))
    return ratings

queryString = raw_input("Please input a query:")
print "Processing..."
print queryString.split()
queryList = []
queryList.append(queryString)
print
print
'''print "Question 1. Term Frequency (TF) Weighting + Cosine Similarity:"
vectorOfQ1 = vectorSpace.search(queryList)

print "\t\tDocID\tScore"'''

def sortAndPrintFirst5(vector):
    sortedIndex = [i[0] for i in sorted(enumerate(vector), key = lambda x:x[1])]
        #myList = [1, 2, 3, 100, 5]
        #[i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
    for i in range(1, 6):
        print "\t\t", sortedIndex[1000-i], "\t", vector[sortedIndex[1000-i]]

'''sortAndPrintFirst5(vectorOfQ1)
print'''


print "Question 2. Term Frequency (TF) Weighting + Jaccard Similarity:"
vectorOfQ2 = searchWithJaccardSimilarity(queryString)
print "\t\tDocID\tScore"
sortAndPrintFirst5(vectorOfQ2)
print


'''print "Question 3. TF-IDF Weighting + Cosine Similarity:"
print "\t\tDocID\tScore"
pprint(vectorSpace.search(Query))
print'''


print "Question 4. TF-IDF Weighting + Jaccard Similarity:"
print "\t\tDocID\tScore"
sortAndPrintFirst5(vectorOfQ2)
file.close()
###########################################
