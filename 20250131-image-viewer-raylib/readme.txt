Compile in macos
clang -framework CoreVideo -framework IOKit -framework Cocoa -framework GLUT -framework OpenGL libraylib.a -Iraylib/src main.c && ./a.out

I built raylib as a static library in macos using this guide from https://github.com/raysan5/raylib/wiki/Working-on-macOS.  There should be a make-raylib.sh file which has the commands.


gcc -I /opt/homebrew/Cellar/raylib/5.5/include -L /opt/homebrew/Cellar/raylib/5.5/lib -l raylib main.c
