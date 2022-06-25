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
.var 1 is i I from Label0 to Label1
	iconst_1
	istore_1
Label4:
	iconst_1
	iconst_5
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label6
	iload_1
	iconst_5
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label8
	goto Label5
Label6:
	iload_1
	iconst_5
	if_icmple Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label8
Label5:
	iload_1
	invokestatic io/putInt(I)V
Label2:
	iconst_1
	iconst_5
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label7
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label8:
Label1:
	return
.limit stack 17
.limit locals 2
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
