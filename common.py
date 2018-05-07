# this module will host a bunch of helper functions while we figure what all we can fo with the graph api.
# once we figure that out, we will re-organize this module
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np

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

def plot_bar_chart(objects, values, y_label, title, x_label_rotation=70, x_label_fontsize=8):
    y_pos = np.arange(len(objects))
    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, objects, rotation=x_label_rotation, fontsize=x_label_fontsize)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid()
    plt.show()    
    return

def plot_pie_chart(values, labels, title, explode=None, show_legend=True, hide_labels_in_chart=False, smart_legends = False):
    explode = explode if explode else [0.0 for _ in labels]
    if hide_labels_in_chart:
        plt.pie(values, explode=explode, startangle=90)
    else:
        plt.pie(values, labels=labels, explode=explode, startangle=90)        
    if show_legend:
        if smart_legends:
            total_sum = sum(values)
            smart_legend_labels = []
            for value, label in zip(values, labels):
                percentage = ''.join([str(round(value*100/total_sum, 2)), '%'])
                smart_label = "%s: (%s, %s)."%(label, str(percentage), value)
                smart_legend_labels.append(smart_label)
            plt.legend(labels=smart_legend_labels)
        else:
            plt.legend(labels=labels)            
    plt.title(title)
    plt.show()    
    return