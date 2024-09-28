from pydantic import BaseModel

class Cropdata(BaseModel):

    N: int
    P : int
    K : int
    Temperatura: float
    Humedad : float
    PH : float
    Rainfall : float
