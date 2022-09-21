def func1(function, *args):
    print('Function name:', (' '.join(function.__name__.split('_'))).capitalize())
    print("Args:", ', '.join(args))


def open_browser(browser_name):
    func1(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func1(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func1(find_registration_button_on_login_page, page_url, button_text)


open_browser('Browser#1')
go_to_companyname_homepage('https://valid.url.com')
find_registration_button_on_login_page('https://valid.url.com', 'Text#1')
