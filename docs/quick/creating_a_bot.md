# Management

## Creating a bot

Build a bot using the next command:

```batch
create-tbot <name> [options]
```
We have a only option, the token option that can be used with *-t* parameter
or with *--token* parameter follow by your bot token given by @BotFather in Telegram.

### Command example  with token

```batch
create-tbot testing -t a_massive_hash_token
```

!!! warning
    The token is embedded in the code so be careful when publishing or deploying the bot

The command creates a folder with the given name in the current location. This folder has inside the necessary files to start programming our bot.