import logging
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .modules.data_models import Message, RequestSentence, ResponsePrediction
from .modules.ml_models import ModelInference


logging.basicConfig(
    format="%(asctime)s ~ %(levelname)s ~ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

global_responses = {
    500: {"description": "Internal Server Error", "model": Message},
}

app = FastAPI()
app.model_inference = ModelInference()


@app.post(
    "/predict", 
    response_model=ResponsePrediction, 
    responses={**global_responses}
)
def predict(request_sentense: RequestSentence):
    try:
        logger.info(f"RequestSentence: {request_sentense}")
        negative_percent, positive_percent = app.model_inference(
            request_sentense.text
        )
        response_prediction = ResponsePrediction(
            positive_percent=positive_percent,
            negative_percent=negative_percent,
        )
        logger.info(f"ResponsePrediction: {response_prediction}")
        return response_prediction
    
    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )
    
        
