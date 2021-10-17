# import statements
import streamlit as st
from PIL import Image
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import tensorflow
import time
from test2 import calories

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
def load_image(uploaded_file):
    img = Image.open(uploaded_file).resize((250,250))
    return img

def run():
# adding title in the app
    st.title('Food Classification and calorie count')
    # load Image
    # Adding upload file option in the web
    uploaded_file = st.file_uploader("Upload Food Image", type=['png','jpeg','jpg'])
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
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
        st.success("Prediction is "+ new_list[int(value)])
        st.info('You will get the '+str(calories[new_list[int(value)]])+' Calories from '+new_list[int(value)])
    else:
        st.warning("Upload an Image to continue.")
run()