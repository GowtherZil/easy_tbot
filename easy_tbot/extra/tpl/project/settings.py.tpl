from easy_tbot.contrib.bot.aiogram import AiogramBackend
from easy_tbot.contrib.db.alchemy import SqlAlchemyBackend
from easy_tbot.contrib.template.jinja import JinjaBackend
from easy_tbot.contrib.cli.fire import FireBackend
from pathlib import Path

BASE_DIR = Path(__file__).parent

BOT=AiogramBackend(token='{token}')

DB = SqlAlchemyBackend(url='sqlite:///./sqlite.db')

TEMPLATE_ENGINE = JinjaBackend(templates=[BASE_DIR/'templates'],\
    allowed_extensions=['html', 'md', 'txt'])

CLI = FireBackend()

SHARDS=[
    'easy_tbot.extra.cli', # a core shard with some useful commads 
    'easy_tbot.contrib.db.alchemy.cli', # the alchemy shard for commands
    ]