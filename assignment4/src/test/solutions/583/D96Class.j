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
	iconst_0
	iconst_1
	iand
	iconst_0
	ior
	iconst_1
	iconst_1
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	iand
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	iconst_1
	iconst_2
	iadd
	iconst_3
	if_icmpne Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	iconst_1
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	if_icmpne Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	invokestatic io/putBoolLn(Z)V
	iload_1
	iload_2
	iadd
	iload_3
	if_icmpeq Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	iconst_1
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 36
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
