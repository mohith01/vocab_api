#VOCAB_API

This package has two main features:\
If given the vocabulary.com lists, it returns all the words as a python list
```py
from vocab_api import get_list
l = get_list("https://www.vocabulary.com/lists/7813867")#Insert the vocab list here
```

There is also a class called Words which contains following features:\
- word_name
- short_desc
- long_desc
- similar
