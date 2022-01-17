from typing import List

from pydantic import BaseModel, Field


class Matrix(BaseModel):
    """
    Metadata on fields of the response model can be specified in the instance of Field class.
    """
    row_count: int = Field(default=..., description="Number of rows of the matrix")
    col_count: int = Field(default=..., description="Number of columns of the matrix")
    values: List[List[int]] = Field(default=..., description="Actual array")
