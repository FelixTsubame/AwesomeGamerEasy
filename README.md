# AGE
Previous plan review:
this project will compare the prize of the game that the user wants to buy on
several online store (Steam and Amazon), then, telling the user which one is the
cheapest one. Furthermore, if the user wants to know about the game, the project
can show the user the details of the game, including age rating, hardware
requirement, reviews, trailers, etc.
Update 1 review:
I have typed rough structure of my project. I have confirmed that applying of
youtube api is working. Next step, I will let my application being able to show the
website of the trailer of the game. Besides, I have proved that web crawler is useful
on game critic forum (IGN.com); then, I will find out the part of the review of the
game. Moreover, because Steam store api key didn’t work, I need to find the way
that I can get the information from Steam webpage and find the other api key to fit
the requirement of final project.
Update 2:
I decide to cancel the function about watching review from IGN because I found
that the homepage of IGN is able to be crawled while it isn’t accessible to the page of
review of game. And I cannot find the proper store webpage to get the price of the
game to compare; thus, I only show the price on Steam. I use crawler on Steam to
get the price of game and the name of game’s publisher. Then, I choose to use the
google map api to search the profile of the publisher. Finally, I use tkinter to create
the GUI.
Run:
The libraries requirement:
import tkinter as tk
from tkinter import ttk
import urllib.request,urllib.parse,urllib.error
import json
from bs4 import BeautifulSoup
