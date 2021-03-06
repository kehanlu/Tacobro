from models.model import model
from datetime import datetime


class Post(model):

    def __init__(self, content, author, board, like_count=0, dislike_count=0, publish_date=datetime.now(), last_modify=datetime.now()):
        self.content = content
        self.publish_date = publish_date
        self.last_modify = last_modify
        self.like_count = like_count
        self.dislike_count = dislike_count
        self.author = author
        self.board = board
