from flask import Flask, request, render_template
import re
import pickle
import nltk
from nltk.corpus import stopwords
#from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''    
    #text = request.form['text']
    text=request.form.get("text", False)
    processed_text = text.lower()
    try:
        if len(processed_text) > 0:
            lemmatizer = WordNetLemmatizer()
            review = re.sub('[^a-zA-Z]', ' ', processed_text)
            review = review.lower()
            review = review.split()    
            review = [lemmatizer.lemmatize(word) for word in review if not word in stopwords.words('english')]
            review = ' '.join(review)
            # Load the countvectorizer 
            countvectorizer = pickle.load(open('countvectorizer.pkl','rb'))
            text_tfidf=countvectorizer.transform([review])
        else:
            prediction = 2
    except BaseException as be:
        return render_template('index.html', prediction_text='There is an user defined exception: {}'.format(str(type(be).__name__) + ' ' + str(be)))
    prediction = model.predict(text_tfidf) 
    output = ''
    if prediction == 1:
        output = 'HAM'
    elif prediction == 0:
        output = 'SPAM'
    else:
        output = 'NULL Value'

    return render_template('index.html', prediction_text='The given SMS is a {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)