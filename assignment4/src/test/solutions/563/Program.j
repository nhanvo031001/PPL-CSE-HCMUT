.source Program.java
.class public Program
.super java/lang/Object
.field a I
.field b I
.field c I

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 100
	putfield Program.a I
	aload_0
	sipush 200
	putfield Program.b I
	aload_0
	sipush 300
	putfield Program.c I
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public static <clinit>()V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public func()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
.var 1 is a I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is b I from Label0 to Label1
	bipush 20
	istore_2
.var 3 is c I from Label0 to Label1
	bipush 30
	istore_3
	iload_1
	invokestatic io/putInt(I)V
	iload_2
	invokestatic io/putInt(I)V
	iload_3
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 1
.limit locals 4
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
