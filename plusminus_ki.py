from tensorflow import keras
from scipy import ndimage
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Erstellen des Modells
model = keras.Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

# Kompilieren des Modells
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Erstellen des Datengenerators
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

# Laden der Trainings- und Testdaten
train_set = train_datagen.flow_from_directory('train', target_size=(64, 64), batch_size=32, class_mode='binary')
test_set = test_datagen.flow_from_directory('test', target_size=(64, 64), batch_size=32, class_mode='binary')

# Training des Modells
model.fit(train_set, epochs=20, validation_data=test_set)

# Vorhersage auf neuen Daten
new_image = keras.preprocessing.image.load_img('new_image.png', target_size=(64, 64))
new_image = keras.preprocessing.image.img_to_array(new_image)
new_image = new_image.reshape((1, new_image.shape[0], new_image.shape[1], new_image.shape[2]))
prediction = model.predict(new_image)

print(prediction)
if prediction > 0.5:
    print('Das Bild zeigt ein "-"')
else:
    print('Das Bild zeigt ein "+"')
