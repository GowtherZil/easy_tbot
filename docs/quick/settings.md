# Settings

This file has 4 basic variables and each one has the configuration of one aspect of the bot.

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