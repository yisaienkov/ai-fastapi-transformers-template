from typing import Tuple

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch


class ModelInference():
    def __init__(self):
        """Initialize.
        """
        model_name = "distilbert-base-uncased-finetuned-sst-2-english"

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def __call__(self, input_sentence: str) -> Tuple[float, float]:
        """Create prediction for one text

        Parameters
        ----------
        input_sentence : str
            The input text

        Returns
        -------
        Tuple[float, float]
            Negative and positive percentages of the prediction
        """
        tokenized = self.tokenizer(
            [input_sentence],
            padding=True,
            truncation=True,
            max_length=512,
            return_tensors="pt"
        )
        outputs = self.model(**tokenized).logits

        return tuple(torch.softmax(outputs, dim=1).tolist()[0])