    .org $8000
start:

    lda #69
    sta $4000
    inc $4000

    .org $FFFC
    .word start
    .word $0000
