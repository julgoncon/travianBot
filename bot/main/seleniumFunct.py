# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import re
import urllib.request
import sqlite3 
import os
import socket
import urllib
from selenium.webdriver.chrome.options import Options
import time 
import basedatos as bd
import random
import time
import re
from selenium.webdriver.common.keys import Keys


aldea=2
def public_ip():
	lista = "0123456789."
	ip=""
	dato=urllib.request.urlopen("http://checkip.dyndns.org").read()
	for x in str(dato):
		if x in lista:
			ip += x
	return ip



def login(cuenta):
    if cuenta=='unicornioazul':
        pwd="blueunicorn"
    if cuenta=='gothem':
        pwd="gothem1997"
    if cuenta=='swishbish':
        pwd="gama1997"
    global driver
    driver = webdriver.Chrome(r"C:\Users\julia\Desktop\test\socio\drivers\chromedriver.exe")
    driver.implicitly_wait(2)
    #driver.minimize_window()
    driver.get("https://tx3.travian.pl/login.php")
    driver.find_element_by_name("name").click()
    time.sleep(random.random()*random.randrange(1,3))
    driver.find_element_by_name("name").clear()
    time.sleep(random.random()*random.randrange(1,3))
    driver.find_element_by_name("name").send_keys(cuenta)
    time.sleep(random.random()*random.randrange(1,3))
    driver.find_element_by_name("password").clear()
    time.sleep(random.random()*random.randrange(1,3))
    driver.find_element_by_name("password").send_keys(pwd)
    time.sleep(random.random()*random.randrange(2,4))
    driver.find_element_by_id("s1").click()
    if aldea==2:
        driver.find_element_by_xpath("//div[@id='sidebarBoxVillagelist']/div[2]/ul/li[2]/a/span").click()
    else:
        driver.find_element_by_xpath("//div[@id='sidebarBoxVillagelist']/div[2]/ul/li/a").click()
    
def closeDriver():
    driver.close()

def nivelCasillas():
    elements=driver.find_elements_by_xpath("//div[contains(@class, 'level')]")
    levels=[]
    for e in elements:
        if e.text=='':
            levels.append(0)
        else:
            levels.append(int(e.text))
    return levels

def recursosDisponibles():
    elements=driver.find_elements_by_xpath("//div[@class='capacity']/div")
    array2=[]
    for e in elements:
        array2.append(e.text)
    newkeys=[key.strip('\u202c') for key in array2]
    newkeys1=[key.strip('\u202d') for key in newkeys]
    array1=[
    driver.find_element_by_xpath("//div[@id='l1']").text,
    driver.find_element_by_xpath("//div[@id='l2']").text,
    driver.find_element_by_xpath("//div[@id='l3']").text,
    driver.find_element_by_xpath("//div[@id='l4']").text
    ]
    newArray=[]
    for e in array1:
        e=e.replace(' ','')
        newArray.append(e)
    newkeys10=[key.strip('\u202c') for key in newArray]
    newkeys11=[key.strip('\u202d') for key in newkeys10]
    newkeys12=[]
    for key in newkeys11:
        newkeys12.append(int(key))
    newkeys12.append(newkeys1)
    return newkeys12
    
def produccion():
    driver.find_element_by_xpath("//div[@id='navigation']/a").click()
    elements=driver.find_elements_by_xpath("//td[@class='num']")
    
    array1=[]
    for e in elements:
        array1.append(e.text)
    
    newkeys=[key.strip('\u202c') for key in array1]
    newkeys1=[key.strip('\u202d') for key in newkeys]
    if aldea!=2:
        newkeys1.pop()
    return newkeys1


def casillasASubir():

    levels=nivelCasillas()
    maxi=max(levels)
    mini=min(levels)
    diff=maxi-mini
    
    levelsDiff=[]
    for i in range(len(levels)):
        levelsDiff.append(maxi-levels[i])
    sample=[]
    for i in range(len(levelsDiff)):
        if levelsDiff[i]==diff:
            sample.append(i)
    random.shuffle(sample)
    return sample

def subirRecursos(lista,start_time):
    levels=nivelCasillas()
    recursosdisponibles=recursosDisponibles()
    print(lista)
    for i in range(len(lista)):
        print(i)
        print(levels[lista[i]],lista[i])
        coste=bd.getCoste(levels[lista[i]],lista[i])
        entrarbucle=True
        while(entrarbucle):
            current_time=time.time()
            if current_time-start_time>=random.randrange(70,100):
                print(current_time-start_time)
                return print('CAMBIO: Se han cumplido los 7 min')
            #comprobacion si hay recursos para construir
            if coste[0]-recursosdisponibles[0]<0 and coste[1]-recursosdisponibles[1]<0 and coste[2]-recursosdisponibles[2]<0 and coste[3]-recursosdisponibles[3]<0:               
                time.sleep(random.random()*random.randrange(0,5))
                driver.find_element_by_xpath("//div[@id='navigation']/a").click()
                driver.find_element_by_xpath("//div[@onclick=\"window.location.href='build.php?id="+str(lista[i]+1)+"'\"]").click()
                try:
                    #construimos si no hay construcciones 
                    time.sleep(random.random()*random.randrange(0,5))
                    driver.find_element_by_xpath("//button[@class='textButtonV1 green build']").click()
                    time.sleep(random.random()*random.randrange(0,2))
                    driver.find_element_by_xpath("//div[@id='navigation']/a").click()
                    entrarbucle=False
                    
                except:
                    time.sleep(random.random()*random.randrange(0,2))
                    driver.find_element_by_xpath("//div[@id='navigation']/a").click()
                    time.sleep(random.random()*random.randrange(10,20))
                    
            else:
                driver.find_element_by_xpath("//div[@id='navigation']/a").click()
                print('going to sleep')
                time.sleep(random.random()*random.randrange(10,20))
                print('ya ma hartao')
                entrarbucle=False

def construirEdificio(edificioID,lugarID):
    time.sleep(random.random()*random.randrange(0,2))
    driver.find_element_by_xpath("//div[@id='navigation']/a[2]").click()
    time.sleep(random.random()*random.randrange(0,2))
    driver.find_element_by_css_selector("div.buildingSlot.a"+str(lugarID)+".g0.aid"+str(lugarID)+".roman > svg.buildingShape.iso > g.hoverShape > path").click()
    try:
        time.sleep(random.random()*random.randrange(0,2))    
        div4=driver.find_element_by_xpath("//div[@id='contract_building23']/div[4]/button").click()
    except:
        pass
    time.sleep(random.random()*random.randrange(0,2))
    driver.find_element_by_xpath("//div[@id='navigation']/a[2]").click()
    
def subirEdificio(edificioID):
    time.sleep(random.random()*random.randrange(0,2))
    driver.find_element_by_xpath("//div[@id='navigation']/a[2]").click()
    time.sleep(random.random()*random.randrange(0,2))
    driver.find_element_by_css_selector("svg.buildingShape.g"+str(edificioID)+" > g.hoverShape > path").click()
    try:
        time.sleep(random.random()*random.randrange(0,2))
        driver.find_element_by_xpath("//div[@class='section1']/button").click()
    except:
        pass
    time.sleep(random.random()*random.randrange(0,2))
    driver.find_element_by_xpath("//div[@id='navigation']/a[2]").click()

def tirarVacas():
    driver.find_element_by_xpath("//div[@id='sidebarBoxLinklist']/div[2]/ul/li/a/span").click()
    time.sleep(random.random()*random.randrange(4,5))
    driver.find_element_by_xpath("//div[@id='list539']/form/div[2]/div/div/label").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//div[@id='navigation']/a").click()

def ataque():
    elements=driver.find_elements_by_xpath("//li[contains(@class, 'attack')]")
    return len(elements)


def salirDriver():
    driver.close()