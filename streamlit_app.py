import cv2 
import streamlit as st
from PIL import Image
import numpy as np
import requests



def Camera():
    global name
    global section
    cam_mode = st.checkbox("Enable Camera")
    picture = st.camera_input("Attendance Check!!!" , disabled=not cam_mode)
    
    if picture is not None:
        byte = picture.getvalue()
        cv2_img =  cv2.imdecode(np.frombuffer(byte, np.uint8), cv2.IMREAD_COLOR)
        detector = cv2.QRCodeDetector()

        data, bbox, straight_qrcode = detector.detectAndDecode(cv2_img)
        st.write(data)
        print(data)

        data = data.split(", ")
        name = data[0]
        section = data[1]
        attendance()



def attendance():
    url = "https://docs.google.com/forms/d/1M3fMgk_zU2X5SXNdyv8SipNehEQZeOoDJ8DoRYCjOnw/formResponse"

    data = {
        "entry.530719642" : f"{name}",   
        "entry.1493533031" : f"{section}"
    }

    try:
        response = requests.post(url, data=data)

        print(response)
        print(response.status_code)

    except:
        pass


Camera()
