# Templates

> Now we can use  templates for rendering complex data inside messages, that is cool.

## Setup

Configure rendering inside TEMPLATE_ENGINE variable in settings.py.

```python
TEMPLATE_ENGINE = {
    'backend':'easy_tbot.contrib.template.jinja.JinjaBackend',
    'config':{
        'templates':[BASE_DIR/'templates'],
        'allowed_extensions':['html', 'md', 'txt']
    }
}
```
!!! note 'JinjaBackend configuration'
    `templates` key holds directories to look for templates and `allowed_extension` key is a filter for extension files. In this case only *html*, *md*, and *txt* extensions are recogniced as templates inside templates folder.

## How to use this template engine?

```python
from easy_tbot.core.client.decorators import message_handler
from aiogram.types import Message
from easy_tbot.core.template import render
# write your handlers in here

@message_handler(commands=['start'])
async def start(msg:Message, **kwargs):
    '''A sample purpose handler'''
    await msg.reply(render('welcome.txt', username=msg.from_user.username))
```

Asuming that welcome.txt is a proper jinja template:

```jinja
Welcome {{username}}.
```

At /start command, our bot will print.:

```text
Welcome Jhon Doe.
```
> Assuming John Doe is your username
