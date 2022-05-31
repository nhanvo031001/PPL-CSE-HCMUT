.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_0
	bipush 9
	iadd
	bipush 9
	isub
	iconst_1
	iadd
	iconst_1
	iconst_0
	iadd
	iconst_0
	isub
	iconst_1
	isub
	iconst_1
	iadd
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 3
.limit locals 1
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
