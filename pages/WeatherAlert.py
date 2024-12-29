import streamlit as st
import requests
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

st.logo(
    image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg",
    link="https://www.linkedin.com/in/mahantesh-hiremath/",
    icon_image="https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
)

W_BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
W_API_KEY = st.secrets["API_KEY"]


# Function to get weather data
def get_weather_data(lat, lon):
    params = {
        'lat': lat,
        'lon': lon,
        'appid': W_API_KEY,
        'units': 'metric'
    }
    response = requests.get(W_BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

# Function to load weather data
def load_weather_data(data):
    df = pd.DataFrame([{
        'date': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'wind_speed': entry['wind']['speed']
    } for entry in data['list']])
    df['date'] = pd.to_datetime(df['date'])
    return df

# Function to generate plot
def generate_weather_plot(df):
    sns.set_style("darkgrid")
    plt.figure(figsize=(12, 8))
    sns.lineplot(x='date', y='temperature', data=df, label='Temperature (°C)', color='darkorange', linewidth=2.5, marker='o', markersize=6)
    sns.lineplot(x='date', y='humidity', data=df, label='Humidity (%)', color='royalblue', linewidth=2.5, marker='o', markersize=6)
    sns.lineplot(x='date', y='wind_speed', data=df, label='Wind Speed (m/s)', color='forestgreen', linewidth=2.5, marker='o', markersize=6)

    plt.title(f'5-Day Weather Forecast', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Date and Time', fontsize=12)
    plt.ylabel('Value', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.legend(fontsize=12)
    plt.grid(axis='y', alpha=0.5)
    plt.tight_layout()

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer

# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, body, attachment):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html'))
    
    if attachment:
        part = MIMEText(attachment.read(), 'base64', 'utf-8')
        part.add_header('Content-Disposition', 'attachment', filename='weather_forecast.png')
        msg.attach(part)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        st.success(f"Email sent successfully to {recipient_email}!")
    except smtplib.SMTPAuthenticationError as e:
        st.error(f"Failed to send email: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

st.title("Weather Forecast and Email Service")

# Inputs
latitude = st.number_input("Enter Latitude:", value=16.504320)
longitude = st.number_input("Enter Longitude:", value=75.291748)
recipient_email = st.text_input("Enter Recipient Email:")
sender_email = 'learnatozaboutdata@gmail.com'
sender_password = st.secrets["SMTP"]

if st.button("Get Weather and Send Email"):
    try:
        # Fetch weather data
        weather_data = get_weather_data(latitude, longitude)
        df = load_weather_data(weather_data)

        # Generate plot
        plot_buffer = generate_weather_plot(df)

        # Display data and plot
        st.write("### Weather Data")
        st.dataframe(df)

        st.write("### Weather Forecast Plot")
        st.image(plot_buffer, use_column_width=True)

        # Send email
        email_body = f"<h1>Weather Forecast</h1><p>Find attached the 5-day weather forecast for latitude {latitude} and longitude {longitude}.</p>"
        send_email(sender_email, sender_password, recipient_email, "5-Day Weather Forecast", email_body, plot_buffer)
    except Exception as e:
        st.error(f"An error occurred: {e}")




st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: blue;
        color: white; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: blue;
        color: white; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
)

footer="""<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #2C1E5B;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤️ by <a style='display: inline; text-align: center;' href="https://www.linkedin.com/in/mahantesh-hiremath/" target="_blank">MAHANTESH HIREMATH</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)  
