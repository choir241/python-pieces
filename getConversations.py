from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

answer = pieces_client.get_conversations()

print(answer)