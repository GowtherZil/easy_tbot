"""
This module requires a bit of explanation: The purpose is create a class that can make a dummy
metaclass for one level of class instantiation that replaces itself with
the actual metaclass. Allowing us to do a multiple class and metaclass inheritance and yes, this
sound like black magic.
"""
# We import a basic **types** modules for further black magic
import types
# and the **sys** module for check some python version before do our bizarre spell \(-_- )
import sys

# ## The factory class
# We already talked about it in the intro of the module, 
# a class that allows you to create mixed metaclasses

class MultiMetaFactory:
    '''
    Factory class that create dummy metaclasses joining multiples metclasses and normal classes.
    '''
    
    def __getitem__(self, base_classes):
        """
        Create a base class with a set of many bases classes, 
        simultaneous metaclass are allowed.

        Parameters
        ----------
        base_classes : *tuple
            A tuple of classes that can be metclasses or object base classes

        Returns
        -------
        metaclass
            dummy metaclasses joining multiples classes
        """
       
        # We declare a variable for store meta classes
        metas = []

        # and another to store normal base classes
        bases = []
        
        # and now we split them 
        for _class in base_classes:
            if issubclass(_class, type):
                metas.append(_class)
            else:
                bases.append(_class)

        # turn the bases list into a tuple
        bases = tuple(bases)

        # and create a base class that inherits from all meta classes filtered
        class meta_mix(*metas):
            pass
        
        # At this point we are ready to cast the spell
        class metaclass(type):
            """
            This is our dummy class
            """

            def __new__(cls, name, this_bases, d):                
                if sys.version_info[:2] >= (3, 7): # whe check for python version

                    # This version introduced PEP 560 that requires a bit
                    # of extra care (we mimic what is done by __build_class__).
                    
                    resolved_bases = types.resolve_bases(bases) # some __build_class__ mimic already promised
                    if resolved_bases is not bases:
                        d['__orig_bases__'] = bases # update base class dictionary
                else:
                    resolved_bases = bases  # just update base class dictionary if python version less than 3.7
                return meta_mix(name, resolved_bases, d) # return the metaclass mixing with updated class bases

            @classmethod
            def __prepare__(cls, name, this_bases): # overload this to prepare metaclass as is espected
                return meta_mix.__prepare__(name, bases)

        return type.__new__(metaclass, 'temporary_class', (), {}) # return the dummy class that is now a super charged dummy class

# Now we create a instance of this  MuliMetaFactory for easing developers life.
MultiMeta = MultiMetaFactory()
# Now we can do something like 

# ```python
#    class SingletonAndABCClass(MultiMeta[ABCMeta, MetaSingleton, Object]): 
#        pass
# ```
