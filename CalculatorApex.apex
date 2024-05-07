public class Calculator {
    // Class Member variables
    public Double operand1;
    public Double operand2;

    // Constructor
    public Calculator(Double op1, Double op2) {
        operand1 = op1;
        operand2 = op2;
    }

    // Addition method
    public Double add() {
        return operand1 + operand2;
    }

    // Subtraction method
    public Double subtract() {
        return operand1 - operand2;
    }

    // Multiplication method
    public Double multiply() {
        return operand1 * operand2;
    }

    // Division method
    public Double divide() {
        if (operand2 != 0) {
            return operand1 / operand2;
        } else {
            // Handling division by zero error
            System.debug('Error: Division by zero');
            return null;
        }
    }
}

Calculator calc = new Calculator(10.0, 5.0);
System.debug('Addition: ' + calc.add());       // Output: 15.0
System.debug('Subtraction: ' + calc.subtract());  // Output: 5.0
System.debug('Multiplication: ' + calc.multiply()); // Output: 50.0
System.debug('Division: ' + calc.divide());     // Output: 2.0
