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

.method public delete(I)V
.var 0 is this LLinked_list; from Label0 to Label1
.var 1 is data I from Label0 to Label1
Label0:
.var 2 is i I from Label0 to Label1
.var 3 is current LNode; from Label0 to Label1
	aload_0
	getfield Linked_list/head LNode;
	astore_3
	aload_3
	getfield Node/data I
	iload_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label5
	aload_0
	aload_0
	getfield Linked_list/head LNode;
	getfield Node/next LNode;
	putfield Linked_list/head LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	putfield Linked_list/size I
	return
	goto Label4
Label5:
Label4:
	iconst_1
	istore_2
Label8:
	iconst_1
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifgt Label10
	iload_2
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	if_icmpge Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
	ifgt Label12
	goto Label9
Label10:
	iload_2
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	if_icmple Label17
	iconst_1
	goto Label18
Label17:
	iconst_0
Label18:
	ifgt Label12
Label9:
	aload_3
	getfield Node/next LNode;
	getfield Node/data I
	iload_1
	if_icmpne Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label22
	aload_3
	aload_3
	getfield Node/next LNode;
	getfield Node/next LNode;
	putfield Node/next LNode;
	aload_0
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	putfield Linked_list/size I
	iload_2
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	if_icmpne Label23
	iconst_1
	goto Label24
Label23:
	iconst_0
Label24:
	ifle Label26
	aload_0
	aload_3
	putfield Linked_list/tail LNode;
	goto Label25
Label26:
Label25:
	return
	goto Label21
Label22:
	aload_3
	getfield Node/next LNode;
	astore_3
Label21:
Label6:
	iconst_1
	aload_0
	getfield Linked_list/size I
	iconst_1
	isub
	if_icmpge Label27
	iconst_1
	goto Label28
Label27:
	iconst_0
Label28:
	ifgt Label11
	iload_2
	iconst_1
	isub
	istore_2
	goto Label8
Label11:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label8
Label7:
Label12:
Label1:
	return
.limit stack 29
.limit locals 4
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
