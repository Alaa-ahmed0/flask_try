from flask import Flask,render_template
#from flask import Flask, request, url_for
#from flask_socketio import SocketIO
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
# Define the filenames for the two FASTA files
file1 = "tp53(3).fasta"
file2 = "rs1042522.fasta"

skills_app = Flask(__name__)

@skills_app.route('/')
def blast():
    # Read the sequences from the files and split them into words
    with open(file1) as f:

        words1 = set()
        for record in SeqIO.parse(f, "fasta"):
            seq = str(record.seq)
            for i in range(len(seq)-10):
                word = seq[i:i+11]
                words1.add(word)
    with open(file2) as f:
        words2 = set()
        for record in SeqIO.parse(f, "fasta"):
            seq = str(record.seq)
            for i in range(len(seq)-10):
                word = seq[i:i+11]
                words2.add(word)

    # Calculate the percentage identity
    total_words = len(words1.union(words2))
    shared_words = len(words1.intersection(words2))
    percentage_identity = (shared_words / len(words2)) * 100
    identity=str(percentage_identity)
    # Print the percentage identity
    return identity
    #print("Percentage identity: {:.2f}%".format(percentage_identity))

# @skills_app.route('/about')
# def aboutpage():
#     return render_template("about.html")
# @skills_app.route('/')
# def homepage():
#     print("hello")
if __name__ == '__main__':
    skills_app.run(debug=True)
# import requests

# url = 'http://127.0.0.1:5000/blast'
# # #'http://127.0.0.1:5000/blast'
# # #'https://blast-app-f7li.onrender.com'
# # #'http://localhost:5000/blast'

# data = {'query': 'file2', 'subject': 'file1'}
# response = requests.post(url, data=data)
# print(response.text)
