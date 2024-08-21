from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

answer = pieces_client.get_conversation(
    conversation_id='17c6883e-10e6-4c6b-b37e-cd6fff615aca',
    include_raw_messages=False
)

print(answer)