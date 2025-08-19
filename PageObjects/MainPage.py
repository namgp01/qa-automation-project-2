from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver

    app_icon = (By.XPATH, "//android.widget.TextView[@content-desc='NAVER']")
    menu_icon = (By.XPATH, "//android.widget.ImageView[@content-desc='메뉴']")
    login_txt = (By.XPATH, "//android.widget.TextView[@resource-id='com.nhn.android.search:id/titleLeftTextView']")
    input_id = (By.XPATH, "//android.widget.AutoCompleteTextView[@content-desc='아이디']")
    input_pw = (By.XPATH, "//android.widget.AutoCompleteTextView[@content-desc='비밀번호 입력']")
    login_btn = (By.XPATH, "//android.widget.Button[@content-desc='로그인']")
    close_btn = (By.XPATH, "//android.widget.ImageView[@content-desc='확장 메뉴 닫기']")
    search_box = (By.XPATH, "//android.view.View[@resource-id='com.nhn.android.search:id/searchBarContainer']")
    series_btn = (By.XPATH, "(//android.widget.ImageView[@resource-id='com.nhn.android.search:id/favIconBorder'])[8]")
    option_btn = (By.XPATH, "//android.widget.ImageView[@content-desc='설정']")
    manage_id = (By.XPATH, "//android.widget.TextView[@resource-id='com.nhn.android.search.Setup:id/titleTitle' and @text='로그인 아이디 관리']")
    dot_btn = (By.XPATH, "//android.widget.ImageView[@resource-id='com.nhn.android.search:id/menu']")
    delete_btn = (By.XPATH, "//android.widget.TextView[@text='이 기기에서 사용 안 함']")
    remove_btn = (By.XPATH, "//android.widget.Button[@content-desc='해제하기']")

    def run_app(self):
        return self.driver.find_element(*MainPage.app_icon).click()

    def click_menu(self):
        return self.driver.find_element(*MainPage.menu_icon).click()

    def click_txt(self):
        return self.driver.find_element(*MainPage.login_txt).click()

    def get_id(self):
        return self.driver.find_element(*MainPage.input_id)

    def get_pw(self):
        return self.driver.find_element(*MainPage.input_pw)

    def click_login(self):
        return self.driver.find_element(*MainPage.login_btn).click()

    def click_close(self):
        return self.driver.find_element(*MainPage.close_btn).click()

    def get_box(self):
        return self.driver.find_element(*MainPage.search_box)

    def click_series(self):
        return self.driver.find_element(*MainPage.series_btn).click()

    def click_option(self):
        return self.driver.find_element(*MainPage.option_btn).click()

    def click_manage(self):
        return self.driver.find_element(*MainPage.manage_id).click()

    def click_dot(self):
        return self.driver.find_element(*MainPage.dot_btn).click()

    def click_delete(self):
        return self.driver.find_element(*MainPage.delete_btn).click()

    def click_remove(self):
        return self.driver.find_element(*MainPage.remove_btn).click()

    def get_txt(self):
        return self.driver.find_element(*MainPage.login_txt).text