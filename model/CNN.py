import tensorflow as tf
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import VGG19, VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import os

image_shape = (150, 200, 3)


def VGG16_model(in_shape=image_shape, num_classes=10, freeze=False):
    # transfer learning from image net
    base = VGG16(weights='imagenet', include_top=False, input_shape=in_shape)

    if freeze:
        base.trainable = False

    model = Sequential()
    model.add(base)

    # Our prediction layers
    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(num_classes, activation='softmax'))

    return model


def split_dataset():
    base_dir = os.path.join(os.getcwd(), "./PSA-Grades-Baseball/")
    train_ds = tf.keras.utils.image_dataset_from_directory(
        base_dir,
        labels="inferred",
        validation_split=0.1,
        subset="both",
        seed=2024,
        shuffle=True,
        image_size=(image_shape[0], image_shape[1]),
        batch_size=32)

    return train_ds


if __name__ == "__main__":
    class_names = ["psa10", "psa9", "psa8", "psa7", "psa6", "psa5", "psa4", "psa3", "psa2", "psa1"]
    dataset = split_dataset()
    train = dataset[0]
    test = dataset[1]
    mlmodel = VGG16_model(freeze=True)
    adam = Adam(learning_rate=0.00001)
    mlmodel.compile(optimizer=adam, loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    history = mlmodel.fit(train, batch_size=30, epochs=20, validation_data=test)
    mlmodel.layers[0].trainable = True
    mlmodel.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=0.000001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    history2 = mlmodel.fit(train, batch_size=30, epochs=20, validation_data=test)
    mlmodel.save("grading.keras")
    # mlmodel = tf.keras.models.load_model('grading.keras')
    mlmodel.summary()
