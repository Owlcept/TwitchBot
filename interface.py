import requests
from config import *

class TwitchInterface:
    """Interfaces with twitch API. Use this to call for a list of team members
    at the start of streams."""

    def __init__(self):
        """Set up the instance with the credentials and settings we need to
        access info via twitch's API"""
        self.base_url = "https://api.twitch.tv"
        self.header = {
            'Accept' : "application/vnd.twitchtv.v5+json",
            'Client-ID' : CLIENT_ID
        }
        #self.team_members = self._get_team_members()
        self.greeted_subs = list()

    def request(self, method, url, params=None, limit=None, version='kraken'):
        if method is 'GET':
            r = requests.get(f"{self.base_url}/{version}/{url}", headers=self.header)
            return r.json()

    """
    def _get_team_members(self):
        'requests a list of team members (in lower) every time the bot starts'
        members = list()
        data = self.request(method='GET', url=f"teams/{os.environ['TEAM']}")
        for user in data['users']:
            members.append(user['name'])
        return members

    def _set_team_members(self):
        self.team_members = []
        self.team_members = self._get_team_members()
    """
    def reset_shoutouts(self):
        self.greeted_subs = []

    def mark_as_greeted(self, user):
        self.greeted_subs.append(user)


twitch_api = TwitchInterface()