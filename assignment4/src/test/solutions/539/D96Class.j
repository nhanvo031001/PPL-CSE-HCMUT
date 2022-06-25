.source D96Class.java
.class public D96Class
.super java/lang/Object
.field static $a Z
.field static final $b Z

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
	iconst_0
	putstatic D96Class.$a Z
	iconst_1
	putstatic D96Class.$b Z
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public func()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	getstatic D96Class/$a Z
	getstatic D96Class/$b Z
	ior
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 2
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
