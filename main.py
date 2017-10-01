import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/home/maciek/projects/vat/chromedriver')
driver.get('http://www.finanse.mf.gov.pl/web/wp/pp/sprawdzanie-statusu-podmiotu-w-vat')
print('done!')
try:
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.ID, "b-7"))
    )

    text_field = driver.find_element_by_id("b-7")
    send_button = driver.find_element_by_id("b-8")

    text_field.send_keys('5993104943234237')
    send_button.click()
    ok_msg = '''Podmiot o podanym identyfikatorze podatkowym NIP jest zarejestrowany jako podatnik VAT czynny'''

    while True:
        time.sleep(1)
        element = driver.find_element_by_id('caption2_b-3')
        if len(element.text):
            result_text = element.text
            break

    if result_text.find(ok_msg) != -1:
        print('OK!')
    else:
        print('BAD!')


finally:
    driver.quit()
