import requests
from fake_useragent import UserAgent
ua = UserAgent()
def get_projects():

    try:
        headers = {
            "user-agent": ua.random,
        }
        url = "https://studlance.ru/"
        body = {
            "price": [
                100,
                85000
            ],
            "priceUndefined": True,
            "publicationDateFrom": "01.01.2011",
            "publicationDateTo": "31.12.2020",
            "urgent": False,
            "pro": False,
            "verified": False,
            "bidLimit": False,
            "userSpecializationsState": True,
            "userSpecializations": False,
            "domains": [
                3
            ],
            "sciences": [],
            "subjects": [],
            "page": 0
        }

        response = requests.post(url, json=body, headers=headers)
        return True, response.json()["value"]
    except Exception as e:
        return False, f"Error, {e}"

print(get_projects())