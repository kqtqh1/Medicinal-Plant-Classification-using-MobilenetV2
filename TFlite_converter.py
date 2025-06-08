import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the Keras model
model = load_model("\Users\\kathl\\best_model_Mobilenet.keras")
# Convert the Keras model to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the TFLite model to a file
with open('best_model_Mobilenet.tflite', 'wb') as f:
    f.write(tflite_model)

print("model has been successfully converted to TFLite format")
