""""
We use a folder module instead a .py becouse some other commands related to
sqlalchemy family can be added in a future and is better for extensibility write
the module in this way
"""

# ## Importing inner commands for recognicion
from .migrate import migrate
