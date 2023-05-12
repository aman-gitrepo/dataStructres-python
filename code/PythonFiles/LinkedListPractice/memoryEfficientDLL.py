# Normal Representation
# NULL[A]B --- A[B]C --- C[D]NULL

# Memory efficient DLL
# 
 

# Node A: npx = 0 XOR add(B) // bitwise XOR of zero and address of B 

# Node B: npx = add(A) XOR add(C) // bitwise XOR of address of A and address of C 

# Node C: npx = add(B) XOR add(D) // bitwise XOR of address of B and address of D 

# Node D: npx = add(C) XOR 0 // bitwise XOR of address of C and 0 

# npx(C) XOR add(B) 
# => (add(B) XOR add(D)) XOR add(B) // npx(C) = add(B) XOR add(D)
# => add(B) XOR add(D) XOR add(B) // a^b = b^a and (a^b)^c = a^(b^c)
# => add(D) XOR 0  // a^a = 0
# => add(D)     // a^0 = a

# A[0 xor B] B[A xor C] C[B xor D] D[C xor 0]