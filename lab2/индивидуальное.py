words = ("кирпич", "апельсин", "черемша", "яблоко", "ананас", "дом", "машина", "a", "дом", "окунь")

volwes = "aeiouаеёиоуыэюя"

def count(word):
  k=0
  for i in range(len(word)):
    if word[i] in volwes:
      k+=1
  return k

def sort_key(word):
  return (-count(word), len(word))

filtred=[]
for w in words:
  if w[0] in volwes:
    filtred.append(w.lower())

swapped=[]
for i in filtred:
  if len(i) > 1:
    swapped.append(i[-1]+i[1:-1]+i[0])
  else: swapped.append(i)

swapped.sort(key=sort_key)

res="-".join(swapped)
print(res)

longest=words[0]
for i in words:
  if len(longest) < len(i):
    longest=i
print(longest[1:-1])