"""
Models.
"""
from typing import List, Union

from pydantic import BaseModel, Field


class RequestSentence(BaseModel):
    text: str


class ResponsePrediction(BaseModel):
    positive_percent: float
    negative_percent: float


class Message(BaseModel):
    message: str
