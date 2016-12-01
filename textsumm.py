from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lex_rank import LexRankSummarizer #We're choosing Lexrank, other algorithms are also built in
import send
def textsummarization(filename,link):
    file = filename
    parser = PlaintextParser.from_file(file, Tokenizer("english"))
    summarizer = LexRankSummarizer()

    summary = summarizer(parser.document, 10) #Summarize the document with 5 sentences

    sentence1="<h1>MOM </h1><br><ul>"
    for sentence in summary:
        print sentence._text
        sentence1 = sentence1+"<br>"+"<li>"+sentence._text+".</li>"
    sentence1=sentence1+"<br></ul>"

    send.sendemail("<h2>Google drive Audio file Link</h2> "+link+"<br>"+sentence1)


