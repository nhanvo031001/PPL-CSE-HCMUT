.source D96Class.java
.class public D96Class
.super java/lang/Object

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

.method public static <clinit>()V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public func()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	iconst_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iconst_0
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	iand
	iconst_0
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iconst_0
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	iand
	ior
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 19
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
.var 1 is obj LD96Class; from Label0 to Label1
	new D96Class
	dup
	invokespecial D96Class/<init>()V
	astore_1
	aload_1
	invokevirtual D96Class/func()V
Label1:
	return
.limit stack 2
.limit locals 2
.end method
