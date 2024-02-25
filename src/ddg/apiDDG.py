import requests
from bs4 import BeautifulSoup


class Duckduckgo:

    def __init__(self):
        self.endpoint = 'https://html.duckduckgo.com/html/'
        self.headers = {
            'Cache-Control': 'no-cache',
            'Content-Length': '11',
            'Origin': 'https://html.duckduckgo.com',
            'Pragma': 'no-cache',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        }

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
        params = {'q': query, "b": ""}
        try:
            response = requests.post(self.endpoint, data=params, headers=self.headers)
            response.raise_for_status()  # This will raise an HTTPError if the status is 4xx, 5xx
            return self.__parse_response(response.content)
        except requests.exceptions.RequestException as e:
            return {"success": False, "statusCode": e.response.status_code if e.response else None,
                    "message": f"Error making request: {e}"}
        except Exception as e:
            return {"success": False, "statusCode": None, "message": f"Error parsing response: {e}"}

