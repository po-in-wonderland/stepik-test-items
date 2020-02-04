def test_should_be_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    button = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert button > 0, 'Элемент по данному селектору отсутсвует'
