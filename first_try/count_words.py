# as a test run, let us try to find out about the comments
# that are related to programming

import json, pprint, matplotlib
import matplotlib.pyplot as plt
import related_programming # keyword generator, only for use for this test run

# matplotlib.rcParams.update({'font.size': 8}) # reduces font size so that the graph labels are readable

data = list()
keywords = related_programming.programming_keywords()
keywords = {keywords[i]: 0 for i in range(len(keywords))} # keep track of word count

with open('first_try/RC_2005-12', 'r') as file: # we are given a json file
    for line in file:
        data.append(json.loads(line))

    count = 0 # total number of comments that are related to programming

    # runtime is O(comment_count * keyword_count)
    for comment in data:
        body = comment['body'].lower()
        for kw in keywords:
            if (kw in body):
                count += 1
                keywords[kw] += 1

word_count = list()
words = list()
for key in keywords:
    words.append(key)
    word_count.append(keywords[key])

# bar chart params
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['font.size'] = 8

plt.bar([w[0].upper() + w[1:] for w in words], word_count) # capitalises the first letter of every word

# labels and title
plt.title('Discussion of programming on reddit in 2015 December')
plt.xlabel('Programming terms')
plt.ylabel('Number of times mentioned')

# full screen
plt.get_current_fig_manager().window.state('zoomed')
plt.show()