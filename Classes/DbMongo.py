import pymongo

import os

class DbMongo:
    
    @staticmethod
    def getDB():
        user = os.environ['StefanyCampos']
        password = os.environ['Lauracampos11']
        cluster = os.environ['cluster0.6ypihks.mongodb.net']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )
 
        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db



