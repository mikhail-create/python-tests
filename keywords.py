import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc placerat leo nunc, quis dictum quam bibendum sit amet. Nulla facilisi. Quisque at varius magna, a lacinia nulla. Mauris dapibus velit dapibus, scelerisque risus at, venenatis metus. Duis iaculis nulla at libero malesuada consequat. Maecenas in risus non nibh sollicitudin feugiat. Nam sed condimentum felis. Sed sollicitudin justo dui, eget tempor diam dignissim vitae. Duis non eleifend diam, quis tincidunt lectus. Fusce ac viverra eros. Sed ullamcorper sed ante rutrum faucibus. Pellentesque hendrerit nibh turpis. Mauris fringilla at erat ac aliquet. Integer posuere condimentum leo quis rutrum. Aenean pharetra augue id faucibus sollicitudin."

sentenses = nltk.sent_tokenize(text)

for i in range(len(sentenses)):
    words = nltk.word_tokenize(sentenses[i])
    print(words)
    tokens_without_sw = [word for word in words if not word in stopwords.words()]
    print(tokens_without_sw, "\n")
