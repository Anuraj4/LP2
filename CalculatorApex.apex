public class Calculator {
    // Class Member variables
    public Decimal operand1;
    public Decimal operand2;

    // Constructor
    public Calculator(Decimal op1, Decimal op2) {
        operand1 = op1;
        operand2 = op2;
    }

    // Addition method
    public Decimal add() {
        return operand1 + operand2;
    }

    // Subtraction method
    public Decimal subtract() {
        return operand1 - operand2;
    }

    // Multiplication method
    public Decimal multiply() {
        return operand1 * operand2;
    }

    // Division method
    public Decimal divide() {
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

