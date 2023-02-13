try:
    import os
    import json
    import boto3
    import requests
    import datetime
    from datetime import datetime
    import time
    import logging
    import random
    from time import sleep
    import uuid
    from dotenv import load_dotenv
    load_dotenv(".env")
except Exception as e:
    print("Error****".format(e))


class Secrets:
    def __init__(self):
        self.AWS_ACCESS_KEY = os.getenv("DEV_ACCESS_KEY")
        self.AWS_SECRET_KEY = os.getenv("DEV_SECRET_KEY")
        self.AWS_REGION_NAME = os.getenv("DEV_AWS_REGION_NAME")
        self.EventBusName = os.getenv("DEV_AWS_EVENT_BUS_NAME_JOB")


class AWSEventBus(Secrets):
    """Helper class to which add functionality on top of boto3 """

    def __init__(self, **kwargs):
        Secrets.__init__(
            self
        )
        self.client = boto3.client(
            "events",
            aws_access_key_id=self.AWS_ACCESS_KEY,
            aws_secret_access_key=self.AWS_SECRET_KEY,
            region_name=self.AWS_REGION_NAME,
        )

    def send_events(self, json_message, DetailType, Source):
        response = self.client.put_events(
            Entries=[
                {
                    'Time': datetime.now(),
                    'Source': Source,
                    'Resources': [],
                    'DetailType': DetailType,
                    'Detail': json.dumps(json_message),
                    'EventBusName': self.EventBusName,
                },
            ]
        )
        return response


class OrderGenerator(object):
    @staticmethod
    def get():
        return {
            "orderid": uuid.uuid4().__str__(),
            "customer_id": uuid.uuid4().__str__(),
            "ts": datetime.now().isoformat().__str__(),
            "order_value": random.randint(10, 1000).__str__(),
            "priority": random.choice(["LOW", "MEDIUM", "URGENT"])
        }


def main():
    helper = AWSEventBus()
    for i in range(1,200):
        message = OrderGenerator.get()
        res = helper.send_events(json_message=message, Source='order', DetailType='order')
        print(res)


main()
