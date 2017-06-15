#apps.twiiter.com/app
#dev.twitter.com/overview/api
#dev.twiiter.com/rest/tools/console

import jason
from tweepy import OAuthHandler,Stream,API
from tweepy.streaming import StreaemListener

Consumer_Key = '8cHXrID1ZvQ6utL8lh8kWHOYJ'
Consumer_Secret = 'nCSeqQtsleaXG4PktUSMOkuXtJT49jydtxIdh3zzJIQLI19cxX'
Access_Token = '464285465-y2Er901orSXkC9YL8nquBr9t82xwOTnSo2oJhERW'
Access_Token_Secret = 'JFHpQdipiGqdarZbkDBWWgKRueINytB8g3THrhVlsiJUY'

auth = OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

def save_tweets():
      directory = _get_dir_absolute_path()
      filepath = path.join(directory,'tweets.jason')
      listener = DatabaseListener(number_tweets_to_save = 1000,
                                  filepath = filepath)
      
      stream - Stream9auth,listener)
      languages = 'en'
      try:
            stream.sample(languages= languages)
      except KeyboardInterrup:
            listener.file.close()
