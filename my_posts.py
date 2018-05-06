from sys import exit
from pprint import pprint

from facepy import GraphAPI

from common import read_access_token_from_file

class MyPosts(object):
    def __init__(self, graph_api, fields=None, post_edges=None, options=None):
        self.posts = graph_api.get(self.__build_query_string(fields, post_edges, options))['data']
        return
    
    def __build_query_string(self, fields, post_edges, options):
        query_params_str = ','.join(fields) if fields else ""
        edges_str = ','.join(["%s{%s}"%(k, ','.join(v)) for k,v in post_edges.items()]) if post_edges else ""
        options_str = ','.join(["%s=%s"%(k,str(v)) for k,v in options.items()]) if options else ""
        query_string = ''.join(['me/posts', '?fields=', query_params_str, ',', edges_str, '&', options_str])
        return query_string
    

if __name__ == '__main__':
    # paste your app token in a local file on your machine and add its path here
    TOKEN_FILE_NAME = "C:\\Users\\TarunJoshi\\FB_ACCESS_TOKENS\\token1.txt"
    ACCESS_TOKEN = read_access_token_from_file(TOKEN_FILE_NAME)
    graph_api = GraphAPI(ACCESS_TOKEN)
    
    post_fields = ['created_time', 'from', 'caption', 'timeline_visibility', 'privacy', 'message', 'place', 'story', 'with_tags']
    post_edges = {
                    'reactions':['type','profile_type','username','name'],
                    'comments':['from','message','like_count','comment_count', 'created_time'],
                    'attachments':['type','title','description']                                        
                 }
    options = {'include_hidden':True}
    my_posts = MyPosts(graph_api, post_fields, post_edges, options)
    pprint(my_posts.posts)