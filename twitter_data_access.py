import jason
from tweepy import OAuthHandler,Stream,API
from tweepy.streaming import StreaemListener

Consumer_Key = '8cHXrID1ZvQ6utL8lh8kWHOYJ'
Consumer_Secret = 'nCSeqQtsleaXG4PktUSMOkuXtJT49jydtxIdh3zzJIQLI19cxX'
Access_Token = '464285465-y2Er901orSXkC9YL8nquBr9t82xwOTnSo2oJhERW'
Access_Token_Secret = 'JFHpQdipiGqdarZbkDBWWgKRueINytB8g3THrhVlsiJUY'

auth = OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)

Class PrintListener(StreamListerner):
      def on_status(self,status):
            if not status.text[:3] == 'RT': 
                  print(status.text)
                  print(status.author,screen_name,status.created_at,status.cource,'\n')
  
      def on_error(self,status_code):
            print("Error Code: {}".format(status_code))
            return True #Keep Stream alive
      def on_timeout(self):
                  print("Listener timed out")
                  return True #Keep Steam alive
                  
                  
def print_to_terminal():
                listener = PrintListener()
                stream = Stream(auth,listener)
                languages = (en',
                stream.sample(languages=languages
                
                              
                              
def pull_down_tweets(screen_name):    
                              api = API(auth)
                              tweets = api.user_timeline(screen_name = screen_name,count = 200) 
                              for tweet in tweets:
                                    print(jason.dumps(tweet._json,ident = 3))
                              
                
if __name__ =='__main__':
         #print_to_terminal()
         pull_down_tweets(auth.username)
  
