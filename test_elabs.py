from elevenlabs import generate, play
from elevenlabs import set_api_key as elevenlabs_set_api_key

elevenlabs_set_api_key(os.getenv("ELEVENLAB_API_KEY"))

audio = generate(
    text="¡Hola! Mi nombre es Arnold, encantado de conocerte!",
    voice="Arnold",
    model='eleven_multilingual_v1'
)

play(audio)
