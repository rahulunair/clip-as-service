from docarray import DocumentArray

da = DocumentArray.pull('ttl-original', show_progress=True, local_cache=True)


from clip_client import Client

c = Client(server='grpc://0.0.0.0:51000')

da = c.encode(da, show_progress=True)

while True:
    vec = c.encode([input('sentence> ')])
    r = da.find(query=vec, limit=9)
    r[0].plot_image_sprites()
