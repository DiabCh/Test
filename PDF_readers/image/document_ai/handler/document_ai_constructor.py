import os
from google.cloud import documentai_v1 as documentai
from keys import LOCATION, PROCESSOR_ID, PROJECT_ID


class Document:

    def __init__(
            self,
            filepath: str,
            mode: str) -> None:
        self.mode = mode
        self.filepath = filepath
        self.document = self.extract_data_single()
        self.entities = self.document.entities

    def extract_data_single(
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

    def __dict__(
            self) -> dict[str:str]:
        return {key.type_: key.mention_text for key in self.entities}

    def __repr__(
            self) -> list[str]:
        return [entity.type_ for entity in self.entities]

    def __len__(
            self) -> int:
        return len(self.entities)

    def __str__(
            self) -> str:
        return self.filepath.split('\\')[-1]
