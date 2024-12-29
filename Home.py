import streamlit as st
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path
import time
import pandas as pd
from PIL import Image
from io import BytesIO
import requests 

st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

st.set_page_config(
  page_title="Weather Alert",
  page_icon=":partly_sunny:",
  layout="wide",
  initial_sidebar_state="expanded",
) 

# --- Info ---

pg1 = st.Page(
    "pages/Architecture.py",
    title="Architecture",
    icon=":material/cognition:",
    default=True,
)

pg2 = st.Page(
    "pages/WeatherAlert.py",
    title="WeatherAlert",
    icon=":material/cloud:"
)

pg = st.navigation(
    {
        "Info": [pg1],
        "Openweathermap": [pg2]
    }
)


pg.run()
