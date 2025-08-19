from selenium.webdriver.common.by import By

class SeriesPage:

    def __init__(self, driver):
        self.driver = driver

    charge_btn = (By.XPATH, "//android.view.View[@content-desc='충전하기']")
    cookie_100 = (By.XPATH, "//android.view.View[@content-desc='100원']")
    buy_btn = (By.XPATH, "//android.widget.Button[@text='100 원 결제하기']")
    success_msg = (By.XPATH, "//android.widget.TextView[@resource-id='android:id/message']")
    done_btn = (By.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")
    home_btn = (By.XPATH, "//android.view.ViewGroup[@content-desc='홈 버튼']/android.view.ViewGroup")

    def click_charge(self):
        return self.driver.find_element(*SeriesPage.charge_btn).click()

    def click_100(self):
        return self.driver.find_element(*SeriesPage.cookie_100).click()

    def click_buy(self):
        return self.driver.find_element(*SeriesPage.buy_btn).click()

    def comp_msg(self):
        return self.driver.find_element(*SeriesPage.success_msg).text

    def click_done(self):
        return self.driver.find_element(*SeriesPage.done_btn).click()

    def click_home(self):
        return self.driver.find_element(*SeriesPage.home_btn).click()