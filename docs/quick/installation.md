# Installation

```bash
python -m pip install easy_tbot[<parameter>]
```

## The allowed parameters and what they do are in the following table

| Parameter | Effect                                  |
| --------- | --------------------------------------- |
| jinja     | Install dependencies for jinja templates|
| aiogram   | Install dependencies for aiogram client |
| fire      | Install dependencies for fire           |
| sql       | install dependencies for sqlalchemy     |
| extras    | install  all  dependencies              |

If you are a novice, I suggest you use the *extras* parameter, remaining like this

```bash
python -m pip install easy_tbot[extras]
```