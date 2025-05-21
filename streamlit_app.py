import streamlit as st

st.title("AditTolonginDit")
st.write("stop judi, judi membuat mu rugi 🔥.")
st.image("Screenshot_20250520_165832.jpg", width=200) 

st.title("Aplikasi Radeung Bisa Berhitung") 
st.header("Radeung Bisa Ngitung, Coba Aja") 
angka = st.number_input ("coba tulis angka apa aja, radeung mah pinter:", value=0, step=1) 

if (angka % 2) == 0:
    st.write(f"{angka} Kata Radeung itu adalah bilangan genap") 
else:
    st.write(f"{angka} Kata Radeung itu adalah bilangan ganjil") 
    
