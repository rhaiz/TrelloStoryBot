import requests
import json
from env_variables import TRELLO_API_KEY, TRELLO_API_TOKEN, TRELLO_BOARD_ID

class Trello:

    def __init__(self):
        self.key = TRELLO_API_KEY
        self.token = TRELLO_API_TOKEN
        self.board = TRELLO_BOARD_ID

    def getBoards(self):
        url = f'https://api.trello.com/1/members/me/boards?key={self.key}&token={self.token}'
        response = requests.get(url)
        boards = response.json()
        for board in boards:
            print(board['name'])
    
    def createCard(self, name, desc, list_id):
        url = f'https://api.trello.com/1/cards?key={self.key}&token={self.token}&name={name}&desc={desc}&idList={list_id}'
        response = requests.post(url)
        card = response.json()
        print(card)

    def getCards(self):
        url = f'https://api.trello.com/1/boards/{self.board}/cards?key={self.key}&token={self.token}'
        response = requests.get(url)
        cards = response.json()
        for card in cards:
            print(card['name'])