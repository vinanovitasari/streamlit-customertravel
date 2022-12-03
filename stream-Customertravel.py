import pickle
import streamlit as st

Customer_model = pickle.load(open('Customertravel_model.sav', 'rb'))

st.title('Memprediksi Pelanggan Akan Bergeser Atau Tidak DiPerusahaan Tour & Travel')

Age = st.text_input('Input Nilai Age')

FrequentFlyer = st.text_input('Input Nilai FrequentFlyer ( No : 1,   Norecord : 2, Yes : 3 )')

AnnualIncomeClass = st.text_input('Input Nilai AnnualIncomeClass ( HigtIncome : 1,   lowIncome : 2,   middleIncome : 3 )')

ServicesOpted = st.text_input('Input Nilai ServicesOpted ( 1 - 6 )')

AccountSyncedToSocialMedia = st.text_input('Input Nilai AccountSyncedToSocialMedia ( Yes : 1,   No : 0 )')

BookedHotelOrNot = st.text_input('Input Nilai Booked Hotel Or Not  (  Yes : 1,   No : 0 )')


Customer_diagnosis = ''

if st.button('Test Presiksi Pelanggan'):
    Customer_diagnosis = Customer_model.predict([[Age, FrequentFlyer, AnnualIncomeClass, ServicesOpted, AccountSyncedToSocialMedia, BookedHotelOrNot]])

    if(Customer_diagnosis[0] == 1):
        Customer_diagnosis = 'Pelanggan Akan Bergeser'
    else :
            Customer_diagnosis = 'Pelanggan Tidak Akan Bergeser'

    st.success(Customer_diagnosis)
