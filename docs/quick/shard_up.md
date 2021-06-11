# Shard up

>A shard is an abstraction, it is the way to encapsulate a fragment of bot logic and thus make it reusable

## Creating a shard

Once our project is created we can open a terminal in its folder and type.

```bash
python botmanager.py createshard <name>
```
This command will add a shard with the name given to the project, a shard is just a python module with the following files inside.

* \_\_init\_\_.py
* handlers.py
* models.py
* commands.py

## Setup the shard

The next thing would be to enable the shard, for doing this just add it in the SHARDS list in the settings

```python hl_lines="4"
SHARDS = [
    'easy_tbot.extra.cli', # a shard with some useful commads 
    'easy_tbot.contrib.db.alchemy.cli', # an alchemy shard with some useful commands
    'your shard name here' # <- 
    ]
```

!!! note
    You can add as many shards as necessary, the only restriction is that they cannot share names.
