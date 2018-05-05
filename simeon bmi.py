import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
import kivy
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, BooleanProperty
from kivy.uix.textinput import TextInput
from kivy.uix.textinput import *
from kivy.uix.dropdown import DropDown
import datetime
import subprocess
import time
import twilio
from twilio.rest import Client
from kivy.clock import Clock
from kivy.animation import Animation
from functools import partial
from kivy.core.audio import SoundLoader
import sys
import datetime
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase

from kivy.utils import get_color_from_hex

from time import strftime
import smtplib

import pymysql
import pymysql.cursors
import datetime 
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
import numpy as np
import math
from math import sqrt
import quandl
import statistics


class First(Screen):
    pass











class Calculator(Screen):

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)


    def calculate(self):
        weight = int(self.ids.weight.text)
        height = int(self.ids.height.text)

        BMI = round((weight * 703) / (height ** 2))

        if BMI < 18.5:
            self.ids.results.text += "Your BMI is " + str(BMI) + " which means you are underweight."


        elif BMI >= 18.5 and BMI < 25:
            self.ids.results.text += "Your BMI is " + str(BMI) + " which means you are in the normal weight range."

    

        elif BMI >= 25 and BMI  <= 30:
            self.ids.results.text += "Your BMI is " + str(BMI) + " which means you are overwieght."
            




        elif BMI >  30:
            self.ids.results.text += "Your BMI is " + str(BMI) + " which means you are obese."

        else:
            self.ids.results.text += "An error occured. Please try again."

    def clear(self):
        self.ids.results.text = ""
        self.ids.weight.text = ""
        self.ids.height.text = ""
        
    




class ScreenManagement(ScreenManager):
    pass



starter = Builder.load_file("simeonbmiapp.kv")


class SimeonBmiApp(App):
    def build(self):
        return starter
    
if __name__=='__main__':
    SimeonBmiApp().run()
