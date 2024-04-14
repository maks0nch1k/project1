from toxicity import ToxicCommentsDetector
import keras

keras.models.load_model('my_model')
keras.model.load_weights('my_model')

test_raw_texts = [
 'ты чего берега попутал?',
 'это правый берег реки, не путай с левым'
]
toxicDetector = ToxicCommentsDetector()
print(toxicDetector.predict(test_raw_texts))