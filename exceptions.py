# import numpy as np
# import pandas as pd
# import operator
# import json
# from pprint import pprint
# import xmljson
# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint
# import datetime
# import time
# import schedule
# import re
from IPython.core.display import display


def check_server(mode):
    if mode == "memory":
        print("Memory is ok")
    elif mode == "connection":
        print("Connection is ok")
    else:
        raise ValueError()


check_server("memory")
