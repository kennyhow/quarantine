# file is at first_actual_attempt/2015-12.bz2
# read the file line by line, and stores the data

import bz2, json, related_programming
data = list()

# open and read file
with bz2.open('first_actual_attempt/2015-12.bz2') as file:
    for line in file:
        # type(line) is bytes; we decode it to a string here
        data.append(json.loads(line.decode("utf-8")))

# programming related words
keywords = related_programming.programming_keywords()
keywords = {keywords[i] : 0 for i in range(len(keywords))}

# TODO: process data