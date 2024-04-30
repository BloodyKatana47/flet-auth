NO_ENV = 'Please, create .env file inside project.\nYou can use .env_example as an example.'
UNKNOWN = 'Unknown error'
EMPTY_DATABASE_NAME = 'Database name can not be empty'


def error_handler(func):
    """
    Main decorator for error handling.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError as type_exc:
            type_exc = str(type_exc)
            if type_exc == r"object of type 'NoneType' has no len()":
                print(f'Error in function: {func.__name__}\n\n{NO_ENV}')
            else:
                print(f'Error in function: {func.__name__}\n\n{UNKNOWN}')
            exit()
        except ValueError as value_exc:
            value_exc = str(value_exc)
            if value_exc == r"DATABASE_NAME can not be empty":
                print(f'Error in function: {func.__name__}\n\n{EMPTY_DATABASE_NAME}')
            else:
                print(f'Error in function: {func.__name__}\n\n{EMPTY_DATABASE_NAME}')
            exit()

    return wrapper
