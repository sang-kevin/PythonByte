# coding=utf-8
import io

# f = open('abc.txt', 'wt', encoding='utf-8')
f = open('abc.txt', 'wt')
f.write("富强民主")
f.close()

# text = open('abc.txt',encoding='utf-8').read()
text = open('abc.txt').read()
print(text)