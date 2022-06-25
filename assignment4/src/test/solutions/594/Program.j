.source Program.java
.class public Program
.super java/lang/Object
.field a Z
.field static $a Z

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	iconst_0
	putfield Program.a Z
Label1:
	return
.limit stack 3
.limit locals 1
.end method

.method public static <clinit>()V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_1
	putstatic Program.$a Z
Label1:
	return
.limit stack 2
.limit locals 1
.end method

.method public func()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	getfield Program/a Z
	getstatic Program/$a Z
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	if_icmpeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 8
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
