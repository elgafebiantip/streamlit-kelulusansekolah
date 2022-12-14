import pickle
import streamlit as st

#membaca model 

rekap_siswa = pickle.load(open('rekap_siswa.sav', 'rb'))

#Nama Web
st.subheader('Elga Febianti Putri')
st.subheader ('191351025 Malam B')
st.title('Prediksi Kelulusan Mahasiswa Universitas Nusantara')



col1, col2 = st.columns(2)

with col1 :
    IPS1 = st.text_input ('Masukan IPS Semester 1')
    IPS2 = st.text_input('Masukan IPS Semester 2')
    IPS3 = st.text_input('Masukan IPS Semester 3')
    IPS4 = st.text_input('Masukan IPS Semester 4')
with col2 :    
    IPS5 = st.text_input('Masukan IPS Semester 5')
    IPS6 = st.text_input('Masukan IPS Semester 6')
    IPS7 = st.text_input('Masukan IPS Semester 7')
    IPS8 = st.text_input('Masukan IPS Semester 8')
with col1 :
    IPK = st.text_input('Masukan IPK')

# Code untuk Prediksi
ket_Kelulusan = ''

# membuat Tombol Untuk Prediksi
if st.button('Test Prediksi Kelulusan') :
    ket_prediction = rekap_siswa.predict([[ IPS1, IPS2, IPS3, IPS4, IPS5, IPS6 , IPS7 , IPS8, IPK]])

    if(ket_prediction[0]==1):
        ket_Kelulusan = 'Mahasiswa Lulus'
    else : 
        ket_Kelulusan = 'Mahasiswa tidak lulus'

    st.success(ket_Kelulusan)