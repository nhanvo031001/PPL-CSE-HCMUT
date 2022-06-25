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
	iconst_1
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	iconst_1
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	ineg
	isub
	invokestatic io/putIntLn(I)V
	iconst_3
	iconst_2
	irem
	iconst_1
	isub
	invokestatic io/putIntLn(I)V
	iconst_4
	iconst_2
	irem
	iconst_1
	isub
	invokestatic io/putInt(I)V
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
