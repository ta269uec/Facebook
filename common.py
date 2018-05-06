# this module will host a bunch of helper functions while we figure what all we can fo with the graph api.
# once we figure that out, we will re-organize this module

def read_access_token_from_file(local_file_name):
    with open(local_file_name, "r") as fid:
        return fid.readline()
    
def convert_time_zone(from_date_time, from_zone='UTC', to_zone='America/New_York'):
    from datetime import datetime
    from dateutil import tz
    from_zone, to_zone = tz.gettz(from_zone), tz.gettz(to_zone)
    # Tell the datetime object that it's in from_zone time zone since datetime objects are 'naive' by default    
    from_date_time = from_date_time.replace(tzinfo=from_zone)
    return from_date_time.astimezone(to_zone)    