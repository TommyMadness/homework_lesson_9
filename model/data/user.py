from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone: str
    date_of_birth: date
    subject: str
    hobbies: List[Hobby]
    picture: str
    address: str
    state: str
    city: str
