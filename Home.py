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
    "pages/About.py",
    title="About",
    icon=":material/home:",
    default=True,
)

pg2 = st.Page(
    "pages/Architecture.py",
    title="Architecture",
    icon=":material/cognition:"
)

pg3 = st.Page(
    "pages/WeatherAlert.py",
    title="WeatherAlert",
    icon=":partly_sunny:"
)

pg = st.navigation(
    {
        "Info": [About,Architecture_page],
        "Openweathermap": [WeatherAlert]
    }
)


pg.run()