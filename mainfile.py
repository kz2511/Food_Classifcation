import streamlit as st
from PIL import Image
import pandas as pd
import base64,random
import time,datetime
import io,random
from PIL import Image
import pymysql
import pafy
import matplotlib.pyplot as plt
import tensorflow
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
from test2 import calories
from test3 import catogries
from video import *
from t1 import video_links
import random
import pafy
import pymysql

def fetch_yt_video(link):
    video = pafy.new(link)
    return video.title

def get_table_download_link(df,filename,text):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    # href = f'<a href="data:file/csv;base64,{b64}">Download Report</a>'
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href


st.set_page_config(
   page_title="Food Classification",
   page_icon="logo.ico",
)
labels = ['mysore_pak', 'ghevar', 'sohan_papdi', 'ras_malai', 'ariselu', 'kofta', 'aloo_tikki',
                          'gajar_ka_halwa', 'chhena_kheeri', 'kakinada_khaja', 'lassi', 'naan', 'chak_hao_kheer',
                          'butter_chicken', 'kajjikaya', 'chicken_razala', 'lyangcha', 'aloo_gobi', 'dal_makhani',
                          'bandar_laddu', 'bhindi_masala', 'unni_appam', 'kuzhi_paniyaram', 'sandesh', 'sohan_halwa',
                          'rasgulla', 'shankarpali', 'pithe', 'imarti', 'misti_doi', 'navrattan_korma', 'daal_puri', 'malapua',
                          'dal_tadka', 'aloo_matar', 'palak_paneer', 'makki_di_roti_sarson_da_saag', 'poornalu',
                          'chicken_tikka', 'kadhi_pakoda', 'basundi', 'chapati', 'phirni', 'chikki', 'sheera', 'karela_bharta',
                          'cham_cham', 'shrikhand', 'litti_chokha', 'qubani_ka_meetha', 'jalebi', 'kachori', 'aloo_methi',
                          'maach_jhol', 'kadai_paneer', 'doodhpak', 'chana_masala', 'boondi', 'misi_roti', 'bhatura',
                          'chicken_tikka_masala', 'double_ka_meetha', 'kalakand', 'poha', 'adhirasam', 'ledikeni',
                          'dharwad_pedha', 'dum_aloo', 'sutar_feni', 'gavvalu', 'anarsa', 'rabri', 'daal_baati_churma',
                          'sheer_korma', 'pootharekulu', 'aloo_shimla_mirch', 'gulab_jamun', 'paneer_butter_masala', 'modak',
                          'biryani']
new_list = []
for i in labels:
    i = i.title().replace('_', ' ')
    new_list.append(i)
print(new_list)

def load_image(uploaded_file):
    img = Image.open(uploaded_file).resize((250,250))
    return img


connection = pymysql.connect(host="localhost", user="root", password="", database="FOOD_PREDICTION")
cursor = connection.cursor()

def run():

    st.sidebar.markdown("# Choose User")
    activities = ["Normal User", "Admin"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)

    if choice == 'Normal User':
        st.title('Food Classification and Calorie Count')
        uploaded_file = st.file_uploader("Upload Food Image", type=['png', 'jpeg', 'jpg'])
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type,
                            "FileSize": uploaded_file.size}
            # st.write(file_details)
            st.image(load_image(uploaded_file))
            save_image_path = './Upload_Images/' + uploaded_file.name
            with open(save_image_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            model = tensorflow.keras.models.load_model('IF (1).h5')
            image = load_img(save_image_path, target_size=(40, 40))
            image = img_to_array(image)
            image = image / 255.0
            prediction_image = np.array(image)
            prediction_image = np.expand_dims(image, axis=0)

            prediction = model.predict(prediction_image)
            value = np.argmax(prediction)
            # move_name=mapper(value)
            food_name = new_list[int(value)]
            rec_vid_list = video_links[food_name]
            ran_video = random.choice(rec_vid_list)
            print(ran_video)

            st.header("🍲 **Prediction Food is " + food_name+'**')
            st.subheader('✅ You will get the ' + str(calories[new_list[int(value)]]) + ' Calories from ' + new_list[int(value)])
            if str(catogries[new_list[int(value)]]) == 'Veg':
                st.success('This Food is  ' + str(catogries[new_list[int(value)]]))
            else:
                st.error('This Food is  ' + str(catogries[new_list[int(value)]]))

            ## Recommend video
            st.header("**Recipe Video For " + food_name + '**')
            vid_ti = fetch_yt_video(ran_video)
            st.subheader(vid_ti)
            st.video(ran_video)

            videoLinksCommaSeperated = ""
            for i in rec_vid_list:
                videoLinksCommaSeperated += str(i) + ", "



            print("Video Links Seperated", videoLinksCommaSeperated)
            #     Query
            query = 'INSERT INTO predictions(prediction, veg_or_non_veg, calorie_count, youtube_predictions, image_path) VALUES(%s,%s,%s,%s,%s)'
            valuesToInsert = (food_name, str(catogries[new_list[int(value)]]), str(calories[new_list[int(value)]]),
                              videoLinksCommaSeperated, save_image_path)
            cursor.execute(query, valuesToInsert)

            connection.commit()

        else:
            st.warning("Upload an Image to continue.")

    else:
        st.title('Food Classification and Calorie Count')
        ## Admin Side
        st.info('Welcome to admin side')
        st.sidebar.warning('Please Enter Id and Password')

        ad_user = st.text_input("Username")
        ad_password = st.text_input("Password", type='password')
        if st.button('Login'):
            if ad_user == 'Kunal' and ad_password == 'Kunal2511':
                st.info("Welcome Kunal")
                # Display Data
                # Display Data
                cursor.execute('''SELECT*FROM predictions''')
                data = cursor.fetchall()
                st.header("**Food Prediction Records**")
                df = pd.DataFrame(data, columns=['id','prediction','veg_or_non_veg','calorie_count','youtube_predictions','image_path'])
                st.dataframe(df)
                st.markdown(get_table_download_link(df,"data.csv","Download"), unsafe_allow_html=True)
                #st.markdown(get_table_download_link(df,'User_Data.csv','Download Report'), unsafe_allow_html=True)



            else:
                st.error("Wrong ID & Password Provided")
run()