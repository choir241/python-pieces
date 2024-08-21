from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

response = pieces_client.ask_question("What is Pieces for Developers?")

print(response)