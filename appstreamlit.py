from PIL import Image
import requests
import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Vishnu Gopan", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/stylest.css")


#load assests
lottie_coding=load_lottieurl("https://lottie.host/d5515d28-d1c8-4f04-bbf2-1c5e9388ae7d/eYn042HS4k.json")
img_contact_form=Image.open("stimages/Bluetooth car.jpg")
img_contact_form1=Image.open("stimages/Billing system.jpg")
img_contact_form2=Image.open("stimages/LED .jpg")
img_contact_form3=Image.open("stimages/RFID.jpg")

#header section
with st.container():
    st.subheader("Hi,I am VISHNU GOPAN:wave:")
    st.title(" Electronics Engineering in India")
    st.write("I am an Engineer who is more passionat in electronics and programming")
    #st.write("[Learn more>](link)")

with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("MY WORKS")
        st.write("##")
        st.write(
            """
        
            *Bluetooth Controlled RC car using Arduino Uno      
            *Billing System using python Tkinder         
            *Controlling LED using fingers using Open CV       
            *RFID and Keypad based door look system using Arduino
            *Basic Python projects
            """
        )
        with right_column:
            st_lottie(lottie_coding,height=300,key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write('##')
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    #insert image
    with text_column:
        st.subheader("Bluetooth controlled car using arduino uno")
        st.write(
            """"
            the components used in the project include HC05 bluetooth module,arduino uno
            """
        )
        #st.markdown("[github link...](link))
    st.write("---")
with st.container():
             image_column, text_column = st.columns((1, 2))
             with image_column:
                 st.image(img_contact_form1)
             # insert image
             with text_column:
                 st.subheader("Billing System using python Tkinder")
                 st.write(
                     """"
                     the components used in the project include HC05 bluetooth module,arduino uno
                     """
                 )
                 # st.markdown("[github link...](link))

             st.write("---")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form2)
    # insert image
    with text_column:
        st.subheader("Controlling LED using fingers using Open CV")
        st.write(
            """"
            the components used in the project include HC05 bluetooth module,arduino uno
            """
        )
        # st.markdown("[github link...](link))
    st.write("---")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form3)
    # insert image
    with text_column:
        st.subheader("RFID and Keypad based door look system using Arduino")
        st.write(
            """"
            the components used in the project include HC05 bluetooth module,arduino uno
            """
        )
        # st.markdown("[github link...](link))
    st.write("---")

#contact
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")
    contact_form="""
    <form action="https://formsubmit.co/vishnugopan015@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email"required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
    
    """

    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
            st.empty()

