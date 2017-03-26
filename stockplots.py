# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:52:04 2017

@author: pinsley
"""

import time
from datetime import date as dt
from datetime import timedelta
import requests as rq
from bokeh.plotting import figure, output_file, save

#import json
#import numpy

def make_ticker_plot(ticker):
 
    this_day = time.strftime("%d")
    this_month = int(time.strftime("%m"))
    this_year = int(time.strftime("%Y"))
    
    last_day = this_day
    
    if this_month == 1:
        last_month = 12
        last_year = this_year-1
    else:
        last_month = this_month -1
        last_year = this_year
    
    if this_month < 10:
        this_month = '0' + str(this_month)
    else:
        this_month = str(this_month)
    
    if last_month < 10:
        last_month = '0' + str(last_month)
    else:
        last_month = str(last_month)
        
    this_year = str(this_year); last_year = str(last_year)
    
    
    URL_1 = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?'
    start_date = 'date.gte=' + last_year + last_month + last_day
    end_date = '&date.lt=' + this_year + this_month + this_day
    URL_2 = start_date + end_date + '&ticker=' + ticker + '&api_key=zrN-ny8EUaZiLH89z4zr'
    URL = URL_1 + URL_2
    r = rq.get(URL, auth=('peter.insley@gmail.com', 'numeracyisking'))
    input_data = r.json()
    input_data = input_data['datatable']['data']
    data = [input_data[i][5] for i in range(0,len(input_data))]
    dates = [input_data[i][1] for i in range(0,len(input_data))]
    
    corrected_data = []; corrected_data.append(data[0])
    
    corrected_dates = [];
    former_date = str(dates[0])
    former_day = int(former_date[-2:])
    former_month = int(former_date[-5:-3])
    former_year = int(former_date[0:4])
    corrected_dates.append(dt(former_year,former_month,former_day))
    
    former_index = 0
    for index, this_date in enumerate(dates[1:]):
        this_date = str(this_date)
        day = int(this_date[-2:])
        month = int(this_date[-5:-3])
        year = int(this_date[0:4])
        delta =  dt(year,month,day) - dt(former_year,former_month,former_day)
        diff = delta.days
        
        for index2 in range(0,max(diff-1,0)):
            corrected_data.append(data[former_index+1])
            
            tmp_date_object = dt(former_year,former_month,former_day) 
            new_tmp_date = tmp_date_object + timedelta(days=index2+1)
            new_year = new_tmp_date.year
            new_month = new_tmp_date.month
            new_day = new_tmp_date.day
            
            corrected_dates.append(dt(new_year,new_month,new_day))
     
     # code here is slightly backward; originally written in a logical way,
     # awkwardly altered to make work with datetime data type without rewrite
        corrected_data.append(data[index+1])
        newest_date = dates[index+1]
        newest_day = int(newest_date[-2:])
        newest_month = int(newest_date[-5:-3])
        newest_year = int(newest_date[0:4])
        corrected_dates.append(dt(newest_year,newest_month,newest_day))
        
        former_day = day
        former_month= month
        former_year = year
        former_index = index
        
    output_file('./templates/datetime.html')
    this_title = "Closing prices for " + ticker.upper() + " stock over the last month.\r"
    p = figure(title = this_title, width=800, height=400, x_axis_type="datetime")
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Share price in dollars'
    p.xaxis[0].ticker.desired_num_ticks = len(corrected_dates)
    p.line(corrected_dates,corrected_data, line_width=3, line_color='red')
    save(p,title='Stock price plot')
