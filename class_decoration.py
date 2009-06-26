class A:
    def __init__( self ):
        self.a = None
        self.b = []
        
    def x( self ):
        print 'x'

def add_setters( obj ):
    import new
    cls = obj.__class__
    d = obj.__dict__
    d.update( dict( ( 'set_'+name, new.instancemethod( lambda obj, val: setattr( obj, name, val ), obj, cls) )
                    for name, value in d.items() if not callable( value ) ) )

def add_getters( obj ):
    import new
    cls = obj.__class__
    d = obj.__dict__
    d.update( dict( ( 'get_'+name, new.instancemethod( lambda obj: getattr( obj, name ), obj, cls ) )
                    for name, value in d.items() if not callable( value ) ) )

def add_getters_setters( obj ):
    add_getters( obj )
    add_setters( obj )

a = A()
print dir( a )
add_setters( a )
print dir( a )
print a.set_a
a.set_a( 'a' )
a.set_b( [1,2] )
add_getters( a )
print dir( a )
a.get_a()
a.get_b()

