import time
from selenium.webdriver.common.by import By

def test_add_to_cart_button_exists(browser):
    """Проверка наличия кнопки добавления товара в корзину"""
    # Открываем страницу товара
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)
    
    # Добавляем задержку для визуальной проверки языка страницы
    time.sleep(30)
    
    # Находим кнопку добавления в корзину
    add_to_cart_button = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    # Проверяем, что кнопка существует на странице
    assert len(add_to_cart_button) > 0, "Кнопка добавления в корзину отсутствует на странице товара"
    
    # Дополнительно можно вывести текст кнопки для проверки
    print(f"Текст кнопки: {add_to_cart_button[0].text}")
