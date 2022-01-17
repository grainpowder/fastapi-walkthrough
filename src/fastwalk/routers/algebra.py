from fastapi import APIRouter, Body, HTTPException, status

from fastwalk.services.algebra import *

ROUTER_PREFIX = "/algebra"
router = APIRouter(prefix=ROUTER_PREFIX, tags=["algebra"])


@router.post(
    path="/determinant",
    status_code=status.HTTP_200_OK,
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
    if not is_row_count_valid(matrix):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"row_count({matrix.row_count}) doesn't match length of values({len(matrix.values)})"
        )
    elif not are_columns_valid(matrix):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Number of elements in each of rows are not same or one of elements is empty"
        )
    elif matrix.row_count != matrix.col_count:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Can't calculate determinant of non-square matrix of shape ({matrix.row_count}, {matrix.col_count})"
        )
    return calculate_determinant(matrix)
