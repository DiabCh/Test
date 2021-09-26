import os
from google.cloud import documentai_v1 as documentai
from keys import LOCATION, PROCESSOR_ID, PROJECT_ID

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'dandsltd-dev-e0c5251c5ebd.json'


class Document:

    def __init__(
            self,
            filepath: str) -> None:

        self.filepath = filepath
        self.document = self.quickstart()
        self.entities = self.document.entities

    def quickstart(
            self) -> documentai.Document:
        client = documentai.DocumentProcessorServiceClient()

        name = f"projects/{PROJECT_ID}/locations/{LOCATION}" \
               f"/processors/{PROCESSOR_ID}"

        # Read the file into memory
        with open(self.filepath, "rb") as image:
            image_content = image.read()

        document = {"content": image_content, "mime_type": "application/pdf"}

        # Configure the process request
        request = {"name": name, "raw_document": document}

        result = client.process_document(request)
        document = result.document
        return document

    def dict_from_entities(
            self) -> dict[str:str]:
        return {key.type_: key.mention_text for key in self.entities}

    def __repr__(
            self) -> list[str]:
        return [entity.type_ for entity in self.entities]

