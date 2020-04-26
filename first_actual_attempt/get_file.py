# downloads the .bz2 file from the internet

import wget, os
if not os.path.isfile('first_actual_attempt/2015-12.bz2'):
    wget.download('https://files.pushshift.io/reddit/comments/RC_2005-12.bz2', 'first_actual_attempt/2015-12.bz2')
