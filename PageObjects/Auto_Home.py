import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Utilitis.BaseClass import BaseClass


class Home(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    title_homepage = (By.TAG_NAME, 'h1')
    alert_btn = (By.XPATH, "(//button)[1]")
    alert_ok_msg = (By.XPATH, "//p[text()='You Pressed the OK Button!']")
    alert_cancel_msg = (By.XPATH, "//p[text()='You pressed the Cancel Button!']")
    tool_tip_ele=(By.XPATH,"//div[@class='tooltip']")
    tool_tip_msg=(By.XPATH,"//span[text()='This is your sample Tooltip text']")
    sample_img=(By.XPATH,"//div[text()='Image']")
    sample_des=(By.XPATH,"//p[contains(text(),'This is your description of the photo')]")
    double_click_btn=(By.XPATH,"//button[text()='Double-click me']")
    double_click_txt=(By.XPATH,"//p[text()='Your Sample Double Click worked!']")
    target_ele=(By.ID,"div1")
    src_ele=(By.ID,"drag1")
    username_txt=(By.ID,"uname")
    pwd_txt=(By.ID,"pwd")
    login_btn=(By.XPATH,"//input[@value='Login']")
    login_sucess_msg=(By.TAG_NAME,"h2")
    # Form
    firstname_txt=(By.ID,"fname")
    lastname_txt=(By.ID,"lname")
    female_radio_btn=(By.ID,"female")
    single_dropdown=(By.XPATH,"//select[@id='option']")
    drop1_value=(By.XPATH,"(//option[@value='option 1'])[2]")
    mul_dropdown=(By.XPATH,"//select[@id='owc']")
    op1=(By.XPATH,"//option[text()='Option 1']")
    op2=(By.XPATH,"//option[text()='Option 2']")
    checkbox1=(By.XPATH,"//input[@name='option1']")
    checkbox2 = (By.XPATH, "//input[@name='option2']")
    checkbox3 = (By.XPATH, "//input[@name='option3']")
    automically_txt=(By.XPATH,"//input[@list='datalists']")
    mint_opt=(By.XPATH,"//option[@value='Mint']")
    select_date=(By.ID,"day")
    scrollrange=(By.ID,"a")
    choose_file=(By.ID,"myfile")
    qunaty_box=(By.NAME,"quantity")
    textarea_box=(By.XPATH,"//textarea[@name='message']")
    submit_btn=(By.XPATH,"//button[text()=' Submit']")

    # web table
    rows_count=(By.XPATH,"//tbody/tr[not(position()=1)]")
    cols_count=(By.XPATH,"(//tr)[1]/th")

    contact_mod=(By.XPATH,"//a[text()='Contact']")
    contact_msg=(By.TAG_NAME,"h2")

    def verify_app_title(self):
        title = self.return_text(self.title_homepage)
        assert title == "Your Website to practice Automation Testing"
        print("app title is verified")

    def alert_popup(self):
        self.javascripit_click(self.alert_btn)
        self.driver.switch_to.alert.accept()
        ale_ok = self.return_text(self.alert_ok_msg)
        assert ale_ok == "You Pressed the OK Button!"
        self.javascripit_click(self.alert_btn)
        self.driver.switch_to.alert.dismiss()
        ale_can = self.return_text(self.alert_cancel_msg)
        assert ale_can == "You pressed the Cancel Button!"
        print("alert messages are verified")

    def get_tooltip_msg(self):
        self.move_to_element(self.tool_tip_ele)
        self.move_to_element(self.tool_tip_msg)
        tootip_msg=self.return_text(self.tool_tip_msg)
        assert tootip_msg=="This is your sample Tooltip text"
        print("tootip messages are verified")

    def capture_img(self):
        txt=self.return_text(self.sample_img)
        assert txt=="Image"
        assert self.return_text(self.sample_des)=="This is your description of the photo"
        print("image is captured")

    def click_double(self):
        self.double_click(self.double_click_btn)
        txt=self.return_text(self.double_click_txt)
        assert txt=="Your Sample Double Click worked!"
        print("double clicked btn is verfied")

    def drag_drop_piza(self):
        self.drag_and_drop(self.src_ele,self.target_ele)

    def sample_login(self):
        self.send_keys(self.username_txt,"test")
        self.send_keys(self.pwd_txt, "test")
        self.click_element(self.login_btn)
        time.sleep(1.0)
        msg=self.return_text(self.login_sucess_msg)
        print(msg)

    def invalid_login(self):
        self.send_keys(self.username_txt, "test")
        self.send_keys(self.pwd_txt, "test123")
        self.click_element(self.login_btn)
        time.sleep(1.0)
        self.driver.switch_to.alert.accept()

    def fill_form(self,fname,lname,msg):
        self.send_keys(self.firstname_txt,fname)
        self.send_keys(self.lastname_txt,lname)
        self.click_element(self.female_radio_btn)
        self.click_element(self.single_dropdown)
        time.sleep(0.9)
        self.move_to_element(self.drop1_value)
        self.click_element(self.drop1_value)
        self.click_element(self.mul_dropdown)
        self.click_element(self.op1)
        self.click_element(self.op2)
        self.click_element(self.checkbox1)
        self.click_element(self.checkbox2)
        self.click_element(self.checkbox3)
        self.click_element(self.automically_txt)
        self.send_keys(self.automically_txt,"Mint")
        self.move_by_offset(self.scrollrange)
        self.send_keys(self.select_date,"08-08-1997")
        self.click_element(self.qunaty_box)
        self.send_keys(self.textarea_box,msg)
        self.click_element(self.submit_btn)


    def sample_web_table_details(self):
        rows=self.get_webtable_rows(self.rows_count)
        cols=self.get_webtable_rows(self.cols_count)
        for row in range(1,rows+1):
            for col in range(1,cols+1):
                xpath="((//tbody/tr)["+str(row)+"]/td)["+str(col)+"]"

                cell_txt=self.return_text((By.XPATH,xpath))
                print(cell_txt, "  ")

        print()

    def navigate_to_contact_page(self):
        self.click_element(self.contact_mod)
        msg=self.return_text(self.contact_msg)
        print(msg)




