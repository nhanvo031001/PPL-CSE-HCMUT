.source Program.java
.class public Program
.super java/lang/Object
.field a Ljava/lang/String;
.field b Ljava/lang/String;

.method public <init>()V
.var 0 is this LProgram; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	ldc "string 1"
	putfield Program.a Ljava/lang/String;
	aload_0
	ldc "string 2"
	putfield Program.b Ljava/lang/String;
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
.var 0 is this LProgram; from Label0 to Label1
Label0:
.var 1 is a Ljava/lang/String; from Label0 to Label1
	ldc "string 3"
	astore_1
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
