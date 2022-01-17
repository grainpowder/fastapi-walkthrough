from fastapi import APIRouter, Body

from fastwalk.services.algebra import *

ROUTER_PREFIX = "/algebra"
router = APIRouter(prefix=ROUTER_PREFIX, tags=["algebra"])


@router.post(
    path="/determinant",
    summary="Calculate determinant of a matrix",
    response_description="Determinant of input matrix"
)
async def call_calculate_determinant(
        matrix: Matrix = Body(
            ...,
            example={
                "row_count": 3,
                "col_count": 3,
                "values": [[2, 0, 0], [0, 7, 0], [0, 0, 3]]
            }
        )
) -> float:
    """
    Like Path, Query of path variable and query parameter, metadata on response model can be specified in Body instance.

    * matrix : Square matrix whose determinant will be calculated
    """
    if is_matrix_valid(matrix):
        # TODO : make custom error message
        pass
    elif not matrix.row_count != matrix.col_count:
        pass
    return calculate_determinant(matrix)
