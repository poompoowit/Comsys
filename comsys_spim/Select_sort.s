	.file	"Select_sort.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"Enter number of elements"
.LC1:
	.string	"%d"
.LC2:
	.string	"Enter %d integers\n"
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align 8
.LC3:
	.string	"Sorted list in ascending order:"
	.section	.rodata.str1.1
.LC4:
	.string	"%d\n"
	.section	.text.unlikely,"ax",@progbits
.LCOLDB5:
	.section	.text.startup,"ax",@progbits
.LHOTB5:
	.p2align 4,,15
	.globl	main
	.type	main, @function
main:
.LFB23:
	.cfi_startproc
	pushq	%r12
	.cfi_def_cfa_offset 16
	.cfi_offset 12, -16
	pushq	%rbp
	.cfi_def_cfa_offset 24
	.cfi_offset 6, -24
	movl	$.LC0, %edi
	pushq	%rbx
	.cfi_def_cfa_offset 32
	.cfi_offset 3, -32
	subq	$432, %rsp
	.cfi_def_cfa_offset 464
	movq	%fs:40, %rax
	movq	%rax, 424(%rsp)
	xorl	%eax, %eax
	call	puts
	leaq	12(%rsp), %rsi
	movl	$.LC1, %edi
	xorl	%eax, %eax
	leaq	16(%rsp), %r12
	call	__isoc99_scanf
	movl	12(%rsp), %edx
	movl	$1, %edi
	xorl	%eax, %eax
	movl	$.LC2, %esi
	call	__printf_chk
	movl	12(%rsp), %edi
	testl	%edi, %edi
	jle	.L2
	movq	%r12, %rbx
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L3:
	movq	%rbx, %rsi
	movl	$.LC1, %edi
	xorl	%eax, %eax
	call	__isoc99_scanf
	movl	12(%rsp), %edi
	addl	$1, %ebp
	addq	$4, %rbx
	cmpl	%ebp, %edi
	jg	.L3
.L2:
	leal	-1(%rdi), %r11d
	xorl	%r8d, %r8d
	movq	%r12, %rbx
	movq	%r12, %r10
	cmpl	%r11d, %r8d
	jge	.L23
	.p2align 4,,10
	.p2align 3
.L8:
	leal	1(%r8), %r9d
	cmpl	%edi, %r9d
	jge	.L5
	movl	%r8d, %edx
	movl	%r9d, %eax
	.p2align 4,,10
	.p2align 3
.L7:
	movslq	%edx, %rsi
	movslq	%eax, %rcx
	movl	16(%rsp,%rcx,4), %ecx
	cmpl	%ecx, 16(%rsp,%rsi,4)
	cmovg	%eax, %edx
	addl	$1, %eax
	cmpl	%edi, %eax
	jne	.L7
	cmpl	%edx, %r8d
	je	.L5
	movslq	%edx, %rdx
	movl	(%r10), %eax
	movl	16(%rsp,%rdx,4), %ecx
	movl	%ecx, (%r10)
	movl	%eax, 16(%rsp,%rdx,4)
.L5:
	movl	%r9d, %r8d
	addq	$4, %r10
	cmpl	%r11d, %r8d
	jl	.L8
.L23:
	movl	$.LC3, %edi
	call	puts
	movl	12(%rsp), %eax
	testl	%eax, %eax
	jle	.L10
	xorl	%ebp, %ebp
	.p2align 4,,10
	.p2align 3
.L9:
	movl	(%rbx), %edx
	xorl	%eax, %eax
	movl	$.LC4, %esi
	movl	$1, %edi
	addl	$1, %ebp
	addq	$4, %rbx
	call	__printf_chk
	cmpl	%ebp, 12(%rsp)
	jg	.L9
.L10:
	xorl	%eax, %eax
	movq	424(%rsp), %rbx
	xorq	%fs:40, %rbx
	jne	.L24
	addq	$432, %rsp
	.cfi_remember_state
	.cfi_def_cfa_offset 32
	popq	%rbx
	.cfi_def_cfa_offset 24
	popq	%rbp
	.cfi_def_cfa_offset 16
	popq	%r12
	.cfi_def_cfa_offset 8
	ret
.L24:
	.cfi_restore_state
	call	__stack_chk_fail
	.cfi_endproc
.LFE23:
	.size	main, .-main
	.section	.text.unlikely
.LCOLDE5:
	.section	.text.startup
.LHOTE5:
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
