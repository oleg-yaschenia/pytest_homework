from selenium.webdriver.common.by import By
import time

def test_1(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    try:
        add_to_basket = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']").text
    except:
        print('\nAdd to Basket button is not found')

    assert add_to_basket in ['Добавить в корзину', 'Add to basket', 'Añadir al carrito', 'Ajouter au panier'],\
        'Add to basket is not tested language'
    time.sleep(3)






