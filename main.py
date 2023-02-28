from jira import JIRA
import matplotlib.pyplot as plt
import json
from datetime import date
import time


def save_data():
    with open('credentials.json', 'r') as c:
        credentials = json.load(c)

    jira = JIRA(server=credentials["serverUrl"], basic_auth=(
        credentials["email"], credentials["OAuthToken"]))

    cards = jira.search_issues(
        f'project = "{credentials["ProjectName"]}" AND sprint in openSprints()')

    estados = {}

    for card in cards:
        estado_card = card.fields.status.name  # type: ignore

        if estado_card in estados:
            estados[estado_card] += 1
        else:
            estados[estado_card] = 1

    dict_estados = json.dumps(estados)

    with open('data.json', 'r') as f:
        data = json.load(f)

    new_line = {str(date.today()): dict_estados}
    data["data"].append(new_line)

    with open('data.json', 'w') as f:
        json.dump(data, f)


today = date.today()

while True:
    ONE_DAY_IN_SECONDS = 24 * 60 * 60

    save_data()
    time.sleep(ONE_DAY_IN_SECONDS)
