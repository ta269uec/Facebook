# this module will host a bunch of helper functions while we figure what all we can fo with the graph api.
# once we figure that out, we will re-organize this module

def read_access_token_from_file(local_file_name):
    with open(local_file_name, "r") as fid:
        return fid.readline()