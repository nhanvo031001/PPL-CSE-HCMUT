.source D96Class.java
.class public D96Class
.super java/lang/Object
.field a I
.field b I
.field c I
.field d F
.field e F
.field f F

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	bipush 10
	putfield D96Class.a I
	aload_0
	bipush 20
	putfield D96Class.b I
	aload_0
	bipush 30
	putfield D96Class.c I
	aload_0
	ldc 10.1
	putfield D96Class.d F
	aload_0
	ldc 20.2
	putfield D96Class.e F
	aload_0
	ldc 30.3
	putfield D96Class.f F
Label1:
	return
.limit stack 2
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
.var 1 is a I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is b I from Label0 to Label1
	bipush 20
	istore_2
.var 3 is c I from Label0 to Label1
	bipush 30
	istore_3
.var 4 is d F from Label0 to Label1
	ldc 10.1
	fstore 4
.var 5 is e F from Label0 to Label1
	ldc 20.2
	fstore 5
.var 6 is f F from Label0 to Label1
	ldc 30.3
	fstore 6
	aload_0
	getfield D96Class/a I
	aload_0
	getfield D96Class/b I
	iadd
	aload_0
	getfield D96Class/c I
	iadd
	invokestatic io/putIntLn(I)V
	aload_0
	getfield D96Class/d F
	aload_0
	getfield D96Class/e F
	fadd
	aload_0
	getfield D96Class/f F
	fneg
	fsub
	invokestatic io/putFloatLn(F)V
	iload_1
	iload_2
	isub
	iload_3
	iconst_2
	imul
	isub
	invokestatic io/putIntLn(I)V
	fload 4
	fload 5
	fadd
	fload 6
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 3
.limit locals 7
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
