.source Program.java
.class public Program
.super java/lang/Object
.field a Z
.field b I
.field c I
.field d I

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield Program.a Z
	aload_0
	iconst_1
	putfield Program.b I
	aload_0
	iconst_2
	putfield Program.c I
	aload_0
	iconst_3
	putfield Program.d I
Label1:
	return
.limit stack 3
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
.var 1 is b I from Label0 to Label1
	iconst_1
	istore_1
.var 2 is c I from Label0 to Label1
	iconst_2
	istore_2
.var 3 is d I from Label0 to Label1
	iconst_3
	istore_3
.var 4 is e Z from Label0 to Label1
	iconst_1
	istore 4
.var 5 is f Z from Label0 to Label1
	iconst_1
	istore 5
.var 6 is g Z from Label0 to Label1
	iconst_1
	istore 6
	iconst_1
	istore_3
	iconst_2
	istore_2
	iconst_3
	istore_1
	iload_3
	iload_2
	iadd
	iload_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	iload_3
	iload_2
	iadd
	iload_1
	isub
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 9
.limit locals 7
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
