from multiprocessing import Pool
import time
import random
from pymongo import MongoClient

MONGO_URI = "mongodb://masteruser:******@insta360-1.cluster-ckutjdcz3cie.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false"

def run_query(user_id):
    client = MongoClient(MONGO_URI)
    db = client.get_database("insta360")
    media = db.media_100k  

    query_duration = 120

    start_time = time.time()
    end_time = start_time + query_duration

    while time.time() < end_time:
        user_id = random.randint(1,99999)
        
        startquery_time = time.time()
        result_count = media.count_documents({
            "$and": [
                {"userId": user_id},
                {"lastUpdatePosition": {"$gt": 0}}
            ]
        })
        endquery_time = time.time()

        print(f"{(endquery_time - startquery_time)*1000}")

    # 关闭连接
    client.close()

if __name__ == "__main__":
    # 创建进程池
    with Pool(processes=60) as pool:
        # 执行 40 个并发查询
        #pool.map(run_query, range(10))
        pool.map(run_query, [985] * 60)
