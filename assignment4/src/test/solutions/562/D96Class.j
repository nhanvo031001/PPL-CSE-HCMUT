.source D96Class.java
.class public D96Class
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Ljava/lang/String; from Label0 to Label1
.var 2 is b Ljava/lang/String; from Label0 to Label1
.var 3 is c Z from Label0 to Label1
.var 4 is d Z from Label0 to Label1
Label0:
	ldc "string 1"
	astore_1
	ldc "string 2"
	astore_2
	iconst_0
	istore_3
	iconst_1
	istore 4
	aload_1
	invokestatic io/putStringLn(Ljava/lang/String;)V
	ldc "string 1"
	invokestatic io/putStringLn(Ljava/lang/String;)V
	iconst_0
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
.limit stack 10
.limit locals 5
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
