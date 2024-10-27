import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {"owner": "vinicius_benites", "start_date": datetime(2023, 9, 3, 10, 00)}


def format_data(res):
    data = {}
    address = res["address"]

    data["id"] = res["id"]
    data["uid"] = res["uid"]
    data["first_name"] = res["first_name"]
    data["last_name"] = res["last_name"]
    data["gender"] = res["gender"]
    data["address"] = (
        f"{address['street_address']}, {address['city']}, {address['state']}, {address['country']}"
    )
    data["post_code"] = address["zip_code"]
    data["email"] = res["email"]
    data["username"] = res["username"]
    data["dob"] = res["date_of_birth"]
    data["phone"] = res["phone_number"]
    data["picture"] = res["avatar"]
    data["employment_title"] = res["employment"]["title"]
    data["employment_key_skill"] = res["employment"]["key_skill"]
    data["credit_card_number"] = res["credit_card"]["cc_number"]
    data["subscription_plan"] = res["subscription"]["plan"]
    data["subscription_status"] = res["subscription"]["status"]
    data["subscription_payment_method"] = res["subscription"]["payment_method"]
    data["subscription_term"] = res["subscription"]["term"]

    return data


def get_data():
    import requests

    res = requests.get("https://random-data-api.com/api/users/random_user")
    res = res.json()

    return res


def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=["broker:29092"], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 30:  # 1 minute
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send("users_created", json.dumps(res).encode("utf-8"))
        except Exception as e:
            logging.error(f"An error occured: {e}")
            continue


with DAG(
    "user_automation",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
) as dag:
    streaming_task = PythonOperator(
        task_id="stream_data_from_api", python_callable=stream_data
    )
