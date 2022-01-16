from enum import Enum


class ArithmeticOperator(str, Enum):
    PLUS = "plus"
    MINUS = "minus"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


class OperandDataType(str, Enum):
    INTEGER = "int"
    FLOAT = "float"


OPERATOR_SIGN = {
    "plus": "+",
    "minus": "-",
    "multiply": "x",
    "divide": "/"
}
