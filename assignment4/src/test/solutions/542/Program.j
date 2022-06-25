.source Program.java
.class public Program
.super java/lang/Object
.field static $a I
.field b F
.field c Ljava/lang/String;
.field d Z

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc 3.2
	putfield Program.b F
	aload_0
	ldc "Class"
	putfield Program.c Ljava/lang/String;
	aload_0
	iconst_0
	putfield Program.d Z
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static <clinit>()V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic Program.$a I
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public func()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	getstatic Program/$a I
	ineg
	invokestatic io/putIntLn(I)V
	aload_0
	getfield Program/b F
	fneg
	invokestatic io/putFloatLn(F)V
	aload_0
	getfield Program/c Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_0
	getfield Program/d Z
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 4
.limit locals 1
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
