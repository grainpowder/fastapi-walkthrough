from typing import Union

from fastwalk.models.arithmetic import *


async def operate_anything(
        operator: ArithmeticOperator,
        data_type: OperandDataType,
        a: Union[int, float],
        b: Union[int, float]
) -> str:
    sign = OPERATOR_SIGN[operator]
    operation_result = 0
    if operator == ArithmeticOperator.PLUS:
        operation_result += a + b
    elif operator == ArithmeticOperator.MINUS:
        operation_result += a - b
    elif operator == ArithmeticOperator.MULTIPLY:
        operation_result += a * b
    elif operator == ArithmeticOperator.DIVIDE:
        operation_result += a / b

    if data_type == OperandDataType.INTEGER:
        return f"{a} {sign} {b} = {operation_result}"
    elif data_type == OperandDataType.FLOAT:
        return f"{a:.4f} {sign} {b:.4f} = {operation_result:.4f}"
    else:
        return ""  # This cannot be called since Pydantic will invalidate the input, but added to complete method
