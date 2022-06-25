.source Linked_list.java
.class public Linked_list
.super java/lang/Object
.field head LNode;
.field tail LNode;
.field size I

.method public <init>()V
.var 0 is this LLinked_list; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
	aload_0
	aconst_null
	putfield Linked_list.next LNode;
	aload_0
	iconst_0
	putfield Linked_list.data I
	aload_0
	aconst_null
	putfield Linked_list.head LNode;
	aload_0
	aconst_null
	putfield Linked_list.tail LNode;
	aload_0
	iconst_0
	putfield Linked_list.size I
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

.method public insert(LNode;)V
.var 0 is this LLinked_list; from Label0 to Label1
.var 1 is node LNode; from Label0 to Label1
Label0:
	aload_0
	getfield Linked_list/size I
	iconst_0
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_0
	aload_1
	putfield Linked_list/head LNode;
	aload_0
	aload_1
	putfield Linked_list/tail LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	iadd
	putfield Linked_list/size I
	goto Label4
Label5:
	aload_0
	getfield Linked_list/tail LNode;
	aload_1
	putfield Node/next LNode;
	aload_0
	aload_1
	putfield Linked_list/tail LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	iadd
	putfield Linked_list/size I
Label4:
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public traverse()V
.var 0 is this LLinked_list; from Label0 to Label1
Label0:
.var 1 is i I from Label0 to Label1
.var 2 is current LNode; from Label0 to Label1
	aload_0
	getfield Linked_list/head LNode;
	astore_2
	iconst_1
	istore_1
Label4:
	iconst_1
	aload_0
	getfield Linked_list/size I
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label6
	iload_1
	aload_0
	getfield Linked_list/size I
	if_icmpge Label11
	iconst_1
	goto Label12
Label11:
	iconst_0
Label12:
	ifgt Label8
	goto Label5
Label6:
	iload_1
	aload_0
	getfield Linked_list/size I
	if_icmple Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label8
Label5:
	aload_2
	getfield Node/data I
	invokestatic io/writeInt(I)V
	aload_2
	getfield Node/next LNode;
	astore_2
Label2:
	iconst_1
	aload_0
	getfield Linked_list/size I
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label7
	iload_1
	iconst_1
	isub
	istore_1
	goto Label4
Label7:
	iload_1
	iconst_1
	iadd
	istore_1
	goto Label4
Label3:
Label8:
Label1:
	return
.limit stack 17
.limit locals 3
.end method
