.source Program.java
.class public Program
.super java/lang/Object
.field static $a F
.field b F

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc 3.42
	putfield Program.b F
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	ldc 1.2
	putstatic Program.$a F
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public func()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	getstatic Program/$a F
	aload_0
	getfield Program/b F
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is obj LProgram; from Label0 to Label1
	new Program
	dup
	invokespecial Program/<init>()V
	astore_1
	aload_1
	invokevirtual Program/func()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
