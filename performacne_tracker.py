import random

def get_video_stats():

    stats = {
        "views": random.randint(1000,10000),
        "likes": random.randint(100,1000),
        "orders": random.randint(1,50)
    }

    return stats
