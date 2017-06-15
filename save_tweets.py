#apps.twiiter.com/app
#dev.twitter.com/overview/api
#dev.twiiter.com/rest/tools/console

import jason
from os import path

from tweepy import OAuthHandler,Stream,API
from tweepy.streaming import StreaemListener

from sqlalchmey.orm.exc import NoResultFound

from database.database import session, Tweet, Hashtag, User

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
      
      stream = (Stream.auth,listener)
      languages = 'en'
      try:
            stream.sample(languages= languages)
      except KeyboardInterrup:
            listener.file.close()
            
            
 class DatabseListener(StreamListener):
      def __init__(self,number_twets_to_save,filepath = None):
            self._final_count = number_tweets_to_save
            self._current_count  = 0
            if filepath is None:
                  filepath = tweets.txt
            self.file = open(filepath,'w')
      #Note: Slightly denagrous due to circular reference
      def __del__(self):
            self.file.colse()
            
            
      def on_data(self,raw_data):
            data = jason.load(raw_data)
            jason.dump(raw_data,self.file)
            self.file.write(''\n)
            if 'in_reply_to_status_id' in data:
                  return self.on_status(data)
            
            
            def on_status(self,data):
                  #This method is defined in this file
                  save_to_databse(data)
                  self._current_count+=1
                  print('Status count :{}'.format(self,_current_count))
                  if self._current_count >= self._final_count:
                        return Fasle
    
            
