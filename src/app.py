import logging
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .modules.data_models import Message, RequestSentense, ResponsePrediction


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


@app.post(
    "/predict", 
    response_model=ResponsePrediction, 
    responses={**global_responses}
)
def predict(request_sentense: RequestSentense):
    try:
        logger.info(f"RequestSentense: {request_sentense}")
        ...
    
    except Exception as exception:
        logger.exception(str(exception))
        return JSONResponse(
            status_code=500, content={"message": "Internal Server Error"}
        )
        
    else:
        response_prediction = ResponsePrediction(predicted_class="positive")
        logger.info(f"ResponsePrediction: {response_prediction}")
        return response_prediction
