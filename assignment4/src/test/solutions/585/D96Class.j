.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
.var 2 is c I from Label0 to Label1
.var 3 is d I from Label0 to Label1
.var 4 is e Z from Label0 to Label1
.var 5 is f Z from Label0 to Label1
.var 6 is g Z from Label0 to Label1
Label0:
	iconst_1
	istore_1
	iconst_2
	istore_2
	iconst_3
	istore_3
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
.limit stack 4
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
