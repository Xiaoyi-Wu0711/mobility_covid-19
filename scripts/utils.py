import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from datetime import timedelta
import folium

plt.rcParams['figure.figsize'] = [10, 10]
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 10000)

pd.set_option('display.float_format', '{:.2f}'.format)


def process_data(raw_data):

    data = raw_data.dropna(subset=['sg_c__naics_code'])

    # preprocess data
    data['pop_up_col'] = 'name: ' + data.sg_c__location_name + '；' + 'type:' + data.sg_c__sub_category + '；' + 'stay time: ' + \
                        data['sg_wp__median_dwell'].astype(str) + '；' + 'visit number: ' + data[
                            'sg_wp__raw_visit_counts'].astype(str)
    data["date_range_start"] = pd.to_datetime(data["date_range_start"])
    data["sg_wp__median_dwell_hour"] = data["sg_wp__median_dwell"] / 60

    # aggravate the business type of data by naics code
    data['naics_2dig'] = data.sg_c__naics_code.astype(str).str[:2].astype(int)
    data['naics_3dig'] = data.sg_c__naics_code.astype(str).str[:3].astype(int)

    naics = pd.read_csv('../data/aggregated_naics.csv')

    data = pd.merge(data, naics, how='left', left_on='naics_2dig', right_on='code')

    # devide 'Accomodation' and 'Food' according to the first 3 digit
    data.loc[data['naics_3dig'] == 721, 'category'] = 'Accomodation'
    data.loc[data['naics_3dig'] == 722, 'category'] = 'Food'
    data=data.dropna(subset=["sg_wp__poi_cbg"])
    data['sg_wp__poi_cbg']=data['sg_wp__poi_cbg'].astype('int64')
    data['tract_id']=data['sg_wp__poi_cbg'].astype(str).str[:9].astype(int)

    return data





# a string funciton to get the
def namestr(obj,namespace=globals()):
    print(namespace.keys())
    return [name for name in namespace if namespace[name] is obj]


### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Functions for simple mapping using folium
### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def make_map_plot(df_,
                  plot_limit=3000,
                  radius_col=None,
                  radius_mod=100,
                  color='black',
                  fill_color='red',
                  fill_opacity = 0.2,
                  pop_up_col='pop_up_col',
                  tooltip = 'Click',
                  zoom_start=10,
                  tiles = 'OpenStreetMap',
                  map_width = 700,
                  map_height = 400,
                  marker_type= 'circle',
                  map_plot=None,
                  verbose=False):
#     title=namestr(df_)[0][-4:]

    # Parameters:
      # df_ is a pandas dataframe. It requires a column called "latitude" and a column called "longitude".
      # radius_col is a column_name or None. If None, every point is given a fixed radius.
          # Otherwise, the value in the column radius_col is used as the radius.
      # radius_mod is to scale your radius units to correspond to units on your map.
      # zoom_start is the scale of the map. Larger numbers = higher resolution.
      # color, fill_color, fill_opacity are marker parameters, see others: https://leafletjs.com/reference-1.3.4.html#path
      # tiles determines the base layer. Open source options include 'OpenStreetMap', 'Stamen Terrain', 'Stamen Toner'
      # map_width and map_height determine the size of the map image (in pixels)
      # marker_type determines what type of marker is being drawn on the map. Options: 'circle' or 'normal'

    # check valid inputs
    valid_inputs = {'marker_type' : {'val' : marker_type, 'valids' : ['circle', 'normal']},
                    'tiles' :  {'val' : tiles, 'valids': ['OpenStreetMap', 'Stamen Terrain', 'Stamen Toner', 'Mapbox Bright', 'Mapbox Control Room']},
                    'radius_col' : {'val' : radius_col, 'valids' : [None] + [col for col in df_.columns if pd.api.types.is_numeric_dtype(df_[col])]}}
    for param, param_valid_dict in valid_inputs.items():
      if(param_valid_dict['val'] not in param_valid_dict['valids']):
        raise Exception("Invalid parameter input for '{0}'. Valid options are {1}. input value was '{2}' .".format(param, param_valid_dict['valids'], param_valid_dict['val']))

    # create basemap
    if(not map_plot):
      map_plot = folium.Map(width=map_width,
                            height=map_height,
                            location=[df_.sg_c__latitude.mean(), df_.sg_c__longitude.mean()],
                            tiles=tiles,
                            zoom_start=zoom_start,
                            control_scale = True)

    # add markers
    counter = 0
    for index, row in df_.iterrows():
        counter+=1
        if(marker_type=='circle'):
          add_circle_marker_to_map(map_plot, row, radius_col, radius_mod, color, fill_color, fill_opacity, pop_up_col, tooltip)
        elif(marker_type=='normal'):
          add_marker_to_map(map_plot, row, pop_up_col, tooltip)
        if(counter>plot_limit): break
    if(verbose): print("Plotted {0} locations".format(counter))
    return(map_plot)



def add_marker_to_map(map_plot, row, pop_up_col, tooltip):
  folium.Marker([row.sg_c__latitude, row.sg_c__longitude],
                        popup= row[pop_up_col] if pop_up_col else None,
                        tooltip=tooltip if pop_up_col else None,
                   ).add_to(map_plot)
  return(None)


def add_circle_marker_to_map(map_plot, row, radius_col, radius_mod, color, fill_color, fill_opacity, pop_up_col, tooltip):
  folium.CircleMarker([row.sg_c__latitude, row.sg_c__longitude],
                        radius= row[radius_col]/radius_mod if radius_col else 2,
                        color = color,
                        fill_color = fill_color,
                        weight=0.5,
                        fill_opacity= fill_opacity,
                        popup= row[pop_up_col] if pop_up_col else None,
                        tooltip=tooltip if pop_up_col else None,
                   ).add_to(map_plot)
  return(None)



def category_dist(raw_data,title):
    # make bar plot of business category
    title = title
    category_counts = raw_data.groupby(['category'])['placekey'].count().to_frame(name='counts').reset_index()
    # category_counts=category_counts.sort_values('counts',ascending=False).reset_index()
    category_counts['counts_percent'] = (category_counts['counts'] /
                                         category_counts['counts'].sum()) * 100
    # main_type=category_counts['category'][:20].tolist()

    # bar ploat
    fig, ax = plt.subplots(1, 1, figsize=(10, 8))
    ax1 = plt.subplot(2, 1, 1)
    ax1.bar(category_counts['category'], category_counts['counts_percent'])
    ax1.set_title('count of categorical places in %s' % title, fontsize=18)
    plt.xticks(rotation=80)
    plt.savefig("../fig/counts_percent_bar_%s" % title + '.png')

    #     ax_2=category_counts.set_index('category').plot.pie(y='counts_percent', figsize=(12, 12))
    #     ax_2.set_title(('count of categorical places in %s'% title),pad=20, fontdict={'fontsize':20})
    #     plt.savefig("./fig/counts_percent_pie_%s"%title+'.png')
    return category_counts


def normalization_change(data):
    data = data.div(data.sum(axis=0))
    data['visit_counts_2021_2020'] = (data.iloc[:, 0] - data.iloc[:, 3]) / data.iloc[:, 3]
    data['visit_counts_2020_2019'] = (data.iloc[:, 3] - data.iloc[:, 6]) / data.iloc[:, 6]

    data['visitor_counts_2021_2020'] = (data.iloc[:, 1] - data.iloc[:, 4]) / data.iloc[:, 4]
    data['visitor_counts_2020_2019'] = (data.iloc[:, 4] - data.iloc[:, 7]) / data.iloc[:, 7]

    data['median_dwell_2021_2020'] = (data.iloc[:, 2] - data.iloc[:, 5]) / data.iloc[:, 5]
    data['median_dwell_2020_2019'] = (data.iloc[:, 5] - data.iloc[:, 8]) / data.iloc[:, 8]

    return data


def dwell_time(raw_data):
    title = namestr(raw_data)[0][-4:]

    data = raw_data.groupby(['category'])['sg_wp__raw_visit_counts', 'sg_wp__median_dwell_hour'].sum()
    data['sg_wp__raw_visit_counts'] = 100 * (
                data['sg_wp__raw_visit_counts'] / np.sum(raw_data['sg_wp__raw_visit_counts']))
    data['sg_wp__median_dwell_hour'] = 100 * (
                data['sg_wp__median_dwell_hour'] / np.sum(raw_data['sg_wp__median_dwell_hour']))
    data_1 = data.sort_values('sg_wp__raw_visit_counts', ascending=False).reset_index()

    data_2 = data.sort_values('sg_wp__median_dwell_hour', ascending=False).reset_index()

    ax_1 = data_1.set_index('category').plot.pie(y='sg_wp__raw_visit_counts', figsize=(12, 12))
    ax_1.set_title(("people's visiting count to POI in %s" % title), pad=20, fontdict={'fontsize': 20})
    plt.savefig("./fig/visit_counts%s" % title + '.png')

    ax_2 = data_2.set_index('category').plot.pie(y='sg_wp__median_dwell_hour', figsize=(12, 12))
    ax_2.set_title(("people's dwell hour to POI in %s" % title), pad=20, fontdict={'fontsize': 20})
    plt.savefig("./fig/dwell_time%s" % title + '.png')

    return data, data_1, data_2