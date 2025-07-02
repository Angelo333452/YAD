from flask import Flask, render_template, request

app = Flask(__name__)

programming_dict = {
    "variable": "A container for storing data values.",
    "function": "A block of code that runs when it is called.",
    "loop": "A way to repeat code multiple times.",
    "class": "A blueprint for creating objects.",
    "list": "An ordered, mutable collection of items.", 
    "tuple": "An ordered, immutable collection of items.",
    "dictionary": "An unordered collection of key-value pairs."
}

@app.route("/", methods=["GET", "POST"])
def home():
    meaning = None  
    word = None     

    if request.method == "POST":
        word = request.form.get("word_input") 
        if word:
        
            meaning = programming_dict.get(word.lower(), "Word not found in dictionary.")
        else:
            meaning = "Please enter a word."

    return render_template("index.html", word=word, meaning=meaning)

if __name__ == '__main__':
    app.run(debug=True) 
