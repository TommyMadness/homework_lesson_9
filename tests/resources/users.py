from datetime import date

from model.data.user import User, Hobby

student = User(
    first_name="Sponge",
    last_name="Bob",
    email="sponge.bob@bbottom.com",
    gender="Male",
    phone="1234567890",
    date_of_birth=date(1986, 7, 15),
    subject="Biology",
    hobbies=[Hobby.SPORTS, Hobby.MUSIC],
    picture="kitty.jpg",
    address="24 Conch Street, Bikini Bottom, Marshall Islands 96970",
    state="NCR",
    city="Delhi",
)
