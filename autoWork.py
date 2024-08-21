from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Open the browser
driver = webdriver.Chrome()
# Navigate to the website
driver.get('https://www.example.com')
sleep(2)
# Find the search input field and enter 'Python'
search_input = driver.find_element(By.NAME, 'q')
search_input.send_keys('Python')
sleep(2)
# Click the search button
search_button = driver.find_element(By.NAME, 'btnK')
search_button.click()
sleep(2)
# Print the number of search results
results = driver.find_elements(By.CSS_SELECTOR, '.g:not(.g-hidden)')
print(f'Number of search results: {len(results)}')
# Close the browser
driver.quit()
# простой синтаксис для автоматизации некоторых процесов 
# так же в selenium можно использовать логику типа так 

# Open the browser
driver = webdriver.Chrome()
# Navigate to the website
driver.get('https://www.example.com')
# Slow the website for looking what it is doing
sleep(2)
# Use the while for do the infinity work
while True:
    # Find the search input field and enter 'Python'
    search_input = driver.find_element(By.link, 'Something') # Use the link by name
    # Wait when the program find the element
    sleep(1)
    # Click the link
    search_input.click()
    # Find the search input field and enter 'Python'
    search_button = driver.find_element(By.link, 'Something_2') # Use by name
    # Wait when the program find the element
    sleep(1)
    search_button.click()

# And wait when the wesite should close
sleep(5)
# After the wait close the browser
driver.quit()