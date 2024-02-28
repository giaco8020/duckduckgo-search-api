import requests
from bs4 import BeautifulSoup
import random


class Duckduckgo:

    def __init__(self):
        self.endpoint = 'https://html.duckduckgo.com/html/'
        self.user_agents = self.__load_user_agents("user-agents.txt")

    def __load_user_agents(self, file_path):
        with open(file_path, 'r') as file:
            user_agents = [line.strip() for line in file if line.strip()]
        return user_agents

    def __get_random_user_agent(self):
        if not self.user_agents:
            raise ValueError("La lista degli User-Agent è vuota.")
        return random.choice(self.user_agents)

    def __parse_response(self, response):
        soup = BeautifulSoup(response, 'html.parser')
        results = soup.find_all("div", class_="result")
        parsed_results = []
        for result in results:
            title = result.find("h2", class_="result__title").get_text(strip=True)
            url = result.find("a", class_="result__a")['href']
            description = result.find("a", class_="result__snippet")
            description = description.get_text(strip=True) if description else "No description available"
            parsed_results.append({"title": title, "url": url, "description": description})
        return {"success": True, "data": parsed_results}

    def search(self, query):
        user_agent = self.__get_random_user_agent()
        headers = {
            'Cache-Control': 'no-cache',
            'Content-Length': '11',
            'Origin': 'https://html.duckduckgo.com',
            'Pragma': 'no-cache',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }
        params = {'q': query, "b": ""}
        try:
            response = requests.post(self.endpoint, data=params, headers=headers)
            response.raise_for_status()
            return self.__parse_response(response.content)
        except requests.exceptions.RequestException as e:
            return {"success": False, "statusCode": e.response.status_code if e.response else None,
                    "message": f"Error making request: {e}"}
        except Exception as e:
            return {"success": False, "statusCode": None, "message": f"Error parsing response: {e}"}

