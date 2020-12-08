from pageObject.GLCareersPage import GLCareersPage
from pageObject.GLCareersResultPage import GLCareersResultPage
from pageObject.config.config import Config

def test_search(browser):
    main_page = GLCareersPage(browser)
    main_page.go_to_site()
    main_page.click_on_the_cookies_allow_button()
    main_page.check_word()
    main_page.enter_word(Config.DATA_FOR_ENTER_WORLD)
    main_page.click_on_the_search_button()
    assert Config.DATA_FOR_CHECK_WORDS in browser.page_source
    result_page = GLCareersResultPage(browser)
    result_page.get_first_result()