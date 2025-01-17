const derivative = (f, x, num, h = 1e-7) => {
  //Calculate derivative using central difference method"""
  try {
    return (f(x + h, num) - f(x - h, num)) / (2 * h);
  } catch {
    return float("inf");
  }
};

function exponential(x, pow) {
  //"""Calculate x^pow"""
  return Math.pow(x, pow);
}

function constant(x) {
  return x;
}

// Test points
x_values = [0, 1, 2, 3];
h = 0.0001;

for (var i = 0; i < x_values.length; i++) {
  numerical_deriv = Math.round(derivative(exponential, x_values[i], 3));
  console.log(`x=${x_values[i]}:`);
  console.log(`  Numerical derivative: ${numerical_deriv}`);
}
