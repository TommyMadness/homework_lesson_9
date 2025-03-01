from model.pages.registration_page import RegistrationPage


def test_submit_practice_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.remove_banners()

    registration_page.fill_first_name("Sponge")
    registration_page.fill_last_name("Bob")
    registration_page.fill_email("sponge.bob@bbottom.com")
    registration_page.select_gender("Male")
    registration_page.fill_mobile_number("1234567890")
    registration_page.fill_date_of_birth(1986, 6, 15)
    registration_page.fill_subject("Biology")
    registration_page.upload_photo("kitty.jpg")
    registration_page.select_hobbies("Sports", "Music")
    registration_page.fill_current_address(
        "24 Conch Street, Bikini Bottom, Marshall Islands 96970"
    )
    registration_page.select_state("NCR")
    registration_page.select_city("Delhi")

    registration_page.submit_form()
    registration_page.should_registered_user_with(
        full_name="Sponge Bob",
        email="sponge.bob@bbottom.com",
        gender="Male",
        phone="1234567890",
        date_of_birth="15 July,1986",
        subjects="Biology",
        hobbies="Sports, Music",
        file_name="kitty.jpg",
        address="24 Conch Street, Bikini Bottom, Marshall Islands 96970",
        state="NCR",
        city="Delhi",
    )
