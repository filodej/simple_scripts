def add_getters( obj, pattern = 'get_%s' ):
    """
        >>> class A:
        ... 	def __init__( self ): self.a = None; self.b = []
        ... 	def x( self ): print 'x'
        ... 	
        >>> a = A()
        >>> print dir( a )
        ['__doc__', '__init__', '__module__', 'a', 'b', 'x']
        >>> add_getters( a )
        >>> print dir(a)
        ['__doc__', '__init__', '__module__', 'a', 'b', 'get_a', 'get_b', 'x']
        >>> add_getters( a )
        >>> print dir(a)
        ['__doc__', '__init__', '__module__', 'a', 'b', 'get_a', 'get_b', 'x']
        >>> a.get_a()
        >>> a.get_b()
        []
    """
    def getter_creator( name ):
        def getter( self_ ):
            return getattr( self_, name )
        return getter
        
    import new
    d = obj.__dict__
    getters = [ ( pattern % name, new.instancemethod( getter_creator( name ), obj, obj.__class__ ) )
                    for name, value in d.items() if not callable( value ) ]
    d.update( dict( getters ) )

def add_setters( obj, pattern = 'set_%s' ):
    """
        >>> class A:
        ... 	def __init__( self ): self.a = None; self.b = []
        ... 	def x( self ): print 'x'
        ... 	
        >>> a = A()
        >>> print dir( a )
        ['__doc__', '__init__', '__module__', 'a', 'b', 'x']
        >>> add_setters( a )
        >>> print dir(a)
        ['__doc__', '__init__', '__module__', 'a', 'b', 'set_a', 'set_b', 'x']
        >>> add_setters( a )
        >>> print dir(a)
        ['__doc__', '__init__', '__module__', 'a', 'b', 'set_a', 'set_b', 'x']
        >>> a.set_a( 1 )
        >>> a.a
        1
        >>> a.set_b( [1,2] )
        >>> a.b
        [1, 2]
    """
    def setter_creator( name ):
        def setter( self_, val ):
            return setattr( self_, name, val )
        return setter
    
    import new
    d = obj.__dict__
    setters = [ ( pattern % name, new.instancemethod( setter_creator( name ), obj, obj.__class__ ) )
                    for name, value in d.items() if not callable( value ) ]
    d.update( dict( setters ) )

def add_getters_setters( obj ):
    """
        >>> class A:
        ... 	def __init__( self ): self.a = None; self.b = []
        ... 	def x( self ): print 'x'
        ... 	
        >>> a = A()
        >>> print dir( a )
        ['__doc__', '__init__', '__module__', 'a', 'b', 'x']
        >>> add_getters_setters( a )
        >>> print dir(a)
        ['__doc__', '__init__', '__module__', 'a', 'b', 'get_a', 'get_b', 'set_a', 'set_b', 'x']
        >>> add_getters_setters( a )
        >>> print dir(a)
        ['__doc__', '__init__', '__module__', 'a', 'b', 'get_a', 'get_b', 'set_a', 'set_b', 'x']
        >>> a.get_a()
        >>> a.set_a( 1 )
        >>> a.get_a()
        1
        >>> a.get_b()
        []
        >>> a.set_b( [1,2] )
        >>> a.get_b()
        [1, 2]
    """
    add_getters( obj )
    add_setters( obj )

def _test():
    import doctest
    doctest.testmod()
 
if __name__ == "__main__":
    _test()
