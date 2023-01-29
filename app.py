import streamlit as st
import pandas as pd
import pickle
import numpy as np


# Loading Data

data_dict = pickle.load(open('data.pkl', 'rb'))
data = pd.DataFrame(data_dict)

model = pickle.load(open('model.pkl', 'rb'))

# UI
st.title("Restaurent Rating Prediction System")

online_order = st.selectbox(
    'Select yes or no for online order features:', ['Yes', 'No'])
online_dict = {'Yes': 1,
               'No': 0}
online_order = online_dict.get(online_order)
# st.write(online_order)


book_table = st.selectbox(
    'Select yes or no for book table features:', ['Yes', 'No'])
book_dict = {'Yes': 1,
             'No': 0}
book_table = book_dict.get(book_table)
# st.write(book_table)

loc_name = data['location'].unique()
location = st.selectbox('Select Location:', loc_name)
loc_dict = {'Banashankari': 1,
            'Basavanagudi': 4,
            'others': 41,
            'Jayanagar': 18,
            'JP Nagar': 17,
            'Bannerghatta Road': 3,
            'BTM': 0,
            'Electronic City': 13,
            'HSR': 15,
            'Marathahalli': 29,
            'Shanti Nagar': 36,
            'Koramangala 5th Block': 23,
            'Richmond Road': 34,
            'Koramangala 7th Block': 25,
            'Koramangala 4th Block': 22,
            'Bellandur': 5,
            'Sarjapur Road': 35,
            'Whitefield': 40,
            'Old Airport Road': 31,
            'Indiranagar': 16,
            'Koramangala 1st Block': 21,
            'Frazer Town': 14,
            'MG Road': 27,
            'Brigade Road': 6,
            'Lavelle Road': 26,
            'Church Street': 8,
            'Ulsoor': 39,
            'Residency Road': 33,
            'Shivajinagar': 37,
            'St. Marks Road': 38,
            'Cunningham Road': 10,
            'Commercial Street': 9,
            'Domlur': 11,
            'Ejipura': 12,
            'Malleshwaram': 28,
            'Kammanahalli': 20,
            'Koramangala 6th Block': 24,
            'Brookefield': 7,
            'Rajajinagar': 32,
            'Banaswadi': 2,
            'Kalyan Nagar': 19,
            'New BEL Road': 30}

location = loc_dict.get(location)
# st.write(location)

votes = int(st.number_input('Enter votes:', step=1))

rest_type = st.selectbox('Select Restaurent Type:', data['rest_type'].unique())
rest_dict = {'Casual Dining': 2,
             'others': 8,
             'Quick Bites': 6,
             'Cafe': 1,
             'Delivery': 4,
             'Dessert Parlor': 5,
             'Bakery': 0,
             'Takeaway, Delivery': 7,
             'Casual Dining, Bar': 3}

# st.write(rest_type)
rest_type = rest_dict.get(rest_type)
cuisines = st.selectbox('Select cuisines:', data['cuisines'].unique())
cuisines_dict = {'North Indian, Mughlai, Chinese': 54,
                 'others': 69,
                 'South Indian, North Indian': 65,
                 'North Indian': 43,
                 'Cafe': 16,
                 'Cafe, Continental': 18,
                 'Cafe, Fast Food': 20,
                 'Cafe, Bakery': 17,
                 'Bakery, Desserts': 4,
                 'Pizza': 58,
                 'Biryani': 9,
                 'North Indian, Chinese, Fast Food': 48,
                 'Chinese, Thai, Momos': 25,
                 'South Indian': 60,
                 'Burger, Fast Food': 15,
                 'Pizza, Fast Food': 59,
                 'North Indian, Chinese': 45,
                 'Chinese, Thai': 24,
                 'Ice Cream, Desserts': 37,
                 'Biryani, Fast Food': 10,
                 'Fast Food, Burger': 33,
                 'Desserts, Beverages': 29,
                 'Chinese': 21,
                 'Bakery': 3,
                 'Biryani, South Indian': 14,
                 'Fast Food': 31,
                 'South Indian, Chinese, North Indian': 63,
                 'Mithai, Street Food': 42,
                 'South Indian, Chinese': 62,
                 'Biryani, North Indian, Chinese': 13,
                 'Desserts': 27,
                 'Ice Cream': 36,
                 'South Indian, North Indian, Chinese': 66,
                 'South Indian, Biryani': 61,
                 'Beverages': 6,
                 'Mithai': 41,
                 'North Indian, Street Food': 57,
                 'Chinese, North Indian': 23,
                 'South Indian, North Indian, Chinese, Street Food': 67,
                 'Andhra': 0,
                 'Italian, Pizza': 38,
                 'Street Food': 68,
                 'Arabian': 2,
                 'North Indian, Chinese, Continental': 47,
                 'Desserts, Ice Cream': 30,
                 'North Indian, Chinese, Biryani': 46,
                 'Fast Food, Rolls': 34,
                 'Beverages, Fast Food': 8,
                 'North Indian, Chinese, South Indian': 50,
                 'South Indian, Fast Food': 64,
                 'North Indian, Fast Food': 52,
                 'Beverages, Desserts': 7,
                 'North Indian, Continental': 51,
                 'North Indian, South Indian': 55,
                 'North Indian, Biryani': 44,
                 'Finger Food': 35,
                 'Continental': 26,
                 'Fast Food, Beverages': 32,
                 'Andhra, Biryani': 1,
                 'Biryani, Kebab': 11,
                 'North Indian, Mughlai': 53,
                 'North Indian, South Indian, Chinese': 56,
                 'Cafe, Desserts': 19,
                 'Biryani, North Indian': 12,
                 'Chinese, Momos': 22,
                 'Kerala, South Indian': 40,
                 'Desserts, Bakery': 28,
                 'Bakery, Fast Food': 5,
                 'Kerala': 39,
                 'North Indian, Chinese, Seafood': 49}

cuisines = cuisines_dict.get(cuisines)
# st.write(cuisines)

cost = st.number_input("Enter cost for 2 person:")

type_select = st.selectbox("Enter type:", data['type'].unique())
type_dict = {'Buffet': 0,
             'Cafes': 1,
             'Delivery': 2,
             'Desserts': 3,
             'Dine-out': 4,
             'Drinks & nightlife': 5,
             'Pubs and bars': 6}

type_select = type_dict.get(type_select)
# st.write(type_select)

if st.button('submit'):
    lst = [online_order, book_table, location, votes,
           rest_type, cuisines, cost, type_select]
    final_result = [np.array(lst)]
    prediction = model.predict(final_result)
    output = round(prediction[0], 1)
    st.write("Rating is: ", output)
