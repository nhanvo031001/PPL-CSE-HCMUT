.source D96Class.java
.class public D96Class
.super java/lang/Object
.field a Ljava/lang/String;
.field b Ljava/lang/String;
.field c Z
.field d Z

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc "string 1"
	putfield D96Class.a Ljava/lang/String;
	aload_0
	ldc "string 2"
	putfield D96Class.b Ljava/lang/String;
	aload_0
	iconst_0
	putfield D96Class.c Z
	aload_0
	iconst_1
	putfield D96Class.d Z
Label1:
	return
.limit stack 4
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
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "string 1"
	astore_1
.var 2 is b Ljava/lang/String; from Label0 to Label1
	ldc "string 2"
	astore_2
.var 3 is c Z from Label0 to Label1
	iconst_0
	istore_3
.var 4 is d Z from Label0 to Label1
	iconst_1
	istore 4
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield D96Class/a Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield D96Class/c Z
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBoolLn(Z)V
	iload 4
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 9
.limit locals 5
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
