from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

answer = pieces_client.update_conversation_name(
    conversation_id='17c6883e-10e6-4c6b-b37e-cd6fff615aca')

print(answer)