"""
Models.
"""
from typing import List, Union

from pydantic import BaseModel


class RequestSentense(BaseModel):
    text: str


class ResponsePrediction(BaseModel):
    predicted_class: str


class Message(BaseModel):
    message: str
