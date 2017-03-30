import os
from cassandra.cluster import Cluster


class DbConfig:

    #hosts = os.getenv("CASSANDRA_HOSTS")

    cluster = Cluster()
    cassandra_session = cluster.connect()

    @staticmethod
    def get_db_connection():
        if DbConfig.cassandra_session is None:
            #hosts = os.getenv("CASSANDRA_HOSTS")
            #hosts = '127.0.0.1'
            cluster = Cluster()
            DbConfig.cassandra_session = cluster.connect()
            return DbConfig.cassandra_session
        else:
            return DbConfig.cassandra_session
