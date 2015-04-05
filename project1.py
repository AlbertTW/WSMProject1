from VectorSpace import VectorSpace
from pprint import pprint
from Parser import Parser

import os
import util
import re
import nltk

fileName = "wsm_essays_small.txt"
try:
    file = open(fileName, "r")
except IOError:
    print "Could not open file wsm_essays_small.txt."

documents = []
i = 0
for line in file:
    if i < 10:
        stringToBeReplaced = line[0] + ":::"
        line = line.replace(stringToBeReplaced, "")
    elif i < 100:
        stringToBeReplaced = line[0] + line[1] + ":::"
        line = line.replace(stringToBeReplaced, "")
    else:
        stringToBeReplaced = line[0] + line[1] + line[2] + ":::"
        line = line.replace(stringToBeReplaced, "")
    i += 1
    line = line.replace("\\n", "")
    line = re.sub("[\r\n:?~;/().!,]", "", line)
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
print "Question 1. Term Frequency (TF) Weighting + Cosine Similarity:"
vectorOfQ1 = vectorSpace.search(queryList)
print "\t\tDocID\tScore"
print

def sortAndPrintFirst5(vector):
    sortedIndex = [i[0] for i in sorted(enumerate(vector), key = lambda x:x[1])]
        #myList = [1, 2, 3, 100, 5]
        #[i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
    for i in range(1, 6):
        print "\t\t", sortedIndex[1000-i], "\t", vector[sortedIndex[1000-i]]

sortAndPrintFirst5(vectorOfQ1)
print


print "Question 2. Term Frequency (TF) Weighting + Jaccard Similarity:"
vectorOfQ2 = searchWithJaccardSimilarity(queryString)
print "\t\tDocID\tScore"
print
sortAndPrintFirst5(vectorOfQ2)
print


print "Question 3. TF-IDF Weighting + Cosine Similarity:"
print "\t\tDocID\tScore"
print
vectorSpace.searchWithTfIdf(queryList)
print


print "Question 4. TF-IDF Weighting + Jaccard Similarity:"
print "\t\tDocID\tScore"
print
sortAndPrintFirst5(vectorOfQ2)
print

print "Question 5. Feedback Queries + TF-IDF Weighting + Cosine Similarity:"
print "\t\tDocID\tScore"
print
topRankedId = vectorSpace.getTopRankedId()
topRankedDoc = documents[topRankedId]
tokens = nltk.word_tokenize(topRankedDoc)
text = nltk.Text(tokens)
tags = nltk.pos_tag(text)
nounAndVerbAttribute = ["NN", "NNS", "NNP", "NNPS", "VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
i = 0
while(i < len(tags)):
    #print "i = ", i, tags[i][0], tags[i][1]
    if tags[i][1] not in nounAndVerbAttribute:
        #print "delete", tags[i][0]
        del tags[i]
        i -= 1
    i += 1
#print tags
newDoc = []
for word in tags:
    newDoc.append(word[0])
'''from collections import Counter
counts = Counter(tag for word, tag in tags)
print counts
print newDoc'''
newDoc = " ".join(newDoc)
#print newDoc
#print topRankedId, ":", topRankedDoc
vectorSpace.relevanceFeedback(newDoc, queryList)
print

file.close()
###########################################
