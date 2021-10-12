from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import tensorflow

labels = ['mysore_pak', 'ghevar', 'sohan_papdi', 'ras_malai', 'ariselu', 'kofta', 'aloo_tikki', 'gajar_ka_halwa', 'chhena_kheeri', 'kakinada_khaja', 'lassi', 'naan', 'chak_hao_kheer', 'butter_chicken', 'kajjikaya', 'chicken_razala', 'lyangcha', 'aloo_gobi', 'dal_makhani', 'bandar_laddu', 'bhindi_masala', 'unni_appam', 'kuzhi_paniyaram', 'sandesh', 'sohan_halwa', 'rasgulla', 'shankarpali', 'pithe', 'imarti', 'misti_doi', 'navrattan_korma', 'daal_puri', 'malapua', 'dal_tadka', 'aloo_matar', 'palak_paneer', 'makki_di_roti_sarson_da_saag', 'poornalu', 'chicken_tikka', 'kadhi_pakoda', 'basundi', 'chapati', 'phirni', 'chikki', 'sheera', 'karela_bharta', 'cham_cham', 'shrikhand', 'litti_chokha', 'qubani_ka_meetha', 'jalebi', 'kachori', 'aloo_methi', 'maach_jhol', 'kadai_paneer', 'doodhpak', 'chana_masala', 'boondi', 'misi_roti', 'bhatura', 'chicken_tikka_masala', 'double_ka_meetha', 'kalakand', 'poha', 'adhirasam', 'ledikeni', 'dharwad_pedha', 'dum_aloo', 'sutar_feni', 'gavvalu', 'anarsa', 'rabri', 'daal_baati_churma', 'sheer_korma', 'pootharekulu', 'aloo_shimla_mirch', 'gulab_jamun', 'paneer_butter_masala', 'modak', 'biryani']
new_list = []
for i in labels:
    i = i.title().replace('_',' ')
    new_list.append(i)
print(labels)
print(new_list)
model = tensorflow.keras.models.load_model('IF.h5')
image=load_img('./archive/kofta/6e0a11570f.jpg',target_size=(40,40))
image=img_to_array(image)
image=image/255.0
prediction_image =np.array(image)
prediction_image = np.expand_dims(image, axis=0)

prediction=model.predict(prediction_image)
value=np.argmax(prediction)
print(value)
# move_name=mapper(value)
print("Prediction is ",new_list[int(value)])