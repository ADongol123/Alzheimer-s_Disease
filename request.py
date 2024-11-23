import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://worldpopulationreview.com/static/states/population.json"
response = requests.get(url)

print(response)
