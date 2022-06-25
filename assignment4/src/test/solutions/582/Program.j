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
	iconst_0
	iconst_1
	iand
	iconst_0
	ior
	iconst_1
	aload_0
	getfield Program/a Z
	iand
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	aload_0
	getfield Program/b I
	aload_0
	getfield Program/c I
	iadd
	aload_0
	getfield Program/d I
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBoolLn(Z)V
	iload_1
	iload_2
	iadd
	iload_3
	if_icmpeq Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 17
.limit locals 4
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
