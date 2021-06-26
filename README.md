# VOCAB_API

This package has two main features:\
If given the vocabulary.com lists, it returns all the words as a python list
```py
from vocab_api import get_list
l = get_list("https://www.vocabulary.com/lists/7813867")#Insert the vocab list here
print(l)
```

There is also a class called Words which contains following features:\
- word_name
- short_desc
- long_desc
- similar

```py
from vocab_api import Word
w = Word("callow")
print(w.as_dict())
```
![image](https://user-images.githubusercontent.com/42903811/123502310-13fa1a00-d669-11eb-8242-00b5621f0b70.png)

I have used html because it would be easy to push into anki. If you \
want text then you can use bs4 text property\
In the above case if i want my short_desc to be in text:
```py
dict1 = w.as_dict()
dict1['short_desc'][0].text
```
would solve the issue
