# Handlers

> Handlers define what shall our bot do when some related event is trigered on Telegram.

## The handlers types are

- Message handler
- Inline handler
- Chosen inline handler
- Callback query handler
- Shipping query handler
- Pre checkout query handler
- Poll handler
- Poll answer handler

!!! note
    For further information refer to the official telegram bot api.

## Where to define a handler?

Handlers are defined in a handler module that can be a handler.py or  a handler folder as a python module that imports inner handler in his \_\_init\_\_.py.

## How to define a handler?

We have two ways to define a handler, one is a class-based handler and the other is a function-based handler.

### Function based handlers

We decided to start with the most known python system for handling incoming info from Telegram Bot Api. The function views are decorators over normal functions. The parameters for the decorator and function views depends of what kind of bot backend your project use.
By default we provide an Aiogram base backend, this means that when we use a decorator, this decorator receives whatever aiogram's decorator with the same purpose will receive. For example:

Aiogram's code for command decorator.

```python linenums="1"
from aiogram import Bot
from aiogram.dispatcher import Dispatcher

bot = Bot(token='your-token')
d= Dispatcher(bot)
@d.mesage_handler(commands=['start'])
async def start(msg, **kwargs):
    await msg.reply('Hello world')
```

easy-tbot's code for command decorator:

```python linenums="1"
from easy_tbot.core.client.decorators import message_handler
from aiogram.types import Message

@message_handler(commands=['start'])
async def hello_world(msg:Message, **kwargs):
    await msg.reply('hello world!!!')
```

If you want to know how to use our handlers just study how to use Aiogram's handlers.

### Class-based handlers

Just like function handlers, class-based handlers are simple and usefull things. The previous command handler defined in a class-base handler will be:

```python
from easy_tbot.core.client.handlers import MessageHandler
from aiogram.types import Message
# write your handlers here

class HelloWorld(MessageHandler):

    async def handle(self, msg:Message, **kwargs):
        msg.reply('Hello world!')

    class Meta:
        commands=['start']        
```

In a class-based handler, inner Meta class holds the same arguments as kwargs in a function base views. The args arguments are defined as Meta inner variables called 'args'. The handle method is the function that defines the handler functionability.

```python
.
.
.
class Meta:
    args=(arg1, arg2,...)

```

Remember our handlers are wraped around well defined functions used as Telegram Api wrappers. This functions are stored into others libraries as Aiogram.

Function-base handlers can be imported

```python
from easy_tbot.core.client.decorators import *
```

Class-base handlers can be imported

```python
from easy_tbot.core.client.handlers import *
```

!!! note
    If you are using the Aiogram Backend refer to [Aiogram documentation](http://test.com) for types and parameters in class and function base view.

