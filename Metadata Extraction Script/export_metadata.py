# -*- coding: utf-8 -*-

import pandas as pd
import pygsheets
from pandas import DataFrame
from py2neo import Graph

'''
Dependencies - Install py2neo, pandas and pygsheets ; For ex: pip install py2neo
Compatible with Python 3.7+
Link to Google Sheet: https://docs.google.com/spreadsheets/d/1rTQeW2DbqpxNK0CBypdsx4ZgK3Kz0E8xk2FgXo37HqQ/edit?usp=sharing
Make sure the service_account.json file is in the same directory as your Python script - else provide the complete path to service_account.json file
Every time the script is re-run, it overwrites the old data on your team's sheet
Requires the use of APOC (https://neo4j.com/labs/apoc/) - make sure you install the plugin by going to Database > Plugins > APOC > Install
'''


# Connect to Neo4j - enter your connection params here
uri = "bolt://localhost:7687"
username = "neo4j"
pwd = "groupproject"

# Enter your team number here - so that the data can be pushed to the appropriate sheet
# Default is 0 - which writes to the Demo Sheet
team = 8

# Enter your DB Name
db_name = 'US Perm Visas'

def write2gsheets(df):
    # Find the service account file to allow writing to the gsheet
    gc = pygsheets.authorize(service_file='service_account.json')

    # open the google spreadsheet
    sh = gc.open('csye7250-metadata')

    # Write to Sheet
    wks = sh[team]
    wks.set_dataframe(df, (1, 1))

    print ("Data written to Google Sheet - for team %s" %team)


def getData():
    session = None
    try:
        session = Graph(uri, auth=(username, pwd))
        print("Connected to Neo4j")
    except Exception as e:
        print('Could not connect to Neo4j. Error Details: %s' % e)

    # APOC cypher to get all the node labels and properties
    query = ''' CALL apoc.meta.schema() YIELD value as schemaMap
    UNWIND keys(schemaMap) as label
    WITH label, schemaMap[label] as data
    WHERE data.type = "node"
    UNWIND keys(data.properties) as property
    WITH label, property, data.properties[property] as propData
    RETURN label,
    property,
    propData.type as type,
    propData.indexed as isIndexed,
    propData.unique as uniqueConstraint,
    propData.existence as existenceConstraint '''

    # access the result data
    result = session.run(query).data()

    # convert result into pandas dataframe
    df = DataFrame(result)

    # Get the counts for all Node Labels
    countsQuery = '''
    MATCH (n) 
    RETURN DISTINCT count(labels(n)) as counts, labels(n) as label;
    '''
    # access the result data
    result = session.run(countsQuery).data()
    df_counts = DataFrame(result)
    df_counts['label'] = df_counts['label'].str[0]

    # merge both dataframes based on label to get the node counts in the original df
    df = pd.merge(df_counts, df, how='left')

    # Add team number - to make it easy for the data ingestion team
    df["team"] = team

    df["dbName"] = db_name

    print ("\nExtracted Labels and Attributes - Snapshot:\n")
    print (df)
    # Add empty field to populate later
    df["relationships"] = ""

    # Loop through all the labels to get list of associated relationships
    for i in df.label.unique():
        print("Getting relationships for Node Label: %s" % i)

        relationshipQuery = '''
        MATCH (p1:%s)
        RETURN apoc.node.relationship.types(p1) AS output;
        ''' % i

        # Get results
        result = session.run(relationshipQuery).data()

        # Since a node may have one or more relationships & we want the list of ALL relationships -
        # some data wrangling to find max of length of all values in returned df and choose the one with max length
        # dirty implementation but works
        relationships = DataFrame(result).loc[DataFrame(result).output.astype(str).map(len).argmax(), 'output']

        # Update the relationships against the node label
        df.loc[df.label == i, 'relationships'] = ','.join(relationships)

    print ("\nExtracted all metadata. Snapshot:\n")
    print(df)

    # Call the function and pass the dataframe to write to google sheets
    write2gsheets(df)


if __name__ == "__main__":
    getData()
