import requests
import inspect
from exceptions import (
    MissingRequiredArgument,
    InvalidResponseException,
    ResponseFailureException)
from helpers.trail import Trail


class Client:
    def __init__(self, api_key: str = None):
        if api_key is None:
            raise MissingRequiredArgument('Missing client api_key')

        self.__api_key = api_key
        self.url = 'https://www.hikingproject.com/data/'
        self.call_type = None
        self.params = {
            'key': self.__api_key,
            'maxResults': 10,
            'maxDistance': 10,
            'minLength': 0,
            'minStars': 0}

    def __send_request(self, call_type, custom_params):
        custom_params.update(self.params)
        return requests.get(self.url + call_type, params=custom_params)

    def __get_response(self, custom_params: dict = None):
        call_type = inspect.stack()[1].function.replace('_', '-')
        response = self.__send_request(call_type, custom_params)
        if not response.ok:
            raise InvalidResponseException(
                f'Error calling {self.url + call_type}, '
                'response: {response.json()}')
        if response.json().get('success') != 1:
            raise ResponseFailureException(
                f'API call failed. Status Code: {response.status_code}, '
                'Data: {response.json()}')
        return response.json().get('trails')

    # Methods to help update things inside of the client. 
    def set_sort_type(self, new_value: str = None):
        """Set the sorting type for trails
        Args:
            new_value (str): How would you like to sort the data?
        """
        sort_values = ['quality', 'distance']
        if new_value is None or new_value.lower() not in sort_values:
            raise ValueError(
                f'Missing or invalid sort value. '
                f'Should be one of: {sort_values}')
        self.params['sort'] = new_value.lower()
    
    def set_max_results(self, new_value: str = None):
        """Set the maximum number of results to return from Hiking Project
        Args:
            new_value (int): How many trails to get back from Hiking Projects?
        """
        if new_value is None or int(new_value) <= 0:
            raise ValueError(
                f'Missing or invalid value. Must be a number > 0')
        self.params['maxResults'] = new_value

    # API Methods as defined by https://www.hikingproject.com/data
    def get_trails(self, lat: str = None, lon: str = None):
        """Returns a list of Trail objeects
        Args:
            lat (str): Lattitude to search for.
            lon (str): Longitude to search for.
        Returns:
            trails (list): List of Trail objects
        """
        custom_params = {'lat': lat, 'lon': lon}
        if None in (lat, lon):
            error_message = f'Lattitude and longitude are required ' \
                            'but received - lat: {lat}, lon: {lon}'
            raise MissingRequiredArgument(error_message)
        return [Trail(x) for x in self.__get_response(custom_params=custom_params)]

    def get_trail_by_id(self, id):
        """Returns a single Trail objeect
        Args:
            id (str): Hiking Project trail id.
        Returns:
            trail (Trail): Single Trail object
        """
        if not id:
            raise MissingRequiredArgument(f'Required field id is missing.')
        return self.get_trails_by_id(ids=id)[0]

    def get_trails_by_id(self, ids=None):
        """Returns a list of Trail objeects
        Args:
            ids (list, str): list or comma separated str of Hiking Project trail ids.
        Returns:
            trails (list): list of Trail objects
        """
        if ids is None:
            raise MissingRequiredArgument(f'Required field ids is missing.')
        if type(ids) == list:
            ids = ','.join(ids)
        custom_params = {'ids': ids}
        return [Trail(x) for x in self.__get_response(custom_params=custom_params)]
