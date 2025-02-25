from demo_graphic_data_util import get_user_id
import random

activities = ["Click", "Purchase"]

def generate_user_activity():
    return {
        "id": get_user_id(),
        "campaignId": random.randint(1, 20),
        "orderId": random.randint(1, 10000),
        "amount": random.randint(1, 10000),
        "units": random.randint(1, 100),
        "activity": random.choice(activities)
    }
