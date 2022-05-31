.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
.var 3 is c I from Label0 to Label1
.var 4 is d F from Label0 to Label1
.var 5 is e F from Label0 to Label1
.var 6 is f F from Label0 to Label1
Label0:
	bipush 10
	istore_1
	bipush 20
	istore_2
	bipush 30
	istore_3
	bipush 10
	bipush 20
	iadd
	bipush 30
	iadd
	invokestatic io/putIntLn(I)V
	ldc 10.1
	ldc 20.2
	fadd
	ldc 30.3
	fneg
	fsub
	invokestatic io/putFloatLn(F)V
	iload_1
	iload_2
	isub
	iload_3
	iconst_2
	imul
	isub
	invokestatic io/putIntLn(I)V
	ldc 10.1
	ldc 20.2
	fadd
	ldc 30.3
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 8
.limit locals 7
.end method

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
