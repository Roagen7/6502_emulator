    .org $8000
start:
    lda #10

    sta $00
    ldx $00
    lda #15

    cpx #11
    bcs sma

    lda #0
    jmp end
    sma:
    lda #1

    end:

    .org $FFFC
    .word start
    .word $0000
