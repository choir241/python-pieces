---
layout: article
title: SDKs
description: Get started with Appwrite SDKs and learn how to use them to add authentication, user management, file storage, and more to your apps.
---

from pieces_os_client.wrapper import PiecesClient
from pieces_os_client import FragmentMetadata

# Replace 'your_base_url' with the base URL of your Pieces OS server
pieces_client = PiecesClient(config={'baseUrl': 'your_base_url'})

# Set the content and metadata for the new asset
content = "print('Hello, World!')"
metadata = FragmentMetadata(ext="ClassificationSpecificEnum.PY") # optional metadata

# Create the new asset using the content and metadata
new_asset_id = pieces_client.create_asset(content, metadata)

print(f"Created asset with ID: {new_asset_id}")
