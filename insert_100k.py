from faker import Faker
from datetime import datetime
from random import randint, choice
import pymongo
from bson.int64 import Int64

#client = pymongo.MongoClient("mongodb://sharon:******1@docdb-2024-10-09-05-15-02.cluster-ctfokeestnyw.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
client = pymongo.MongoClient("mongodb://masteruser:******1@insta360-1.cluster-ckutjdcz3cie.us-east-1.docdb.amazonaws.com:27017/?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false")
db = client["insta360"]
media_collection = db["media_100k"]

fake = Faker()

for i in range(1, 100001):
#for _ in range(1000):
    #user_id = randint(1, 1000000) 
    user_id = i
    media_type = choice(['image', 'video', 'audio'])
    title = fake.sentence(nb_words=5)
    caption = fake.sentence(nb_words=10)
    media_url = fake.url()
    thumbnail_url = fake.image_url() if media_type == 'image' else None
    shoot_time = fake.date_time_between(start_date='-1y', end_date='now').timestamp() * 1000
    size = randint(1000000, 500000000)  # 文件大小在1MB到500MB之间
    delete_status = 'normal'
    create_time = fake.date_time_between(start_date='-1y', end_date='now')
    create_time_ms = int(create_time.timestamp() * 1000)
    update_time = fake.date_time_between(start_date=create_time, end_date='now')
    update_time_ms = int(update_time.timestamp() * 1000)
    file_items = [fake.file_name(extension='lrv'), fake.file_name(extension='insv')]
    audit_status = randint(0, 2)
    last_update_position = Int64(randint(1000, 99999))
    upload_status = choice(['start_upload', 'uploading', 'end_upload'])
    upload_time = fake.date_time_between(start_date='-1y', end_date='now').timestamp() * 1000
    tool_version = fake.numerify(text="##.##.###")
    process_status = {
        'r4view': choice([True, False]),
        'error': choice([True, False]),
        'played': choice([True, False]),
        'r4play': choice([True, False])
    }
    upload_finish_time = fake.date_time_between(start_date='-1y', end_date='now').timestamp() * 1000
    camera_type = 'Insta360 X4'
    file_info = {
        'size': size,
        'format': 'insv',
        'ict_version': tool_version,
        'creationtime': fake.date_time_between(start_date='-1y', end_date='now').strftime('%Y-%m-%d %H:%M'),
        'cameratype': camera_type
    }
    height = 3840
    metadata = fake.binary(length=1024)  # 随机二进制数据
    plane_thumb = {
        'bucket': 'insta360-cloud-shenzhen-internal',
        'object': f'cloud-test/c184/{Int64(randint(1000, 99999))}/{fake.date_time_this_year().strftime("%Y%m%d%H%M%S")}/tl/thumbnail_320-320.jpg'
    }
    shoot_mode = randint(0, 2)
    tab = randint(0, 2)
    thumb = {
        'bucket': 'insta360-cloud-shenzhen-internal',
        'object': f'cloud-test/c184/{Int64(randint(1000, 99999))}/{fake.date_time_this_year().strftime("%Y%m%d%H%M%S")}/tl/thumbnail_640-320.jpg'
    }
    version = tool_version
    video_duration = randint(1000, 60000)
    video_info = {
        'distance': str(fake.pydecimal(right_digits=18, positive=True)),
        'framerate': str(fake.pydecimal(right_digits=18, positive=True)),
        'ict_version': tool_version,
        'index': randint(0, 10),
        'bitrate': str(fake.pydecimal(right_digits=18, positive=True)),
        'fov': str(fake.pydecimal(right_digits=18, positive=True)),
        'resolution': {
            'w': 7680,
            'h': 3840
        },
        'submediatype': randint(0, 10),
        'catagory': randint(0, 10),
        'duration': str(fake.pydecimal(right_digits=18, positive=True)),
        'codec': randint(100, 200),
        'fov_type': randint(10, 20),
        'dimension': {
            'w': 3840,
            'h': 3840
        },
        'render_resolution': {
            'w': 3840,
            'h': 3840
        }
    }
    width = 3840

    media_data = {
        "userId": user_id,
        "localMediaId": fake.uuid4(),
        "mediaId": str(randint(1000, 99999)),
        "name": fake.file_name(extension='insv'),
        "type": "pano_video",
        "shootTime": shoot_time,
        "size": size,
        "deleteStatus": delete_status,
        "createTime": create_time_ms,
        "updateTime": update_time_ms,
        "fileItems": file_items,
        "auditStatus": audit_status,
        "lastUpdatePosition": last_update_position,
        "uploadStatus": upload_status,
        "uploadTime": upload_time,
        "toolVersion": tool_version,
        "processStatus": process_status,
        "uploadFinishTime": upload_finish_time,
        "cameraType": camera_type,
        "fileInfo": file_info,
        "height": height,
        "metadata": metadata,
        "planeThumb": plane_thumb,
        "shootMode": shoot_mode,
        "tab": tab,
        "thumb": thumb,
        "version": version,
        "videoDuration": video_duration,
        "videoInfo": video_info,
        "width": width
    }

    media_collection.insert_one(media_data)

print("测试数据已插入到media集合中。")
