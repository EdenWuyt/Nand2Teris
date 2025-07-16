// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//  compute the product R0*R1 and store the result to R2
//  base=R0, n=R1, i=1, sum=0
//  for (i=1); i<=n; i++) {
//    sum = sum + base }
//  assume that R0 ≥ 0, R1 ≥ 0, and R0 * R1 < 32768

    @i          // i=1
    M=1

    @sum        // sum=0
    M=0

    @R0         // base=R0 (if base==0, goto STOP)
    D=M
    @base
    M=D
    @STOP
    D;JEQ

    @R1          // n=R1 (if n==0, goto STOP)
    D=M
    @n
    M=D
    @STOP
    D;JEQ


(LOOP)
    @i           // if (i-n) > 0, goto STOP
    D=M
    @n
    D=D-M
    @STOP
    D;JGT

    @sum         // sum=sum+base
    D=M
    @base
    D=D+M
    @sum
    M=D

    @i            // i++
    M=M+1

    @LOOP
    0;JMP

(STOP)
    @sum          // R2=sum
    D=M
    @R2
    M=D
    @END
    0;JMP         // go to END

(END)
    @END
    0;JMP         // go to END
    
    

    
  