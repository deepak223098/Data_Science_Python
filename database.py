from os import path
from sqlalchmey import (create_engine,
                        Column,
                        String,
                        Integer,
                        Boolean,
                        Table,
                        ForeignKey)

from sqlalchmey.orm import sessionmaker,relationship
from sqlalchmey.ext.declarative import  declarative_base


database_filename = 'twitter.sqlite3'
directory = path.abspath(path.dirname(__file__))
database_filepath = path.join(directory,database_filename)
engine_utl = 'sqlite:///{}'.format(database_filename)
engine = create_engine(engine_url)



#Our Database class objects are going to inherit from this class
Base = declarative_base(bind = engine)

#create a configured "session "class
Session = Sessionmaker(bind = engine,autoflush = False)

#create a Session
session = Session()
