.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Ljava/lang/String; from Label0 to Label1
.var 2 is b Ljava/lang/String; from Label0 to Label1
Label0:
	ldc "Nhan"
	astore_1
	ldc "Vo"
	astore_2
	aload_1
	astore_2
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_2
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
.limit locals 3
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
