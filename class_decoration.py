def add_getters( obj ):
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
        None
        >>> a.get_b()
        []
    """
    import new
    d = obj.__dict__
    getters = [ ( 'get_'+name, new.instancemethod( lambda _self: getattr( _self, name ), obj, obj.__class__ ) )
                    for name, value in d.items() if not callable( value ) ]
    d.update( dict( getters ) )

def add_setters( obj ):
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
    import new
    d = obj.__dict__
    setters = [ ( 'set_'+name, new.instancemethod( lambda _self, val: setattr( _self, name, val ), obj, obj.__class__ ) )
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
        >>> a.get_a
        <bound method A.<lambda> of <__main__.A instance at ...
        >>> a.get_a()
        None
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
