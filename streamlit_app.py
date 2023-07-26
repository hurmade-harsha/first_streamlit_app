import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 avocado, toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


#create the reeatable code block(called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized 

#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
       streamlit.error("please select a fruit to get information,")
  else:
#streamlit.write('The user entered ', fruit_choice)
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
       #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
       #fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
       #streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()


streamlit.header("The fruit load list contains:")
#snowflake -related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur: 
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
#add a button to load the fruit
if streamlit.button('Get Fruit load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_row = get_fruit_load_list()
    streamlit.dataframe(my_data_row)


def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur: 
        my_cur.execute("insert into fruit_load_list values('" + ???? +"')")
        return "Thanks for adding " + new_fruit
add_my_fruit = streamlit.text_input('what fruit would you like to add?')       
#add a button to load the fruit
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_froim_function)

# add button to load the fruit list
if streamlit.button('Get fruit list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_cur.execute("select * from fruit_load_list")
    my_cnx.close()
    streamlit.dataframe(my_data_row)
    
streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)
#challenge

fruit_choice1 = streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write('Thanks for adding ', fruit_choice1)

streamlit.write('thanks for adding', fruit_choice1 )
my_cur.execute("insert into fruit_load_list values ('from streamlit')")







