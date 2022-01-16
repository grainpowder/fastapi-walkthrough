from fastapi import APIRouter, Path, Query

from fastwalk.services.arithmetic import *

ROUTER_PREFIX = "/arithmetic"
router = APIRouter(prefix=ROUTER_PREFIX, tags=["arithmetic"])


@router.get(
    path="/plus-int/{a}/{b}",
    summary="Simple plus operation on integers",
    response_description="String that states 'a plus b is a + b'",
)
async def add_integers(a: int, b: int):
    """
    You can add detailed description on this endpoint in markdown format to be displayed in swagger.
    As type of a and b is specified, Pydantic will validate the type of input that client has passed.
    If type of input is invalid, response will be 422 error: Unprocessable Entity

    - **a** : first operand
    - **b** : second operand
    """
    return f"{a} + {b} = {a + b}"


@router.get(
    path="/{operator}/{data_type}",
    summary="Any arithmetic operations on int or float"
)
async def call_operate_anything(
        operator: ArithmeticOperator,
        a: Union[int, float],
        data_type: OperandDataType = Path(...),  # as in typer, '...' means that the argument is required, not optional
        b: Union[int, float] = Query(...)
):
    """
    Document says: function parameters that are not part of the path parameters are understood as query parameters.
    Of course, there are ways to tell FastAPI explicitly that a parameter is path variable or query parameter.
    Set default value of the method as an instance of Path or Query class.

    However, when to use which? Medium post "When Should You Use Path Variable and Query Parameter?" says:
    - If you want to identify a resource in a path, use path variable.
    - Otherwise(ex. use value as a parameter of a query or certain operation), use query parameters.
    """
    if type(a) != type(b):
        # TODO : raise custom error to deliver specific message
        pass
    elif (isinstance(a, int) and data_type == OperandDataType.FLOAT) or \
            (isinstance(a, float) and data_type == OperandDataType.INTEGER):
        pass
    return await operate_anything(operator, data_type, a, b)
