# DocSearch

## ASSIGNMENT

Write a Python application program (main file called DocSearch.py) that implements document searching
based on vector-based document matching as well as inverted index, as discussed in the lectures.

**Input and Output**. The input to your program involves two text files **docs.txt** which contains all
the documents in the corpus and **queries.txt** which includes all the queries.

The file **docs.txt** is a text file with each line containing the content of a document. To simplify your work,
stopwords and symbols not related to words have already been removed, and letters have been converted
to lower case. You should treat any consecutive sequence of characters separated by whitespace in the
documents as a word. When referring to a document, we use its ID, a number consecutively assigned to
each document as it appears in **docs.txt**. So the first line in **docs.txt** is the document with ID 1, the
second line ID 2, etc.

The file **queries.txt** is a text file with each line containing a query. Each query is composed of one or more
words in lower case, separated by whitespace. A query may contain words not appearing in any of the
documents, and in which case such words should be ignored in matching.

For output, print the required messages (see details below and sample outputs overleaf) following exactly
the same format (except for the actual number of whitespace characters) as specified and as in the examples.

**Building the Dictionary**. Your program should build a dictionary containing all the unique words in
the corpus. For simplicity, we treat words with any different character as different words. So for example,
system and systems are treated as different words, even though they are just different morphological forms.
Print the number of unique words in the dictionary (“Words in dictionary: number”).

**Building Inverted Index**. Your program should also build an inverted index listing all the documents
associated with each word in the dictionary.

**Document Searching**. For each query (each line in **queries.txt**), your program should perform the
following:

• Print the query in a line “Query: query”.
• Using the inverted index, find all the documents that contain all the words in the query (except for words not in the dictionary which are ignored). Print a line containing “Relevant documents: list of document IDs”, where list of document IDs are IDs of relevant documents separated by
whitespace. The IDs can appear in any order. If none of the documents contain all the words in the
query, list of document IDs should be empty.
• For documents in the list above, work out the angle (in degrees) between the search query and each
document, and print in the order from most relevant to least relevant the list of documents, one per
line. Each line contains two numbers, the document ID and the angle (in degrees with at least 2 digit
fractional accuracy), separated by whitespace. Note:

  – When representing a document as a vector, each vector component represents the number of times
  the corresponding word in the dictionary appears in the document.
  – When representing a search query as a vector, each vector component represents whether the
  corresponding word in the dictionary appears in the search query (1 if it does and 0 otherwise).
  – If two items are equally similar, they can appear in any order.
  
Error checking is not required (invalid input, etc.) Remember that I will perform extensive tests on your
program, using more than just the test data I have provided.

Hint: The Week 6 lab includes exercises related to handling text files using Python, which can be useful.
Several further testcases and their expected output are provided on learning central.
