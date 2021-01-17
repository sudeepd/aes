# aes
Attempt to learn AES step by step. The idea of the code is not efficiency , but the maths, and pedagogy.
So instead of using an unt8_t to represent 8 bits or a bye, I am using an array of 0 and 1

So, the 128 bit block would be an array of 128 0s and 1s

The mathematics is also simplified, and is mostly based on first principles. Polynomials are binary (base 2 variables) and are represented by an array of 0s and 1s representing the coefficients of terms. For example
```
[1,1,0,1,0,1] represents 1 * x^0 + 1 * x^1 + 0 * x^2 + 1 * x^3 + 0 * x^4 + 1 * x^5 
```
That is, the array index indicates the power of the variable, and the value represents the coefficients
