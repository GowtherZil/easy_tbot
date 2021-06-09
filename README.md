# Easy Tbot

Mini framework for database and other useful stuff integration with Telegram bot api

## Motivation

The biggest motivation was when I wanted to make my first bot on Telegram using python. I had many modules like telethon or pyTelegramBotApi but it did not solve the idea of how to structure the project, how to make it join a database and other integrations. The most important thing if I wanted to do another project, would I have to repeat all the code? Thus was born easy_tbot. Another motivation that came as a divine sign was to try to copy (test purpose) a friend's bot, a .py of more than 3000 lines of code -_-

## Telegram user and IT point of view

For a few years, telegram has gained popularity and lately more, mainly due to the different
privacy policies between it and its competitors, but mainly because it is one of the few messaging
services that so completely exposes a public API that allows , among other things, the construction of Bots.
Today due to social isolation and measures of the same nature adopted as a result of the recent situation with
sars-cov2, many services and entities make use of the facilities provided by Telegram in this regard.
To accomplish this are several libraries that work as clients of these APIs allowing us to create these bots in our preferred languages.
These libraries collect the basic functionality to build a bot but do not solve problems that are normally included in this process.
Which leads us to ask ourselves.

## What do we want when we make a bot?

There are several things that are wanted when making a bot in telegram and in most three things are required:

*   Process information
*   Store information
*   Show information

Current libraries allow us to process and display information but in the lower layer of what is
expected from a bot in Telegram, making the process of creating serious functionalities more
complex than just processing simple commands and eventually forcing us to depend on other libraries
that they are not part of the Telegram packaging. Hence the idea of ​​making a framework that allows us
to make telegram bots with some comfort without rewriting code, using well-equipped libraries for this purpose.


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

### Old version compatibility

| Version | Supported          |
| ------- | ------------------ |
| 1.0.4b2 | No                 |
| 1.0.5   | No                 |
| 1.0.7   | No                 |


## Future plans
Right now the framework is very useful but we are going to make it flatter in the future. We want shards to be more and more reusable even between different backends of the same framework.

## Thanks

My thanks to [GowterZil](https://github.com/GowtherZil) a newborn of zen.
