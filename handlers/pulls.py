import requests
LOGIN = ""
PASSWORD = ""
URI_PARAMS = {'per_page': '100', 'state': 'all'}
URL = 'https://api.github.com/repos/alenaPy/devops_lab/pulls'


def get_pulls(state):
    json = get_json()
    if state == "open" or state == "closed":
        return parse_json_state(state, json)
    elif state == "accepted" or state == "needs work":
        return parse_json_label(state, json)
    else:
        return parse_json(json)


def get_json():
    get = requests.get(URL, params=URI_PARAMS, auth=(LOGIN, PASSWORD))
    response = get.json()
    return response


def parse_json(json):
    output_json = []
    for x in json:
        output_json.append(
            {'num': x['number'], 'link': x['html_url'], 'title': x['title']})
    return output_json


def parse_json_state(state, json):
    output_json = []
    if state == "open" or state == "closed":
        for x in json:
            if x['state'] == state:
                output_json.append(
                    {'num': x['number'], 'link': x['html_url'], 'title': x['title']})
    return output_json


def parse_json_label(state, json):
    output_json = []
    if state == "accepted" or state == "needs work":
        for x in json:
            if x['labels'] == []:
                continue
            else:
                if x['labels'][0]['name'] == state:
                    output_json.append(
                        {'num': x['number'], 'link': x['html_url'], 'title': x['title']})
    return output_json
