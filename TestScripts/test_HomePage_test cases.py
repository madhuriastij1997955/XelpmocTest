import time

from PageObjects.Auto_Home import Home
class Test_Home:


    def test_verify_application_title(self):
        home_p=Home(self.driver)
        home_p.verify_app_title()

    def test_verify_alert_messages(self):
        home_p = Home(self.driver)
        home_p.alert_popup()

    def test_verify_tooltip_message(self):
        home_p = Home(self.driver)
        home_p.get_tooltip_msg()

    def test_verify_capturing_photo(self):
        home_p = Home(self.driver)
        home_p.capture_img()

    def test_double_click_btn(self):
        home_p = Home(self.driver)
        home_p.click_double()

    def test_drag_drop_pizza(self):
        home_p = Home(self.driver)
        home_p.drag_drop_piza()

    def test_sample_login_valid_creditionals(self):
        home_p = Home(self.driver)
        home_p.sample_login()


    def test_sample_login_Invalid_creditionals(self):
        home_p = Home(self.driver)
        home_p.invalid_login()

    def test_fill_form(self):
        home_p = Home(self.driver)
        home_p.fill_form("madhuri","jasti","this is automation testing with selenium")

    def test_print_webtable_details(self):
        home_p = Home(self.driver)
        home_p.sample_web_table_details()

    def test_navigate_to_contat_page(self):
        home_p = Home(self.driver)
        home_p.navigate_to_contact_page()







