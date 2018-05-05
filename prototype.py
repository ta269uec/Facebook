from pprint import pprint
from sys import exit

# simply trying out various ways to access to access facebook API

def read_access_token_from_file(local_file_name):
    with open(local_file_name, "r") as fid:
        return fid.readline()

def example_using_facebook_package(ACCESS_TOKEN, VERSION):
    # http://facebook-sdk.readthedocs.io/en/latest/api.html
    # https://github.com/mobolic/facebook-sdk/blob/master/docs/api.rst
    import facebook
    graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, version=VERSION)
    posts = graph.get_connections(id='me', connection_name='posts', fields='created_time,from')
    pprint(posts)
    return

def example_using_facepy_package(ACCESS_TOKEN, VERSION):
    # https://github.com/jgorset/facepy
    from facepy import GraphAPI
    graph = GraphAPI(ACCESS_TOKEN)
    posts = graph.get('me/posts')
    pprint(posts)
    return

if __name__ == '__main__':
    TOKEN_FILE_NAME = "C:\\Users\\TarunJoshi\\FB_ACCESS_TOKENS\\token1.txt"
    ACCESS_TOKEN = read_access_token_from_file(TOKEN_FILE_NAME)
    VERSION = '2.7'
    
#    example_using_facebook_package(ACCESS_TOKEN, VERSION)
    example_using_facepy_package(ACCESS_TOKEN, VERSION)