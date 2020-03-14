from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.auth.decorators import login_required
import time

from .models import club
from .models import Post

@login_required(login_url="/accounts")
def club(request,club_name):

    driver = webdriver.Firefox(executable_path="/home/jatin/Selenium/geckodriver")

    driver.get("http://www.facebook.com")

    elem_email = driver.find_element_by_id("email")
    elem_email.send_keys("7973286902")
    elem_pass = driver.find_element_by_id("pass")
    elem_pass.send_keys("Jatin1234567890@")

    elem_email.send_keys(Keys.RETURN)
    elem_pass.send_keys(Keys.RETURN)

    # wait for sometime for the sssion to know that you have logged in then fetch the club

    element = WebDriverWait(driver,20).until(
	EC.presence_of_element_located((By.NAME,"q"))
	)

    # fetch the club url

    driver.get("https://www.facebook.com/pg/"+club_name+"/posts/")

    # the class _3ixn obscures see mroe link in facebook

    element = WebDriverWait(driver,30).until(
	EC.invisibility_of_element_located((By.CLASS_NAME,"_3ixn"))
	)
    elem_see_mores = driver.find_elements_by_class_name("see_more_link")
    for see_more in elem_see_mores:
        see_more.click()

    elem_full = driver.find_elements_by_class_name("_5pcr")

    data={}
    for elem in elem_full:
        print(elem)
        #img = elem.find_element_by_class_name("_4-eo")
        #src = img.get_attribute('src')
        #print(src)
        post = Post()
        post.content = elem.text
        #post.club_name ='Coding Club'
        post.updated_on = "jatin"
        post.save()
        tmp = elem.find_element_by_class_name("timestampContent")
        content=elem.find_element_by_class_name("_5pbx")
        print('content above\n')
        tmp2 = []
        title = content.text.split("\n")
        for tit in title:
            tmp2.append(tit)
            print(tit)
            print('\n')
        data[tmp.text]=tmp2
        print('\n\n\n')

        

    driver.close()
    return render(request, 'css_post.html', {'posts': data, 'club_name':club_name})


# Different methods of waiting in selenium
    # # invisibility_of_element_located
    # title_is
    # title_contains
    # presence_of_element_located
    # visibility_of_element_located
    # visibility_of
    # presence_of_all_elements_located
    # text_to_be_present_in_element
    # text_to_be_present_in_element_value
    # frame_to_be_available_and_switch_to_it
    # invisibility_of_element_located
    # element_to_be_clickable
    # staleness_of
    # element_to_be_selected
    # element_located_to_be_selected
    # element_selection_state_to_be
    # element_located_selection_state_to_be
    # alert_is_present

# this code piece was used for waiting before for see more links
    # element = WebDriverWait(driver,20).until(
	# EC.visibility_of_element_located((By.CLASS_NAME,"see_more_link"))
	# )

    # element = WebDriverWait(driver,30).until(
	# EC.element_to_be_clickable((By.CLASS_NAME,"see_more_link"))
	# )
    # element_to_be_clickable
    # element = WebDriverWait(driver,30)
    # continue_link = driver.find_elements_by_link_text('See More')


# This was the older code for post context retrieval then to add time stamp the new one was added
    # posts = ([])
    # elem_posts = driver.find_elements_by_class_name("_5pbx")
    # for post in elem_posts:
    #     tmp = []
    #     title = post.text.split("\n")
    #     for tit in title:
    #         tmp.append(tit)
    #     posts.append(tmp);

    # if not elem_posts:
    #     print("Nothing to show.")
