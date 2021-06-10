from pathlib import Path

BASE_DIR = Path(__file__).parent

CLIENT = {
    'backend':'easy_tbot.contrib.client.aiogram.AiogramBackend',
    'config':{
        'token':'{token}'
    }
}

DB = {
    'backend':'easy_tbot.contrib.db.alchemy.SqlAlchemyBackend',
    'config':{
        'url':'sqlite:///./sqlite.db'
    }
}

TEMPLATES = {
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