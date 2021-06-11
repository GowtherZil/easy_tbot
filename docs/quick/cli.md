# CLI

> A way of adding new and utils shell commands to your app.

## Where do we define shells commands?

Inside any shard in a file called commands.py

## How to define shell commands?

Shell commands are defined with a decorator and a function. It's easier to explain with a example.

```python
from easy_tbot.core.cli.decorator import command

# create your commands here

@command
def hello_world():
    '''`A sample purpose command'''
    print(f'Hello World!!')

```

A fancy command that prints hello world in the screen. With this new command if you run `python bormanager.py -h` it will print `hello_world` info and other loaded commands. If you type `python botmanager.py hello_world -h` it will print `A sample purpose command`. If you used it as `python botmanager.py hello_world` it will print `Hello World!!`.

!!! note
    The current backend class that the **CLI** raises is *fire* and we do not think that we'll be implementing another for a while since it solves almost all the problems related to the **CLI** .
