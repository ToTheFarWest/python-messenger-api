import uuid
class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.id = uuid.uuid4()
    self.token = uuid.uuid4()
  