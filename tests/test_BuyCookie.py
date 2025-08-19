import time
import pytest

from appium.webdriver.extensions.android.nativekey import AndroidKey
from TestData.logindata import LoginData
from utilities.BaseClass import BaseClass
from PageObjects.MainPage import MainPage
from PageObjects.SeriesPage import SeriesPage

class TestBuyCookie(BaseClass):

    expect_msg = "쿠키 충전 완료되었습니다"
    expect_txt = "로그인"

    def test_login(self, get_data):
        log = self.get_log()

        main_page = MainPage(self.driver)

        main_page.run_app()
        main_page.click_menu()
        main_page.click_txt()
        # 앱 실행 후 로그인 진입

        main_page.get_id().send_keys(get_data["ID"])
        main_page.get_pw().send_keys(get_data["PW"])
        # 로그인 정보 입력

        main_page.click_login()
        main_page.click_close()
        # 네이버 메인 진입

        assert main_page.get_box().is_displayed()
        log.info("로그인 성공")
        # 검색창 확인

        main_page.click_menu()
        main_page.click_series()
        # 네이버 시리즈 진입

    def test_buy_cookie(self):
        log = self.get_log()

        series_page = SeriesPage(self.driver)

        series_page.click_charge()
        series_page.click_100()
        # 결제 화면 진입

        series_page.click_buy()
        time.sleep(10)
        # 보안 키패드 수동 입력

        assert series_page.comp_msg() == self.expect_msg
        log.info("결제 성공")
        # 결제 완료 팝업 확인

        series_page.click_done()
        series_page.click_home()
        # 팝업 닫은 후 네이버 메인 진입

    def test_logout(self):
        log = self.get_log()

        main_page = MainPage(self.driver)

        main_page.click_menu()
        main_page.click_option()
        # 설정 페이지 진입

        main_page.click_manage()
        main_page.click_dot()
        main_page.click_delete()
        main_page.click_remove()
        # 간편 아이디 삭제

        self.driver.press_keycode(AndroidKey.BACK)
        # 백키 탭

        assert main_page.get_txt() == self.expect_txt
        log.info("로그아웃 성공")
        # 로그인 문구 확인

        self.driver.terminate_app("com.nhn.android.search")
        # 앱 종료

    @pytest.fixture(params=LoginData.get_test_data("1"))
    def get_data(self, request):
        return request.param
        # 엑셀 데이터 받기