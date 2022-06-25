.source Program.java
.class public Program
.super java/lang/Object

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
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
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
.var 2 is b F from Label0 to Label1
	ldc 2.0
	fstore_2
.var 3 is c F from Label0 to Label1
	ldc 10.0
	fstore_3
.var 4 is d F from Label0 to Label1
	ldc 20.0
	fstore 4
	fload_1
	fneg
	fload_2
	fsub
	fload_3
	fsub
	fload 4
	fsub
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
.limit locals 5
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
