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
.var 1 is a F from Label0 to Label1
	ldc 1.0
	fstore_1
	fload_1
	fneg
	invokestatic io/putFloatLn(F)V
	ldc 2.0
	fstore_1
	fload_1
	ldc 2.0
	fmul
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 2
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
