from pieces_copilot_sdk import PiecesClient

pieces_client = PiecesClient(config={'baseUrl': 'http://localhost:1000'})

new_conversation = pieces_client.create_conversation(
    props={
        "name": "Test Conversation",
        "firstMessage": "Hello, how can I use the API?"
    }
)

print(new_conversation)