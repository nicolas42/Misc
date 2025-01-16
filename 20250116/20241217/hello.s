;; HelloWorld: HelloWorld.o
;; 	ld -o HelloWorld HelloWorld.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _start -arch arm64 

;; HelloWorld.o: HelloWorld.s
;; 	as -arch arm64 -o HelloWorld.o HelloWorld.s

;; as -arch arm64 -o hello.o hello.s && ld -o hello hello.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _start -arch arm64 

	.global _start
	.align 4

_start:	mov 	X0, #1
	adr 	X1, helloworld
	mov 	X2, #13
	mov	X16, #4
	svc 	#0x80

	mov 	X0, #0
	mov 	X16, #1

	svc 	#0x80

helloworld:		.ascii "Hello World!\n"

	
