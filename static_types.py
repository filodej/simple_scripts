
def returns( expected_types ):
    if not isinstance( expected_types, tuple ):
        expected_types = ( expected_types, )
    def checker( fn ):
        def check_ret( *args, **kwargs ):
            value = fn( *args, **kwargs )
            if type( value ) not in expected_types:
                raise TypeError( "Call of '%s': wrong return type (value '%s' is of %s, expected %s)" \
                                 % ( fn.func_name, value, type( value ), expected_types ) )
            return value
        # propagate function object attributes
        check_ret.func_name = fn.func_name
        check_ret.func_doc = fn.func_doc
        check_ret.func_dict = fn.func_dict
        #check_args.func_code = fn.func_code
        return check_ret
    return checker

def accepts( *targs, **tkwargs ):
    def checker( fn ):
        # build type map
        type_map = dict( zip( fn.func_code.co_varnames, targs ) )
        type_map.update( tkwargs )
        for k, v in type_map.iteritems():
            if not isinstance( k, tuple ):
                type_map[k] = ( v, )
        def check_args( *args, **kwargs ):
            # build arg map
            arg_map = dict( zip( fn.func_code.co_varnames, args ) )
            arg_map.update( kwargs )
            #print arg_map
            # check whether all explicit types fit
            for ( name, expected_types ) in type_map.items():
                value = arg_map[name]
                if type( value ) not in expected_types:
                    raise TypeError( "Call of '%s': wrong type of parameter '%s' (value '%s' is of %s, expected %s)" \
                                     % ( fn.func_name, name, value, type( value ), expected_types ) )
            return fn( *args, **kwargs )
        # propagate function object attributes
        check_args.func_name = fn.func_name
        check_args.func_doc = fn.func_doc
        check_args.func_dict = fn.func_dict
        #check_args.func_code = fn.func_code
        return check_args
    return checker

@accepts( float, float, float )
@returns( float )
def three_floats( a, b, c ):
    """
        >>> three_floats( 3.3, 2.0, 1.0 )
        6.2999999999999998

        >>> three_floats( 3.3, 2.0, 1 )
        Traceback (most recent call last):
        ...
        TypeError: Call of 'three_floats': wrong type of parameter 'value' (value '1' is of <type 'int'>, expected (<type 'float'>,))
        """
    return a + b + c

@returns( int )
def increment( val ):
    """
        >>> increment( 1 )
        2

        >>> increment( 1.0 )
        Traceback (most recent call last):
        ...
        TypeError: Call of 'increment': wrong return type (value '2.0' is of <type 'float'>, expected (<type 'int'>,))
    """
    return val + 1

@accepts( name=str, age=int )
def named_args( name, age, data ):
    """
        >>> named_args( 'John', 32, {} )
        John (32): {}

        >>> named_args( 'Jack', 16, 'personal data' )
        Jack (16): personal data

        >>> named_args( 'Sally', 87.5, [] )
        Traceback (most recent call last):
        ...
        TypeError: Call of 'named_args': wrong type of parameter 'age' (value '87.5' is of <type 'float'>, expected (<type 'int'>,))

        >>> named_args( 'Monica', data=( 'secret', 'code' ), age='53' )
        Traceback (most recent call last):
        ...
        TypeError: Call of 'named_args': wrong type of parameter 'age' (value '53' is of <type 'str'>, expected (<type 'int'>,))
    """
    print '%s (%d):' % ( name, age ), data


def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()

#named_args( 'Jack', age=16, data='personal data' )        
#three_floats( 3.3, 2.0, 1.0 )
#named_args( 'John', 32, {} )
#named_args( 'Jack', 16, 'personal data' )
#named_args( 'Sally', 87.5, [] )

#increment( 1 )
#increment( 1.0 )
#three_floats( 3.3, 2.0, 'a' )
#return_float()
