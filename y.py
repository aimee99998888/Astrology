import streamlit as st
from io import StringIO

st.markdown(
    f"""
       <style>
       .stApp {{
           background-image: url("https://i.pinimg.com/originals/dc/84/36/dc8436d03012b7204637ed7207a05808.gif");
           background-attachment: fixed;
           background-size: cover;
           /* opacity: 0.3; */
       }}
       """,
    unsafe_allow_html=True
)
e1,e2,e3 =st.tabs(["Astrology App","calculate moon sign","uploaded"])
with e1:
    import streamlit as st

    # Import the get_horoscope function
    import requests


    def get_horoscope(zodiac_sign):
        url = f"https://aztro.sameerkumar.website/?sign={zodiac_sign.lower()}&day=today"
        response = requests.post(url)
        if response.status_code == 200:
            result = response.json()
            horoscope = result["description"]
            return horoscope
        else:
            return "Failed to get horoscope."


    # Create a title for the app
    st.title("Astrology App")

    # Create a dropdown menu for the zodiac signs
    zodiac_signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius",
                    "Capricorn", "Aquarius", "Pisces"]
    selected_zodiac_sign = st.selectbox("Select your zodiac sign", zodiac_signs)

    # Create a button to generate the horoscope
    if st.button("Generate horoscope"):
        # Generate the horoscope based on the selected zodiac sign
        horoscope = get_horoscope(selected_zodiac_sign)
        # Display the horoscope to the user
        st.write(horoscope)

with e2:
    import streamlit as st
    import datetime


    # สร้างฟังก์ชันคำนวณดวงจันทร์
    def calculate_moon_sign(day, month, year):
        date = datetime.date(year, month, day)
        days_in_month = 29 + (month + month // 3) % 2
        month_start = datetime.date(year, month, 1)
        month_end = datetime.date(year, month, days_in_month)

        # คำนวณจำนวนวันตั้งแต่เดือนเริ่มต้นจนถึงวันเกิด
        days_since_start = (date - month_start).days + 1

        # คำนวณหา phase ของจันทร์ โดยใช้วันที่หมดอายุของเดือนเป็น phase 0
        moon_phase = (days_since_start / days_in_month) * 30
        moon_phase = moon_phase % 30

        # หา sign ของดวงจันทร์จาก moon phase
        if moon_phase < 3.3333:
            return "Aries"
        elif moon_phase < 6.6666:
            return "Taurus"
        elif moon_phase < 10:
            return "Gemini"
        elif moon_phase < 13.3333:
            return "Cancer"
        elif moon_phase < 16.6666:
            return "Leo"
        elif moon_phase < 20:
            return "Virgo"
        elif moon_phase < 23.3333:
            return "Libra"
        elif moon_phase < 26.6666:
            return "Scorpio"
        elif moon_phase < 30:
            return "Sagittarius"


    # สร้างเนื้อหาหน้าเว็บ
    st.title("calculate moon sign")
    st.write("your date of birth")

    # รับข้อมูลวันเกิด
    day = st.slider("day", 1, 31, 1)
    month = st.slider("month", 1, 12, 1)
    year = st.slider("Years", 1900, 2023, 1990)

    # คำนวณดวงจันทร์
    moon_sign = calculate_moon_sign(day, month, year)

    # แสดงผลลัพธ์
    st.write("your moon", moon_sign)

with e3:
    st.title("uploaded")

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)