
def ret_type( expected_type ):
    def checker( fn ):
        def check_ret( *params ):
            value = fn( *params )
            if not isinstance( value, expected_type ):
                raise TypeError( "Call of '%s': wrong return type (value '%s' is of %s, expected %s)" \
                                 % ( fn.func_name, value, type( value ), expected_type ) )
            return value
        return check_ret
    return checker

def arg_types( *types ):
    def checker( fn ):
        def check_args( *params ):
            if len( params ) != len( types ):
                raise TypeError( "Call of '%s': wrong number of parameters (%d), expected %d" \
                                 % ( fn.func_name, len( params ), len( types ) ) )
            for ( expected_type, value, name ) in zip( types, params, fn.func_code.co_varnames ):
                if not isinstance( value, expected_type ):
                    raise TypeError( "Call of '%s': wrong type of parameter '%s' (value '%s' is of %s, expected %s)" \
                                     % ( fn.func_name, name, value, type( value ), expected_type ) )
            return fn( *params )
        return check_args
    return checker

@arg_types( float, float, float )
#@ret_type( float )
def three_floats( a, b, c ):
    return a + b + c

@ret_type( int )
def increment( val ):
    return val + 1

#three_floats( 3.3, 2.0, 1.0 )
#increment( 1 )
#increment( 1.0 )
three_floats( 3.3, 2.0, 'a' )
#return_float()
