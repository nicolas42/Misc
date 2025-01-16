// hello.s
.global _start        // Make start symbol global
.align 2             // Align to 2^2 (4) bytes

_start:
    // Setup parameters for write syscall
    mov x0, #1       // File descriptor 1 is stdout
    adr x1, message  // Load address of message
    mov x2, #14      // Message length
    mov x16, #4      // MacOS write syscall number
    svc #0x80        // Make system call

    // Setup parameters for exit syscall
    mov x0, #0       // Return code 0
    mov x16, #1      // MacOS exit syscall number
    svc #0x80        // Make system call

message:
    .ascii "Hello, ARM64!\n"
