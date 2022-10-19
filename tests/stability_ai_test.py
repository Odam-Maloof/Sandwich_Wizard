

'''
import io
import os
import warnings

from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# NB: host url is not prepended with \"https\" nor does it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# To get your API key, visit https://beta.dreamstudio.ai/membership
os.environ['STABILITY_KEY'] = 'sk-8gIxTQZBAfYIHEQ1FXaCrsAhRulKPWXE33OOWA9enq8dnd9Y'



stability_api = client.StabilityInference(
    key = os.environ['STABILITY_KEY'], 
    verbose = True,
)
# the object returned is a python generator
answers = stability_api.generate(
    prompt = "cat sitting on the moon, pencil drawing"
)

# iterating over the generator produces the api response
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            print('failed')
        if artifact.type == generation.ARTIFACT_IMAGE:
            print('success')
            img = Image.open(io.BytesIO(artifact.binary))
            display(img)'''