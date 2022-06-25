.source D96Class.java
.class public D96Class
.super java/lang/Object
.field c Z
.field d Ljava/lang/String;

.method public <init>()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield D96Class.c Z
	aload_0
	ldc "Nhan"
	putfield D96Class.d Ljava/lang/String;
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
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	aload_0
	getfield D96Class/c Z
	invokestatic io/putBoolLn(Z)V
	aload_0
	getfield D96Class/d Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
