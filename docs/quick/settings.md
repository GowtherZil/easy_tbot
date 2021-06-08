# Settings

>Settings are in settings.py file. This file has 4 basic variables and each one has the configuration of one aspect of the bot.

## Overview

A configuration file looks like this

```python hl_lines="5 12 19 27 32"
from pathlib import Path

BASE_DIR = Path(__file__).parent

CLIENT = {
    'backend':'easy_tbot.contrib.client.aiogram.AiogramBackend',
    'config':{
        'token':'' # this must be setup
    }
}

DB = {
    'backend':'easy_tbot.contrib.db.alchemy.SqlAlchemyBackend',
    'config':{
        'url':'sqlite:///./sqlite.db'
    }
}

TEMPLATE_ENGINE = {
    'backend':'easy_tbot.contrib.template.jinja.JinjaBackend',
    'config':{
        'templates':[BASE_DIR/'templates'],
        'allowed_extensions':['html', 'md', 'txt']
    }
}

CLI = {
    'backend':'easy_tbot.contrib.cli.fire.FireBackend',
    'config':{}
}

SHARDS = [
    'easy_tbot.extra.cli', # a shard with some useful commads 
    'easy_tbot.contrib.db.alchemy.cli', # an alchemy shard with some useful commands
    ]
```

## Generic explanation about variables

Each variable contains a dictionary with two entries, the backend and the configuration called *config*.

```python hl_lines="2 3" 
VARNAME = {
    'backend':'' # Here is written the address of the backend
    'config':{} # Here are the arguments it receives in the form  *'name': value*
}
```

## Variables

This table contains the variables and what they configure

| Variable           | Description                                     |
| :----------        | :-----------------------------------            |
| CLIENT             | Contains client configuration                   |
| DB                 | Contains database configuration                 |
| TEMPLATE_ENGINE    | Contains template engine configuration          |
| CLI                | Contains *command line interface* configuration |

!!! warning
    When you create a project for the first time, the first thing you should put is the token in the client configuration if it is not passed by command before.

