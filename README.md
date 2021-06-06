# Easy Tbot

Mini framework for database and other useful stuff integration with Telegram bot api

## Motivation

The biggest motivation was when I wanted to make my first bot on Telegram using python. I had many modules like telethon or pyTelegramBotApi but it did not solve the idea of how to structure the project, how to make it join a database and other integrations. The most important thing if I wanted to do another project, would I have to repeat all the code? Thus was born easy_tbot. Another motivation that came as a divine sign was to try to copy (test purpose) a friend's bot, a .py of more than 3000 lines of code -_-

## Documentation

TODO: test purpose

## What are we?

- A framework.
- A component-oriented system.
- The VERY higher layer of what is desired in most telegram bots.
- An idea.

## What are we not?

- A telegram api wrapper.

## Release Notes

In some versions of the project all backwards compatibility has been destroyed but to prevent future disasters we are going to follow some rules when it comes to versioning the API.

We will use versions with form 'x.y.z'. The changes in the smaller versions (z) will be related to the private part of the api and will not spoil the backwards compatibility. The changes in the medium versions (y) will be related to new features that hopefully we can do on top of the previous API without spoiling the compatibility and otherwise we will notify in the documentation as it should. The big versions (x) are related to big changes in the public API that can go from huge refactorings to architecture changes or some milestones fulfill in the project life time.

### Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.4b2 | :x:                |
| 1.0.5   | :x:                |
| 1.0.7   | :x:                |


## Future plans
Right now the framework is very useful but we are going to make it flatter in the future. We want shards to be more and more reusable even between different backends of the same framework.

## Thanks

My thanks to [GowterZil](https://github.com/GowtherZil) a newborn of zen.
