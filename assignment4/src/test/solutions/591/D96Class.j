.source D96Class.java
.class public D96Class
.super java/lang/Object

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
Label1:
	return
.limit stack 0
.limit locals 1
.end method

.method public func()V
.var 0 is this LD96Class; from Label0 to Label1
Label0:
	iconst_0
	ifgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifgt Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifgt Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifgt Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifgt Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifgt Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifgt Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifgt Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	ifgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	invokestatic io/putBoolLn(Z)V
	iconst_0
	ifgt Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifgt Label26
	iconst_1
	goto Label27
Label26:
	iconst_0
Label27:
	ifgt Label28
	iconst_1
	goto Label29
Label28:
	iconst_0
Label29:
	ifgt Label30
	iconst_1
	goto Label31
Label30:
	iconst_0
Label31:
	ifgt Label32
	iconst_1
	goto Label33
Label32:
	iconst_0
Label33:
	ifgt Label34
	iconst_1
	goto Label35
Label34:
	iconst_0
Label35:
	ifgt Label36
	iconst_1
	goto Label37
Label36:
	iconst_0
Label37:
	ifgt Label38
	iconst_1
	goto Label39
Label38:
	iconst_0
Label39:
	ifgt Label40
	iconst_1
	goto Label41
Label40:
	iconst_0
Label41:
	ifgt Label42
	iconst_1
	goto Label43
Label42:
	iconst_0
Label43:
	ifgt Label44
	iconst_1
	goto Label45
Label44:
	iconst_0
Label45:
	ifgt Label46
	iconst_1
	goto Label47
Label46:
	iconst_0
Label47:
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 72
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
