from datetime import datetime
from typing import Dict

INDEX_ENDPOINT = "https://beta-api.crunchyroll.com/index/v2"
PROFILE_ENDPOINT = "https://beta-api.crunchyroll.com/accounts/v1/me/profile"
TOKEN_ENDPOINT = "https://beta-api.crunchyroll.com/auth/v1/token"
SEARCH_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/search"
STREAMS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/videos/{}/streams"
SERIES_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/series/{}"
SEASONS_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/seasons"
EPISODES_ENDPOINT = "https://beta-api.crunchyroll.com/cms/v2{}/episodes"
SIMILAR_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/{}/similar_to"
NEWSFEED_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/news_feed"
BROWSE_ENDPOINT = "https://beta-api.crunchyroll.com/content/v1/browse"
AUTHORIZATION = "Basic aHJobzlxM2F3dnNrMjJ1LXRzNWE6cHROOURteXRBU2Z6QjZvbXVsSzh6cUxzYTczVE1TY1k="

def fixup(d: Dict):
    if '' in d:
        d["raw"] = d[""]
        d.pop("")
    for v in d.values():
        if isinstance(v, dict):
            fixup(v)

def get_date() -> datetime: 
    now = datetime.utcnow()
    return datetime.strptime(
        "{}-{}-{}T{}:{}:{}Z".format(
            now.year, now.month,
            now.day, now.hour,
            now.minute, now.second
        ),
        "%Y-%m-%dT%H:%M:%SZ"
    )

def str_to_date(string: str) -> datetime: 
    return datetime.strptime(
        string,
        "%Y-%m-%dT%H:%M:%SZ"
    )