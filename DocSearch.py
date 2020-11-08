# C1949969
#
# Joseph Wilson-Hall
#
import math
import numpy as np

txtFile = "docs.txt"
queryFile = "queries.txt"
queryWords = []
docWords = []
unique_words = dict()


def get_words(file_path):
    with open(file_path) as textFile:
        return textFile.readlines()


def initialize_file_data():  # this function simply grabs all the data that we are going to use and manipulate
    temp_var = get_words(queryFile)
    for phrase in range(0, len(temp_var)):
        queryWords.append(temp_var[phrase].strip().split())
    temp_var = get_words(txtFile)
    for string in range(0, len(temp_var)):
        docWords.append(temp_var[string].strip().split())


def word_duplicates(): # 
    initialize_file_data()
    lineNumber = 0
    for lines in docWords:
        lineNumber += 1
        for word in lines:
            if word not in unique_words:
                unique_words[word] = []
                unique_words[word].append(1)
                unique_words[word].append([lineNumber])
            else:
                unique_words[word][0] += 1
                unique_words[word][1].append(lineNumber)
    print("Words in dictionary: ", len(unique_words))


def calculate_angle_difference(v1, v2):
    vector_total = 0
    a = 0
    b = 0
    for i in range(0, len(v1)):
        vector_total = vector_total + (v1[i] * v2[i])
        a = v1[i] ** 2 + a
        b = v2[i] ** 2 + b
    a = math.sqrt(a)
    b = math.sqrt(b)
    angle = math.acos(vector_total / (a * b)) * 180 / math.pi  # turning the answer into an angle in degrees
    return angle


def main():
    word_duplicates()
    for line in queryWords:
        j = 0
        relevantDocList = []
        queryVector = np.array([0] * len(unique_words))
        for word in unique_words:
            for queryWord in line:
                if word == queryWord:
                    relevantDocList.append(unique_words[queryWord][1])
                    queryVector[j] = 1
            j += 1
        if len(line) > 1:
            if len(line) == 2:
                if line[0] or line[1] not in unique_words:
                    relevantDocList = set(relevantDocList[0]) & set(relevantDocList[1])
                    print("Relevant documents: "+ str(relevantDocList).replace("{", "").replace("}", "").replace(",", ""))
                else:
                    print("Relevant documents: ")
            if len(line) == 3:
                if line[0] or line[1] or line[2] not in unique_words:
                    relevantDocList = set(relevantDocList[0]) & set(relevantDocList[1]) & set(relevantDocList[2])
                    print("Relevant documents: " + str(relevantDocList).replace("{", "").replace("}", "").replace(",", ""))
                else:
                    print("Relevant documents: ")
        else:
            if line[0] in unique_words:
                for i in line:
                    relevantDocList = []
                    for x in unique_words[i][1]:
                        if x not in relevantDocList:
                            relevantDocList.append(x)
                    print("Relevant documents:", " ".join(map(str, relevantDocList)))
            else:
                print("Relevant documents: ")
        docVector = np.array([0] * len(unique_words))
        output_dictionary = {}
        for lineNumber in relevantDocList:
            for i in range(0, len(unique_words)):
                docVector[i] += 1
                i += 1
            j = 0
            for word in unique_words:
                n = 0
                for dictWord in docWords[lineNumber - 1]:
                    if word == dictWord:
                        n += 1
                docVector[j] = n
                j += 1
            angle = calculate_angle_difference(docVector, queryVector)
            angle = "%.5f" % round(angle, 5)
            y = {lineNumber: angle}
            output_dictionary.update(y)
        output_dictionary = sorted(output_dictionary.items(), key=lambda x: x[1])
        for key in output_dictionary:
            print(" ".join([str(s) for s in list(key)]))


main()
