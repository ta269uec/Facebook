from sys import exit
from pprint import pprint
from collections import defaultdict

from facepy import GraphAPI
from facepy.utils import get_extended_access_token

from common import read_access_token_from_file

class MyPosts(object):
    # The required post fields, post edges, and options are defined here. 
    # The user can pass additional fields, edges, and options which will be appended to the required fields, edges, and options.
    required_post_fields = set(['created_time', 'from', 'caption', 'timeline_visibility', 'privacy', 'message', 'place', 'story', 'with_tags'])
    required_post_edges = {
                            'reactions':set(['type','profile_type','username','name']),
                            'comments':set(['from','message','like_count','comment_count', 'created_time']),
                            'attachments':set(['type','title','description'])     
                        }
    required_options = {'include_hidden':True}
    def __init__(self, graph_api, fields=None, post_edges=None, options=None):
        self.me_id = self.__get_me_id(graph_api)
        if self.me_id is None:
            raise Exception('Failed to get user id and cannot proceed.') 
        fields = MyPosts.required_post_fields if fields is None else fields.union(required_post_fields)
        if post_edges is None:
            post_edges = MyPosts.required_post_edges
        else:
            temp = {k:v for k,v in MyPosts.required_post_edges.items()}
            for k in post_edges:
                if k in temp:
                    temp[k] = temp[k].union(post_edges[k])
                else:
                    temp[k] = post_edges[k]
            post_edges = temp
        options = MyPosts.required_options if options is None else required_options
        self.posts = graph_api.get(self.__build_query_string(fields, post_edges, options))['data']
        post_id_view, reaction_view = self.__build_post_views(self.posts)
        return
    
    def __get_me_id(self, graph_api):
        """
            Code to get your own id so that you can filter on posts that were created by just you and not posted on your timeline.
        """
        try:
            return graph_api.get('me?fields=id')['id']
        except:
            return None
    
    def __build_query_string(self, fields, post_edges, options):
        query_params_str = ','.join(fields) if fields else ""
        edges_str = ','.join(["%s{%s}"%(k, ','.join(v)) for k,v in post_edges.items()]) if post_edges else ""
        options_str = ','.join(["%s=%s"%(k,str(v)) for k,v in options.items()]) if options else ""
        query_string = ''.join(['me/posts', '?fields=', query_params_str, ',', edges_str, '&', options_str])
        return query_string
    
    def __build_post_views(self, posts):
        post_id_view = {} # Key is post_id and value is the post
        reaction_id_view = {} # Key is reaction id and value is post id
        reaction_type_view = defaultdict(list) # Key is reaction_type and value consists of a list of post ids.
        # Key is friend's name and value is a dictionary which has key as reaction type and value as list of post-ids where they have reacted.
        friend_reaction_view = defaultdict(dict) 
        
        for post in posts:
            if 'from' in posts and posts['from']['id'] ==  self.me_id:
                post_id_view[post['id']] = post
                if "reactions" in post:
                    for reaction in post["reactions"]["data"]:
                        reaction_id_view[reaction['id']] = post['id']
                        if 'type' in reaction:
                            reaction_type_view[reaction['type']].append(post['id'])
                            if 'name' in reaction and 'profile_type' in reaction and  reaction['profile_type'] == 'user':
                                friend_reaction_view[reaction['name']][reaction['type']].append(post['id'])
        return post_id_view, reaction_id_view
    

#  'created_time': '2018-04-05T01:45:54+0000',

if __name__ == '__main__':
    # Paste your app token in a local file on your machine and add its path here.
    # Note this token is a user token and is temporary. This will expire in 2-3 hours and you need to regenrate it.
    # TODO: Research how I can get a long term access token.
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
#     my_posts = MyPosts(graph_api, post_fields, post_edges, options)
    my_posts = MyPosts(graph_api)    
    pprint(my_posts.posts)