# Database

> Most of the bots we're use rigth now need some kind of persistent data storage. We are covering that in this section.

## Configuring

Databases are configured into DB in settings.py file. The basic configuration is a good example.

```python
DB={
    'backend': 'easy_tbot.contrib.db.alchemy.SqlAlchemyBackend',
    'config': {
        'url':'sqlite:///./sqlite.db'
        }
}
```

## Where to define models?

Inside our shards we are going to find a models.py that we can populate with models. A model is an object if you are using SqlAlchemyBackend is based on the ORM of SqlAlchemy's package  that represents a table in a database and is usefull as a representation of the data in our code.

## How to define models?

Now an example of a model definition in our model.py .

```python
from easy_tbot.contrib.db.alchemy import model
from sqlalchemy import Column, Integer, String

Model = model()
# Write your models in here

class UserGameProfile(Model):
    '''A sample purpose model'''
    
    __tablename__='test'

    #telegram user id
    id = Column(Integer, primary_key=True)
    player_title = Column(String, default='turtle egg')
    mony = Column(Integer, default=0)
    lvl = Column(Integer, default=0)
    atk = Column(Integer, default=10)
    defense = Column(Integer, default=20)
```

Now we need to know how to make data and models queries from  our database.

```python
from easy_tbot.core.client.handlers import MessageHandler
from easy_tbot.contrib.db.alchemy import session_scope
from aiogram.types import Message
from ..models import UserGameProfile

class Profile(MessageHandler):
    async def handle(self, msg:Message):
        
        with session_scope() as session:
            profile = session.query(UserGameProfile).get(msg.from_user.id)
            if profile is None:
                profile = UserGameProfile(id=msg.from_user.id) 
            
            async msg.reply('done')
    
    class Meta:
        commands=['create_profile']
```

This example shows the creation of a profile of a game like chatwars.