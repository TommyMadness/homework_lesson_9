from model.pages.registration_page import RegistrationPage
from tests.resources import users


def test_submit_practice_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(users.student)
    registration_page.should_have_registered(users.student)
