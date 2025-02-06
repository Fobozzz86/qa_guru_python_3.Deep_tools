from selene import browser, be, have

def test_search_google():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_search_duckduckgo():
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('.react-results--main').should(have.text('Selene: User-Oriented Web UI Browser Tests in Python - GitHub Pages'))

def test_search_ya():
    browser.open('https://ya.ru/')
    browser.element('#text').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search-result').should(have.text(': User-oriented Web UI browser tests in Python'))
