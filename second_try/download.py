# downloads file containing comments and converts to json

import wget, json, bz2, os
if(not os.path.isfile('second_try/tmp.bz2')):
    wget.download('https://files.pushshift.io/reddit/comments/RC_2005-12.bz2', 'second_try/tmp.bz2')

with bz2.open("second_try/tmp.bz2") as file:
    for line in file:
        data = json.loads(line.decode("utf-8"))
        break
print(data['body'])