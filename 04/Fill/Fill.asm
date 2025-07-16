// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// while True: {
//   i=0, n=8192, addr=screen
//   if (key == 0) {
//     for (i=0; i<n; i++) {
//       memory[addr] = 0
//       address ++;
//   }} else {
//     for (i=0; i<n; i++) {
//       memory[addr] = -1
//   }}

(LOOP)
  @i        // i=0
  M=0

  @8192     // n=8192
  D=A
  @n
  M=D

  @SCREEN   // addr = SCREEN (store the current address as a variable = pointer)
  D=A
  @addr
  M=D

  @KBD      // get keyboard input
  D=M

  @NOTPRESSED  // if keyboard is not pressed, goto NOTPRESSED
  D;JEQ

  @PRESSED     // else, goto PRESSES
  0;JMP

(NOTPRESSED)   
  @i           // if i-n >=0, goto LOOP
  D=M
  @n
  D=D-M
  @LOOP
  D;JGE

  @addr           // memory[addr] = 0; addr++
  A=M
  M=0
  @addr
  M=M+1

  @i         // i++;
  M=M+1
  @NOTPRESSED
  0;JMP

(PRESSED)
  @i           // if i-n >=0, goto LOOP
  D=M
  @n
  D=D-M
  @LOOP
  D;JGE     

  @addr           // memory[addr] = -1; addr++
  A=M
  M=-1
  @addr
  M=M+1

  @i         // i++;
  M=M+1
  @PRESSED
  0;JMP