from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

answer = pieces_client.prompt_conversation(
    message='Hello, world!',
    conversation_id='17c6883e-10e6-4c6b-b37e-cd6fff615aca',
    regenerate_conversation_name=False,
)

print(answer)