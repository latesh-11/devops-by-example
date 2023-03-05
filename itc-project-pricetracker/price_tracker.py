from inspect import ClassFoundException
from msilib.schema import Class
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib.request
import smtplib
import ssl
import requests
import email.message  
from time import sleep
from twilio.rest import Client


URL ='https://www.amazon.in/Apple-USB-C-Adapter-iPhone-AirPods/dp/B08L5WWFCY/?_encoding=UTF8&pd_rd_w=89Rwo&content-id=amzn1.sym.a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_p=a591f53f-b25f-40ba-9fb6-d144bc8febfb&pf_rd_r=0HZ4KPZJW7Y9E06PQWCX&pd_rd_wg=huN9z&pd_rd_r=313da1bf-d233-4e50-a174-64118967d1c1&ref_=pd_gw_ci_mcx_mr_hp_atf_m'
receiver_email = 'XYZ@gmail.com'
receiver_phone = 'YOUR NO. WITH COUNTRY CODE'



# Function to extract price of the product

def get_price(URL):
    # Send a request to the URL with headers
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(URL, headers=headers)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the product title and price elements
        product_title = soup.find(id="productTitle" , class_="a-size-large product-title-word-break")
        product_price = soup.find(class_="a-price-whole")

        # Check if both elements were found
        if product_title is not None and product_price is not None:
            product_title = product_title.get_text().strip()
            product_price = float(product_price.get_text().strip()[1:].replace(',', ''))
            return product_title, product_price
        else:
            print("Error: Could not find product title or price on the page.")
            return None, None
    else:
        print("Error: Request failed with status code", response.status_code)
        return None, None







# Function to send an email
def send_email(product_title, product_price, URL, receiver_email):
    # Your email and password
    sender_email = "zkuffynedr@eurokool.com"
    sender_password = "sM%O#;EB"

    # Email subject and body
    subject = f"{product_title} is now {product_price}!"
    body = f"Check out the product here: {URL}"

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=message)

# Function to send an SMS using Twilio
def send_sms(product_title, product_price, URL, receiver_phone):
    # Your Twilio account SID, auth token, and phone number
    account_sid = "XXXXXXXXXXXXXX"
    auth_token = "XXXXXXXXXXXXXXXXXXXX"
    twilio_phone = "COUNTRY CODE XXXXXXXXXX"

    # Create the Twilio client
    client = Client(account_sid, auth_token)

    # SMS message
    message = f"{product_title} is now {product_price}! Check it out here: {URL}"

    # Send the SMS message
    client.messages.create(to=receiver_phone, from_=twilio_phone, body=message)

# Function to track the price
def track_price(URL, receiver_email, receiver_phone):
    # Get the initial price of the product
    product_title, product_price = get_price(URL)
    if product_title is None or product_price is None:
        return
    min_price = product_price
    desired_price = 0.9 * product_price

    while True:
        # Wait for one hour
        sleep(10)

        # Get the current price of the product
        product_title, product_price = get_price(URL)
        if product_title is None or product_price is None:
            continue

        # Print the current price and the minimum price so far
        print(f"Title: {product_title}")
        print(f"Current Price: {product_price}")
        print(f"Minimum Price: {min_price}")
        print(f"Desired Price: {desired_price}\n")

        # Update the minimum price if necessary
        if product_price < min_price:
            min_price = product_price

        # Send an email and/or SMS if the price is less than or equal to the desired price
 
track_price(URL,receiver_email , receiver_phone)

print("Code is running perfectly")



