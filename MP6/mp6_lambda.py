import json
import sys
import logging
import redis
import pymysql


DB_HOST = "database-mp6.cluster-ro-ckpzvytub95c.us-east-1.rds.amazonaws.com"
DB_USER = "admin"
DB_PASS = "adminmp6"
DB_NAME = "mp6"
DB_TABLE = "heroes"
REDIS_URL = "redis://mp6-cluster.aonr9n.ng.0001.use1.cache.amazonaws.com:6379"

TTL = 10

class DB:
    def __init__(self, **params):
        params.setdefault("charset", "utf8mb4")
        params.setdefault("cursorclass", pymysql.cursors.DictCursor)

        self.mysql = pymysql.connect(**params)

    def query(self, sql):
        with self.mysql.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()

    def get_idx(self, table_name):
        with self.mysql.cursor() as cursor:
            cursor.execute(f"SELECT MAX(id) as id FROM {table_name}")
            idx = str(cursor.fetchone()['id'] + 1)
            return idx

    def insert(self, idx, data):
        with self.mysql.cursor() as cursor:
            hero = data["hero"]
            power = data["power"]
            name = data["name"]
            xp = data["xp"]
            color = data["color"]
            
            sql = f"INSERT INTO heroes ('id', 'hero', 'power', 'name', 'xp', 'color') VALUES ('{idx}', '{hero}', '{power}', '{name}', '{xp}', '{color}')"

            cursor.execute(sql)
            self.mysql.commit()

def read(use_cache, indices, Database, Cache):
    sql = f"SELECT * FROM heroes WHERE id in {indices}"
    result = []
    if use_cache:
        # if Redis contains the data with given id. if not, read row from RDS, store in Redis
        for i in indices:
            res = Cache.hgetall(i)
            if res:
                Cache.hmset(i, res)
                Cache.expire(i, TTL)
                result.append(res)
            else:
                res = Database.query(sql)
                Cache.setex(sql, TTL, json.dumps(res))
    else:
        result = Database.query(sql)
    return json.loads(result)
    
def write(use_cache, sqls, Database, Cache):
    if use_cache:
        # write through strategy
        for sql in sqls:
            res = Cache.set(sql)
            Cache.setex(sql, TTL, json.dumps(res))

    else:
        for sql in sqls:
            idx = Database.get_idx('heroes')
            Database.insert(idx, sql)

def lambda_handler(event, context):
    
    USE_CACHE = (event['USE_CACHE'] == "True")
    REQUEST = event['REQUEST']
    
    # initialize database and cache
    try:
        Database = DB(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DB_NAME)
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()
        
    Cache = redis.Redis.from_url(REDIS_URL)
    print("Connected to REDIS? {0} ".format(Cache.ping()))
    
    result = []
    if REQUEST == "read":
        # event["SQLS"] should be a list of integers
        result = read(USE_CACHE, event["SQLS"], Database, Cache)
    elif REQUEST == "write":
        # event["SQLS"] should be a list of jsons
        write(USE_CACHE, event["SQLS"], Database, Cache)
        result = "write success"
    
    
    return {
        'statusCode': 200,
        'body': result
    }
