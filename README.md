# Simplecalculator
Simplecalculator is a Python library for making basic calculations including addition, subtraction, multiplication, division and finding the nth root of a number.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install simplecalculator.

```bash
!pip install git+https://github.com/adeyinkaoresanya/simplecalculator.git
```

## Usage

```python
from simplecalculator import Calculator

calculator = Calculator()
# returns the result of the addition operation
calculator.add()

# returns the result of the subtraction operation
calculator.subtract()

# returns the result of the multiplication operation
calculator.multiply()

# returns the result of the division operation
calculator.divide(num)

# returns the result of the nth root
calculator.nth_root(root, num= None)

# resets the memory of the calculator
calculator.reset()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
