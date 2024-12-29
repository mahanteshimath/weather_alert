import streamlit as st
import streamlit.components.v1 as components


st.markdown("""
### Problem Statement: Open Weather Challenge

The goal of this challenge is to design and implement a service that fetches daily weather forecast data for a specified location and sends it via email to users. The solution should integrate the Weather API provided by OpenWeather to retrieve forecast information based on latitude and longitude and leverage cloud services to create a scalable and efficient system.

### Requirements:
1. **Weather Data**: Use the OpenWeather API to fetch the latest weather forecast for a given location (specified by latitude and longitude).
2. **Email Notification**: Send the fetched weather forecast as an email to the intended recipients.
3. **Implementation Language**: Develop the solution using Python for both fetching weather data and sending emails.
4. **Cloud Services**: Incorporate AWS or GCP services for any additional infrastructure needs, ensuring scalability, reliability, and cost-effectiveness.
5. **Documentation**: Provide clear documentation of the design and implementation, including steps to set up and run the service.

### Key Deliverables:
1. **Python Scripts**: Code for fetching weather data from the OpenWeather API and sending emails.
2. **Cloud Architecture**: Recommendations and/or implementation of cloud services (AWS or GCP) used to support the service, such as:
   - Task scheduling (e.g., AWS CloudWatch, Google Cloud Scheduler).
   - Serverless computing (e.g., AWS Lambda, Google Cloud Functions).
   - Email service integration (e.g., AWS SES, SMTP).
3. **Design Documentation**: A detailed explanation of the architecture, dependencies, and steps to deploy and execute the solution. 

### Objective:
Deliver a robust and scalable solution that ensures daily weather forecasts are sent reliably via email, meeting the specified constraints and requirements.

""")

st.markdown("""------""")

st.title("Architecture Diagram")
with open("./src/WeatherForecast.txt", "r") as file:
   html_content = file.read()
components.html(html_content, width=800, height=600, scrolling=True)


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