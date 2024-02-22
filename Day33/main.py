import requests
import json
import html
from typing import List, Any, Tuple


def generate_questions() -> List[dict]:
    response = requests.get('https://opentdb.com/api.php?amount=10&category=17')
    return response.json()["results"]


if __name__ == '__main__':
    print(generate_questions())
