
class MissingRequiredArgument(Exception):
    """Raised when missing a required argument"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class InvalidResponseException(Exception):
    """Raised when the the request response is not < 400"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class ResponseFailureException(Exception):
    """Raised when Hiking Project reports an unsuccessful API call"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
