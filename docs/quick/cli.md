# CLI

> A way of adding new and utils shell commands to your app.

## Where define shells commands?

Inside any shard in a file called commands.py

## How define shells commads?

Shell commands are defined by a class and some inner methods. Its more easy to explain with a example.

```python
from easy_tbot.shell.custom import ShellCommand

class HelloWorldCommand(ShellCommand):
    '''A sample purpose shell'''

    name='hello_world'
    extra={'help':'A sample purpose command'}

    def do(self, *args, **kwargs):
        print('Hello World!!')
    
    def post_insert(self, argument_parser):
        pass
```

A fancy command that print hello world in the screen. The name attribute define the literal to call the command, and extra attributes the other argument that you can pass to an Argumentparser. With this new command if you run `python bormanager.py -h` it will print `hello_world` info and other loaded commands. If you type `python botmanager.py hello_world -h` it will print `A sample purpose command`. If you used it as `python botmanager.py hello_world` it will print `Hello World!!`.

 And for exceptic ones, post_insert function help us to add some complexity to our commands, its recieve an ArgumentParser and you can add some parameters or subparsers in this sections, basic commands don't need to declare this function.
