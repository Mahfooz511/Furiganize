from pyahooapis import jlp

appid = 'dj00aiZpPW5DVGVLZW9aYzRjdiZzPWNvbnN1bWVyc2VjcmV0Jng9YmU-'
api = jlp.JLPAPIs(appid)
sentence = '澱んだ街角で僕らは出会った'

chunks = api.da.get_chunks(sentence)

for chunk in chunks:
    print('%s -> %s ') % (chunk, chunks[chunk.dependency] if chunk.dependency != -1 else None)