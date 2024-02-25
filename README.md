# DuckDuckGoSearchApi

DuckDuckGoSearchApi is a Python library that provides a simple and direct interface for interacting with the DuckDuckGo API. This library is designed to simplify searches and the analysis of results from DuckDuckGo.

## Instalation

To install run the following:

```python
pip install duckduckgo_search_api
```

## Available Methods

The `Duckduckgo` class offers the following main methods:

- `search(query)`: Accepts a query string and returns search results.

## Usage

Here's an example of how to use the DuckDuckGoSearchApi:

```python
from ddg import Duckduckgo

ddg_api = Duckduckgo()

results = ddg_api.search("Google")
```

## Success request

Search results are returned as a Python dictionary. Each result contains the page title, URL, and a description

```json
{
  "success": true,
  "data": [
    {
      "title": "Page Title",
      "url": "https://www.example.com",
      "description": "Short description of the page"
    },
    
  ]
}
```

## Error request

In case of an error the returned object will contain the `success` field set to `false`

```json
{
  "success": false,
  "statusCode": 404,
  "message": "Failed to fetch data"
}
```

