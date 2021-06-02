"""The jinja backend main module"""

# We load jinja **FileSystemLoader, Environment and select_autoescape** for initialization and setup
from jinja2 import FileSystemLoader, Environment, select_autoescape
# and our [template engine backend](ref:easy_tbot.core.tenplate.backend:Backend)
from easy_tbot.core.template.backend import Backend

# ## The JinjaBackend (a django like template engine)
# Used just for jinja configuration and initialization
class JinjaBackend(Backend):
    def __init__(self, templates:list, allowed_extensions:list):
        """Jinjabackend initialization

        Parameters
        ----------
        templates : List[str]
            a list of directories to search for templates files
        allowed_extensions : List[str]
            a list of extensions like 'md, html, tpl' for filter the templates
            founded in templates directories
        """        
        autoescape = select_autoescape(allowed_extensions)
        self.__env = Environment(loader=FileSystemLoader(searchpath=templates), autoescape=autoescape)
    
    def render(self, template,*args, **kwargs):
        """A funtion to process a template witha context

        Parameters
        ----------
        template : str
            relative path to template based on configurations

        Returns
        -------
        str
            The result string of processing the template
        """             
        return self.__env.get_template(template).render(*args, **kwargs)