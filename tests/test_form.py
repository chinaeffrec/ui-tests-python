from pages.form_page import FormPage

def test_form_positive(driver):
    page = FormPage(driver)

    alert_text = (
        page.open_page()
        .enter_name("John Connor")
        .enter_password("12345")
        .select_drinks()
        .select_color()
        .select_automation()
        .enter_email("mail@mail.com")
        .enter_message()
        .submit()
        .get_alert_text()
    )

    assert alert_text == "Message received!"


def test_form_negative_invalid_email(driver):
    page = FormPage(driver)

    alert_text = (
        page.open_page()
        .enter_name("Frodo Baggins")
        .enter_password("12345")
        .select_drinks()
        .select_color()
        .select_automation()
        .enter_email("invalid-email")
        .enter_message()
        .submit()
        .get_alert_text()
    )

    assert alert_text == "Invalid email!"
