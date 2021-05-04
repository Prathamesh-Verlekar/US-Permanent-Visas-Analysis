import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

total_data = open('D:/Spring 2021/BigData/US_Permanent_Visa.csv', encoding = "ISO-8859-1")
us_app=pd.read_csv(total_data)
us_app['decision_date'] = pd.to_datetime(us_app['decision_date'])
# Applied Year
us_app['applied_year'] = pd.DatetimeIndex(us_app['decision_date']).year
# Total Cases
total_cases = us_app['case_status'].count()
# Total Approved
us_approved =us_app[us_app['case_status']=='Approved']
total_approved=us_approved['case_status'].count()
# Total Denied
us_denied =us_app[us_app['case_status']=='Denied']
total_denied=us_denied['case_status'].count()
# Total Withdrawn
us_withdrawn =us_app[us_app['case_status']=='Withdrawn']
total_withdrawn=us_withdrawn['case_status'].count()

# create dictionary of list
country_data_list = us_app[['country_of_citizenship','latitude','longitude']]
dict_of_locations = country_data_list.set_index(['country_of_citizenship'])[['latitude','longitude']].T.to_dict('dict')


app = dash.Dash(__name__,)

app.layout =html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('corona-logo-1.jpg'),
                     id='corona-image',
                     style={'height': '80px',
                            'width': 'auto',
                            'margin-bottom': '25px'})

        ],className='one-third column'),
        html.Div([
            html.Div([
                html.H3('US-VISA-APPLICATION', style={'margin-bottom': '0px', 'color': 'white'}),
                html.H5('TRACKER-US', style={'margin-bottom': '0px', 'color': 'white'})
            ])
        ],className='one-half column', id ='title'),
        html.Div([
            html.H6('Last Updated: ' +str(us_app['decision_date'].iloc[-1].strftime('%B %d, %Y'))+ ' 00:01 (ET)',
                    style={'color':'orange'})

        ],className='one-third column', id='title1')

    ], id ='header', className='row flex-display', style={'margin-bottom': '25px'}),
    html.Div([
        html.Div([
            html.H6(children='Total Cases',
                    style={'textAlign':'center',
                           'color':'white'}),
            html.P(f"{total_cases:,.0f}",
                    style={'textAlign':'center',
                           'color':'orange',
                           'fontSize':40})
        ],className='card_container three columns'),
    html.Div([
            html.H6(children='Total Approved',
                    style={'textAlign':'center',
                           'color':'white'}),
            html.P(f"{total_approved:,.0f}",
                    style={'textAlign':'center',
                           'color':'green',
                           'fontSize':40})
        ],className='card_container three columns'),
    html.Div([
            html.H6(children='Total Denied',
                    style={'textAlign':'center',
                           'color':'white'}),
            html.P(f"{total_denied:,.0f}",
                    style={'textAlign':'center',
                           'color':'#dd1e35',
                           'fontSize':40})
        ],className='card_container three columns'),
    html.Div([
            html.H6(children='Total Withdrawn',
                    style={'textAlign':'center',
                           'color':'white'}),
            html.P(f"{total_withdrawn:,.0f}",
                    style={'textAlign':'center',
                           'color':'#e55467',
                           'fontSize':40})
        ],className='card_container three columns')
    ], className='row flex display'),
    html.Div([
        html.Div([
            html.P('Select Class Admission:', className='fix_label',style={'color':'white'}),
            dcc.Dropdown(id ='w_countries',
                         multi= False,
                         searchable= True,
                         value='F-1',
                         placeholder='select Class Admission',
                         options=[{'label': c,'value':c}
                                  for c in (us_app['class_of_admission'].unique())],className='dcc_compon'),
            html.P(
                   className='fix_label',style={'text-align':'center','color':'white'}),
            dcc.Graph(id= 'confirmed', config={'displayModeBar':False},className='dcc_compon',
                      style={'margin-top':'20px'}),
            dcc.Graph(id= 'denied', config={'displayModeBar':False},className='dcc_compon',
                      style={'margin-top':'20px'}),
            dcc.Graph(id= 'withdrawn', config={'displayModeBar':False},className='dcc_compon',
                      style={'margin-top':'20px'})

        ],className='create_container three columns'),
        html.Div([
            dcc.Graph(id= 'pie_chart', config={'displayModeBar':'hover'}
                      )
        ],className='create_container four columns'),
        html.Div([
            dcc.Graph(id= 'line_chart', config={'displayModeBar':'hover'}
                      )
        ],className='create_container five columns')
    ], className='row flex-display'),
html.Div([
        html.Div([

            html.P('Select By State:', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_State',
                         multi=False,
                         searchable=True,
                         value='RI',
                         placeholder='State Name:',
                         options=[{'label': c, 'value': c}
                                  for c in (us_app['employer_state'].unique())], className='dcc_compon'),
            html.P('Select By City:', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_city',
                         multi=False,
                         searchable=True,
                         value='',
                         placeholder='City Name:',
                         options=[], className='dcc_compon'),
            html.P('Select By Company:', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_company',
                         multi=False,
                         searchable=True,
                         value='',
                         placeholder='Company Name:',
                         options=[], className='dcc_compon')

        ],className='create_container three columns'),
        html.Div([
                dcc.Graph(id='bar_chart_company', config={'displayModeBar': 'hover'}
                          )
            ], className='create_container nine columns')
    ], className='row flex-display'),
html.Div([
html.Div([
            html.P('Select By Country:', className='fix_label',style={'color':'white'}),
            dcc.Dropdown(id ='w_region',
                         multi= False,
                         searchable= True,
                         value='India',
                         placeholder='select By Country:',
                         options=[{'label': c,'value':c}
                                  for c in (us_app['country_of_citizenship'].unique())],className='dcc_compon')
],className='create_container three columns'),
html.Div([
    dcc.Graph(id='map_chart',config={'displayModeBar': 'hover'}
              )
], className='create_container1 nine columns')
    ],className='row flex-display'),
html.Div([
        html.Div([
            html.P('Select By Title:', className='fix_label',style={'color':'white'}),
            dcc.Dropdown(id ='w_titles',
                         multi= False,
                         searchable= True,
                         value='Computer Systems Analysts',
                         placeholder='select By Title:',
                         options=[{'label': c,'value':c}
                                  for c in (us_app['pw_soc_title'].unique())],className='dcc_compon'),
            html.P(
                   className='fix_label',style={'text-align':'center','color':'white'}),
            dcc.Graph(id= 'confirmed_titles', config={'displayModeBar':False},className='dcc_compon',
                      style={'margin-top':'20px'}),
            dcc.Graph(id= 'denied_titles', config={'displayModeBar':False},className='dcc_compon',
                      style={'margin-top':'20px'}),
            dcc.Graph(id= 'withdrawn_titles', config={'displayModeBar':False},className='dcc_compon',
                      style={'margin-top':'20px'})

        ],className='create_container three columns'),
        html.Div([
            dcc.Graph(id= 'pie_chart_titles', config={'displayModeBar':'hover'}
                      )
        ],className='create_container four columns'),
        html.Div([
            dcc.Graph(id= 'line_chart_titles', config={'displayModeBar':'hover'}
                      )
        ],className='create_container five columns')
    ], className='row flex-display')
], id = 'mainContainer', style={'display': 'flex', 'flex-direction': 'column'})



@app.callback(Output('confirmed_titles','figure'),
              [Input('w_titles','value')])
def update_confirmed(w_titles):
    value_approved = us_approved[us_approved['pw_soc_title']==w_titles].case_status.count()
    return{
        'data':[go.Indicator(
            mode='number',
            value=value_approved,
            number={'valueformat':',',
                    'font': {'size':20}},
            domain={'y':[0,1],'x':[0,1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total Approved',
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            font=dict(color='green'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50,
        )
    }

@app.callback(Output('denied_titles','figure'),
              [Input('w_titles','value')])
def update_confirmed(w_titles):
    value_denied = us_denied[us_denied['pw_soc_title']==w_titles].case_status.count()
    return{
        'data':[go.Indicator(
            mode='number',
            value=value_denied,
            number={'valueformat':',',
                    'font': {'size':20}},
            domain={'y':[0,1],'x':[0,1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total Denied',
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            font=dict(color='red'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50,
        )
    }

@app.callback(Output('withdrawn_titles','figure'),
              [Input('w_titles','value')])
def update_confirmed(w_titles):
    value_withdrawn = us_withdrawn[us_withdrawn['pw_soc_title']==w_titles].case_status.count()
    return{
        'data':[go.Indicator(
            mode='number',
            value=value_withdrawn,
            number={'valueformat':',',
                    'font': {'size':20}},
            domain={'y':[0,1],'x':[0,1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total Withdrawn',
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            font=dict(color='#e55467'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50,
        )
    }


@app.callback(Output('pie_chart_titles','figure'),
              [Input('w_titles','value')])
def update_graph(w_titles):
    approved_value = us_approved[us_approved['pw_soc_title'] == w_titles].case_status.count()
    denied_value = us_denied[us_denied['pw_soc_title'] == w_titles].case_status.count()
    withdrawn_value = us_withdrawn[us_withdrawn['pw_soc_title']==w_titles].case_status.count()
    colors=['green','red','#e55467']
    return{
        'data':[go.Pie(
            labels=['Approved','Denied','Withdrawn'],
            values=[approved_value,denied_value,withdrawn_value],
            marker=dict(colors=colors),
            hoverinfo='label+value+percent',
            textinfo= 'label+value',
            hole=.7,
            rotation= 45
            #insidetextorientation='radial'

        )],

        'layout': go.Layout(
            title={'text': 'Title : ' + (w_titles),
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            titlefont={'color':'white',
                       'size':20},
            font=dict(family='sans-serif',
                      color ='white',
                      size =12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation':'h',
                    'bgcolor':'#1f2c56',
                    'xanchor':'center','x':0.5,'y':-0.7}
        )
    }

@app.callback(Output('line_chart_titles','figure'),
              [Input('w_titles','value')])
def update_graph(w_titles):
    approved_value = us_approved[us_approved['pw_soc_title'] == w_titles].groupby('applied_year').count().case_status
    denied_value = us_denied[us_denied['pw_soc_title'] == w_titles].groupby('applied_year').count().case_status
    withdrawn_value = us_withdrawn[us_withdrawn['pw_soc_title'] == w_titles].groupby('applied_year').count().case_status
    applied_year = us_approved['applied_year'].unique()
    return{
        'data':[go.Bar(
            x = applied_year,
            y = approved_value,
            text= approved_value,
            texttemplate='%{text:, .0f}',
            textposition='auto',
            name='Approved',
            marker=dict(color='orange'),
            hoverinfo='text',
            #hovertext='<b>Year</b>' + applied_year + '<br>' +
            #'<b>Approved Cases</b>' + approved_value + '<br>'

        ),
            go.Bar(
                x=applied_year,
                y=denied_value,
                text=denied_value,
                texttemplate='%{text:, .0f}',
                textposition='auto',
                name='denied',
                marker=dict(color='red'),
                hoverinfo='text',
                # hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
                # '<b>Approved Cases</b>' + approved_value  + '<br>'

            ),
            go.Bar(
                x=applied_year,
                y=withdrawn_value,
                text=withdrawn_value,
                texttemplate='%{text:, .0f}',
                textposition='auto',
                name='withdrawn',
                marker=dict(color='#e55467'),
                hoverinfo='text',
                # hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
                # '<b>Approved Cases</b>' + approved_value  + '<br>'

            )
        ],

        'layout': go.Layout(
            barmode= 'stack',
            title={'text': 'Titles: ' + (w_titles),
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            titlefont={'color':'white',
                       'size':20},
            font=dict(family='sans-serif',
                      color ='white',
                      size =12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation':'h',
                    'bgcolor':'#1f2c56',
                    'xanchor':'center','x':0.5,'y':-0.7},
            margin=dict(r=0),
            xaxis= dict(title='<b>Date</b>',
                        color = 'white',
                        showline= True,
                        showgrid= True,
                        showticklabels = True,
                        linecolor = 'white',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Aerial',
                            color = 'white',
                            size=12
                        )),
            yaxis=dict(title='<b>Cases</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='white',
                           size=12
                       ))
        )
    }
@app.callback(Output('confirmed','figure'),
              [Input('w_countries','value')])
def update_confirmed(w_countries):
    value_approved = us_approved[us_approved['class_of_admission']==w_countries].case_status.count()
    return{
        'data':[go.Indicator(
            mode='number',
            value=value_approved,
            number={'valueformat':',',
                    'font': {'size':20}},
            domain={'y':[0,1],'x':[0,1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total Approved',
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            font=dict(color='green'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50,
        )
    }

@app.callback(Output('denied','figure'),
              [Input('w_countries','value')])
def update_confirmed(w_countries):
    value_denied = us_denied[us_denied['class_of_admission']==w_countries].case_status.count()
    return{
        'data':[go.Indicator(
            mode='number',
            value=value_denied,
            number={'valueformat':',',
                    'font': {'size':20}},
            domain={'y':[0,1],'x':[0,1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total Denied',
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            font=dict(color='red'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50,
        )
    }

@app.callback(Output('withdrawn','figure'),
              [Input('w_countries','value')])
def update_confirmed(w_countries):
    value_withdrawn = us_withdrawn[us_withdrawn['class_of_admission']==w_countries].case_status.count()
    return{
        'data':[go.Indicator(
            mode='number',
            value=value_withdrawn,
            number={'valueformat':',',
                    'font': {'size':20}},
            domain={'y':[0,1],'x':[0,1]}
        )],

        'layout': go.Layout(
            title={'text': 'Total Withdrawn',
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            font=dict(color='#e55467'),
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            height=50,
        )
    }

@app.callback(Output('pie_chart','figure'),
              [Input('w_countries','value')])
def update_graph(w_countries):
    approved_value = us_approved[us_approved['class_of_admission'] == w_countries].case_status.count()
    denied_value = us_denied[us_denied['class_of_admission'] == w_countries].case_status.count()
    withdrawn_value = us_withdrawn[us_withdrawn['class_of_admission']==w_countries].case_status.count()
    colors=['green','red','#e55467']
    return{
        'data':[go.Pie(
            labels=['Approved','Denied','Withdrawn'],
            values=[approved_value,denied_value,withdrawn_value],
            marker=dict(colors=colors),
            hoverinfo='label+value+percent',
            textinfo= 'label+value',
            hole=.7,
            rotation= 45
            #insidetextorientation='radial'

        )],

        'layout': go.Layout(
            title={'text': 'Class Of Admission: ' + (w_countries),
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            titlefont={'color':'white',
                       'size':20},
            font=dict(family='sans-serif',
                      color ='white',
                      size =12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation':'h',
                    'bgcolor':'#1f2c56',
                    'xanchor':'center','x':0.5,'y':-0.7}
        )
    }

@app.callback(Output('line_chart','figure'),
              [Input('w_countries','value')])
def update_graph(w_countries):
    approved_value = us_approved[us_approved['class_of_admission'] == w_countries].groupby('applied_year').count().case_status
    denied_value = us_denied[us_denied['class_of_admission'] == w_countries].groupby('applied_year').count().case_status
    withdrawn_value = us_withdrawn[us_withdrawn['class_of_admission'] == w_countries].groupby('applied_year').count().case_status
    applied_year = us_approved['applied_year'].unique()
    return{
        'data':[go.Bar(
            x = applied_year,
            y = approved_value,
            text=approved_value,
            texttemplate='%{text:, .0f}',
            textposition='auto',
            name='Approved',
            marker=dict(color='orange'),
            hoverinfo='text',
            #hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
            #'<b>Approved Cases</b>' + approved_value  + '<br>'

        ),
            go.Bar(
                x=applied_year,
                y=denied_value,
                text=denied_value,
                texttemplate='%{text:, .0f}',
                textposition='auto',
                name='denied',
                marker=dict(color='red'),
                hoverinfo='text',
                # hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
                # '<b>Approved Cases</b>' + approved_value  + '<br>'

            ),
            go.Bar(
                x=applied_year,
                y=withdrawn_value,
                text=withdrawn_value,
                texttemplate='%{text:, .0f}',
                textposition='auto',
                name='withdrawn',
                marker=dict(color='#e55467'),
                hoverinfo='text',
                # hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
                # '<b>Approved Cases</b>' + approved_value  + '<br>'

            )],

        'layout': go.Layout(
            barmode= 'stack',
            title={'text': 'Cases by Year: ' + (w_countries),
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            titlefont={'color':'white',
                       'size':20},
            font=dict(family='sans-serif',
                      color ='white',
                      size =12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation':'h',
                    'bgcolor':'#1f2c56',
                    'xanchor':'center','x':0.5,'y':-0.7},
            margin=dict(r=0),
            xaxis= dict(title='<b>Date</b>',
                        color = 'white',
                        showline= True,
                        showgrid= True,
                        showticklabels = True,
                        linecolor = 'white',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Aerial',
                            color = 'white',
                            size=12
                        )),
            yaxis=dict(title='<b>Cases</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='white',
                           size=12
                       ))
        )
    }

@app.callback(Output('map_chart','figure'),
              [Input('w_region','value')])
def update_graph(w_region):
    approved_value = us_approved[us_approved['country_of_citizenship'] == w_region].groupby(['latitude','longitude','country_of_citizenship']).count().case_status
    denied_value = us_denied[us_denied['country_of_citizenship'] == w_region].groupby(['latitude','longitude','country_of_citizenship']).count().case_status
    withdrawn_value = us_withdrawn[us_withdrawn['country_of_citizenship'] == w_region].groupby(['latitude','longitude','country_of_citizenship']).count().case_status
    applied_year = us_approved['applied_year'].unique()
    country_map = us_app[us_app['country_of_citizenship'] == w_region]

    if w_region:
        zoom = 2
        zoom_lat = dict_of_locations[w_region]['latitude']
        zoom_long = dict_of_locations[w_region]['longitude']

    return{
        'data':[go.Scattermapbox(
            lon=country_map['longitude'].unique(),
            lat=country_map['latitude'].unique(),
            mode='markers',
            marker=go.scattermapbox.Marker(size=approved_value/10,
                                           color=approved_value,
                                           colorscale='HSV',
                                           showscale=False,
                                           sizemode='area',
                                           opacity=0.3),
            hoverinfo='text',
            hovertext='<b>Country</b>: ' + w_region + '<br>' +
            '<b>Longitude</b>: ' + country_map['longitude'].astype(str)+ '<br>' +
            '<b>Latitude</b>: ' + country_map['latitude'].astype(str) + '<br>'+
            '<b>Approved Cases</b>: ' + [f'{x:,.0f}' for x in approved_value] + '<br>' +
            '<b>Denied Cases</b>: ' + [f'{x:,.0f}' for x in denied_value] + '<br>' +
            '<b>Withdrawn Cases</b>: ' + [f'{x:,.0f}' for x in withdrawn_value] + '<br>'


        )],

        'layout': go.Layout(
            hovermode= 'x',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            margin=dict(r=0, l=0, b=0, t=0),
            mapbox=dict(
                accesstoken = 'pk.eyJ1IjoicGFuZHlheSIsImEiOiJja25xcTEzeTcwOXhsMnZvZ3pzeDV5cnZiIn0.N9aMzT04vMcJqwYHCwkHWA',
                center = go.layout.mapbox.Center(lat=zoom_lat,lon=zoom_long),
                style='dark',
                zoom = zoom,

            ),
            autosize= True
        )
    }

@app.callback(Output('w_city','options'),
              [Input('w_State','value')])
def update_country(w_State):
    city_select = us_app[us_app['employer_state']==w_State]
    return [{'label': i , 'value': i} for i in city_select['employer_city'].unique()]

@app.callback(Output('w_city','value'),
              [Input('w_city','options')])
def update_country(w_city):
    return [k['value'] for k in w_city][0]

@app.callback(Output('w_company','options'),
              [Input('w_city','value')])
def update_city(w_city):
    company_select = us_app[us_app['employer_city']==w_city]
    return [{'label': i , 'value': i} for i in company_select['employer_name'].unique()]

@app.callback(Output('w_company','value'),
              [Input('w_company','options')])
def update_city(w_company):
    return [k['value'] for k in w_company][0]

@app.callback(Output('bar_chart_company','figure'),
              [Input('w_company','value')])
def update_graph(w_company):
    approved_value = us_approved[us_approved['employer_name'] == w_company].groupby('applied_year').count().case_status
    denied_value = us_denied[us_denied['employer_name'] == w_company].groupby('applied_year').count().case_status
    withdrawn_value = us_withdrawn[us_withdrawn['employer_name'] == w_company].groupby('applied_year').count().case_status
    applied_year = us_approved['applied_year'].unique()
    return{
        'data':[go.Bar(
            x = applied_year,
            y = approved_value,
            text= approved_value,
            texttemplate='%{text:, .0f}',
            textposition='auto',
            name='Approved',
            marker=dict(color='orange'),
            hoverinfo='text',
            #hovertext='<b>Year</b>' + applied_year + '<br>' +
            #'<b>Approved Cases</b>' + approved_value + '<br>'

        ),
            go.Bar(
                x=applied_year,
                y=denied_value,
                text=denied_value,
                texttemplate='%{text:, .0f}',
                textposition='auto',
                name='denied',
                marker=dict(color='red'),
                hoverinfo='text',
                # hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
                # '<b>Approved Cases</b>' + approved_value  + '<br>'

            ),
            go.Bar(
                x=applied_year,
                y=withdrawn_value,
                text=withdrawn_value,
                texttemplate='%{text:, .0f}',
                textposition='auto',
                name='withdrawn',
                marker=dict(color='#e55467'),
                hoverinfo='text',
                # hovertext='<b>Year</b>' + applied_year.astype(str) + '<br>' +
                # '<b>Approved Cases</b>' + approved_value  + '<br>'

            )
        ],

        'layout': go.Layout(
            barmode= 'stack',
            title={'text': 'Company: ' + (w_company),
                   'y':1,
                   'x':0.5,
                   'xanchor':'center',
                   'yanchor':'top'},
            titlefont={'color':'white',
                       'size':20},
            font=dict(family='sans-serif',
                      color ='white',
                      size =12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation':'h',
                    'bgcolor':'#1f2c56',
                    'xanchor':'center','x':0.5,'y':-0.7},
            margin=dict(r=0),
            xaxis= dict(title='<b>Date</b>',
                        color = 'white',
                        showline= True,
                        showgrid= True,
                        showticklabels = True,
                        linecolor = 'white',
                        linewidth = 1,
                        ticks = 'outside',
                        tickfont = dict(
                            family = 'Aerial',
                            color = 'white',
                            size=12
                        )),
            yaxis=dict(title='<b>Cases</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Aerial',
                           color='white',
                           size=12
                       ))
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)