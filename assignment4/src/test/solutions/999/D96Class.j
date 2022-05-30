.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b F from Label0 to Label1
.var 3 is e I from Label0 to Label1
.var 4 is f F from Label0 to Label1
Label0:
	iconst_1
	istore_1
	ldc 2.2
	fstore_2
	iload_1
	invokestatic io/writeIntLn(I)V
	fload_2
	invokestatic io/writeFloatLn(F)V
	ldc "Nhan Vo"
	invokestatic io/writeStrLn(Ljava/lang/String;)V
	iconst_0
	invokestatic io/writeBoolLn(Z)V
	bipush 100
	ineg
	invokestatic io/writeIntLn(I)V
	ldc 200.2
	invokestatic io/writeFloatLn(F)V
	bipush 100
	ineg
	iload_1
	iadd
	invokestatic io/writeIntLn(I)V
	bipush 100
	iconst_2
	imul
	invokestatic io/writeIntLn(I)V
	ldc 3.0
	ldc 2.0
	fdiv
	invokestatic io/writeFloatLn(F)V
Label1:
	return
.limit stack 10
.limit locals 5
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
