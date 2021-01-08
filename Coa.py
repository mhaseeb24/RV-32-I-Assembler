
x0 = "00000"
x1 = "00001"
x2 = "00010"
x3 = "00011"
x4 = "00100"
x5 = "00101"
x6 = "00110"
x7 = "00111"
x8 = "01000"
x9 = "01001"
x10 = "01010"
x11 = "01011"
x12 = "01100"
x13 = "01101"
x14 = "01110"
x15 = "01111"
x16 = "10000"
x17 = "10001"
x18 = "10010"
x19 = "10011"
x20 = "10100"
x21 = "10101"
x22 = "10110"
x23= "10111"
x24 = "11000"
x25 = "11001"
x26 = "11010"
x27 = "11011"
x28 = "11100"
x29 = "11101"
x30 = "11110"
x31 = "11111"
print("\n*************************************        ASSEMBLER FOR RISC V 32I INSTRUCTION SET ARCHITECTURE        ********************************                        Designed by: Naiyer Abbas and Mohammad Haseeb")
print("\n\nNOTE: You can use following 37 instructions : add, sub, sll, slt, sltu, sltI, sltuI, xor, srl, sra, or, and, addI, sllI, sltuI, xorI, srlI, sraI, orI, andI, LH, LBU, LHU, LW, SB, SH, SW, LUI, AUIPC, beq, bne, bge, bllu, bgeu, jal ")
print("*****\n\n")
for j in range(1000) :


        #************************************************* R FORMAT ****************************************************

                # ADD FUNCTION

    def add(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "000"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

                            #SUBTRACT FUNCTION

    def sub(a,b,c) :
        opcode = "0110011"
        func7 =  "0100000"
        func3 = "000"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)
        
        # SLL FUNCTION

def sll(a,b,c) :
    opcode = "0110011"
    func7 =  "0000000"
    func3 = "001"
    if a=='x0' :
        rd = "00000"
    elif a=='x1' :
        rd= "00001"

    elif a=='x2' :
        rd = "00010"
    elif a=='x3' :
        rd= "00011"
    elif a == 'x4':
        rd = "00100"

    elif a == 'x5':
        rd = "00101"
    elif a == 'x6':
        rd = "00110"
    elif a == 'x7':
        rd = "00111"

    elif a == 'x8':
        rd = "01000"
    elif a == 'x9':
        rd = "01001"
    elif a == 'x10':
        rd = "01010"

    elif a == 'x11':
        rd = "01011"
    elif a == 'x12':
        rd = "01100"
    elif a == 'x13':
        rd = "01101"

    elif a == 'x14':
        rd = "01110"
    elif a == 'x15':
        rd = "01111"
    elif a == 'x16':
        rd = "10000"

    elif a == 'x17':
        rd = "10001"
    elif a == 'x18':
        rd = "10010"
    elif a == 'x19':
        rd = "10011"

    elif a == 'x20':
        rd = "10100"
    elif a == 'x21':
        rd = "10101"
    elif a == 'x22':
        rd = "10110"

    elif a == 'x23':
        rd = "10111"
    elif a == 'x24':
        rd = "11000"
    elif a == 'x25':
        rd = "11001"
    elif a == 'x26':
        rd = "11010"
    elif a == 'x27':
        rd = "11011"

    elif a == 'x28':
        rd = "11100"
    elif a == 'x29':
        rd = "11101"
    elif a == 'x30':
        rd = "11110"

    elif a == 'x31':
        rd = "11111"
    else:
        print("Error")

    if b=='x0' :
        rs1 = "00000"
    elif b=='x1' :
        rs1= "00001"

    elif b=='x2' :
        rs1 = "00010"
    elif b=='x3' :
        rs1= "00011"
    elif b == 'x4':
        rs1 = "00100"

    elif b == 'x5':
        rs1 = "00101"
    elif b == 'x6':
        rs1 = "00110"
    elif b == 'x7':
        rs1 = "00111"

    elif b == 'x8':
        rs1 = "01000"
    elif b == 'x9':
        rs1 = "01001"
    elif b == 'x10':
        rs1 = "01010"

    elif b == 'x11':
        rs1 = "01011"
    elif b == 'x12':
        rs1 = "01100"
    elif b == 'x13':
        rs1 = "01101"

    elif b == 'x14':
        rs1 = "01110"
    elif b == 'x15':
        rs1 = "01111"
    elif b == 'x16':
        rs1 = "10000"

    elif b == 'x17':
        rs1 = "10001"
    elif b == 'x18':
        rs1 = "10010"
    elif b == 'x19':
        rs1 = "10011"

    elif b == 'x20':
        rs1 = "10100"
    elif b == 'x21':
        rs1 = "10101"
    elif b == 'x22':
        rs1 = "10110"

    elif b == 'x23':
        rs1 = "10111"
    elif b == 'x24':
        rs1 = "11000"
    elif b == 'x25':
        rs1 = "11001"
    elif b == 'x26':
        rs1 = "11010"
    elif b == 'x27':
        rs1 = "11011"

    elif b == 'x28':
        rs1 = "11100"
    elif b == 'x29':
        rs1 = "11101"
    elif b == 'x30':
        rs1 = "11110"

    elif b == 'x31':
        rs1 = "11111"
    else:
        print("Error")

    if c=='x0' :
        rs2 = "00000"
    elif c=='x1' :
        rs2= "00001"

    elif c=='x2' :
        rs2 = "00010"
    elif c=='x3' :
        rs2= "00011"
    elif c == 'x4':
        rs2 = "00100"

    elif c == 'x5':
        rs2 = "00101"
    elif c == 'x6':
        rs2 = "00110"
    elif c == 'x7':
        rs2 = "00111"

    elif c == 'x8':
        rs2 = "01000"
    elif c == 'x9':
        rs2 = "01001"
    elif c == 'x10':
        rs2 = "01010"

    elif c == 'x11':
        rs2 = "01011"
    elif c == 'x12':
        rs2 = "01100"
    elif c == 'x13':
        rs2 = "01101"

    elif c == 'x14':
        rs2 = "01110"
    elif c == 'x15':
        rs2 = "01111"
    elif c == 'x16':
        rs2 = "10000"

    elif c == 'x17':
        rs2 = "10001"
    elif c == 'x18':
        rs2 = "10010"
    elif c == 'x19':
        rs2 = "10011"

    elif c == 'x20':
        rs2 = "10100"
    elif c == 'x21':
        rs2 = "10101"
    elif c == 'x22':
        rs2 = "10110"

    elif c == 'x23':
        rs2 = "10111"
    elif c == 'x24':
        rs2 = "11000"
    elif c == 'x25':
        rs2 = "11001"
    elif c == 'x26':
        rs2 = "11010"
    elif c == 'x27':
        rs2 = "11011"

    elif c == 'x28':
        rs2 = "11100"
    elif c == 'x29':
        rs2 = "11101"
    elif c == 'x30':
        rs2 = "11110"

    elif c == 'x31':
        rs2 = "11111"
    else:
        print("Error")

    print(func7,rs2,rs1,func3,rd,opcode)



                
            # SLT Function

    def slt(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "010"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

                    #sltu function

    def sltu(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "011"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

                    #xor function

    def xor(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "100"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

            #srl function

    def srl(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "101"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

            # sra

    def sra(a,b,c) :
        opcode = "0110011"
        func7 =  "0100000"
        func3 = "101"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

            #or function
    def Or(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "110"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

            #and function

    def And(a,b,c) :
        opcode = "0110011"
        func7 =  "0000000"
        func3 = "111"
        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if c=='x0' :
            rs2 = "00000"
        elif c=='x1' :
            rs2= "00001"

        elif c=='x2' :
            rs2 = "00010"
        elif c=='x3' :
            rs2= "00011"
        elif c == 'x4':
            rs2 = "00100"

        elif c == 'x5':
            rs2 = "00101"
        elif c == 'x6':
            rs2 = "00110"
        elif c == 'x7':
            rs2 = "00111"

        elif c == 'x8':
            rs2 = "01000"
        elif c == 'x9':
            rs2 = "01001"
        elif c == 'x10':
            rs2 = "01010"

        elif c == 'x11':
            rs2 = "01011"
        elif c == 'x12':
            rs2 = "01100"
        elif c == 'x13':
            rs2 = "01101"

        elif c == 'x14':
            rs2 = "01110"
        elif c == 'x15':
            rs2 = "01111"
        elif c == 'x16':
            rs2 = "10000"

        elif c == 'x17':
            rs2 = "10001"
        elif c == 'x18':
            rs2 = "10010"
        elif c == 'x19':
            rs2 = "10011"

        elif c == 'x20':
            rs2 = "10100"
        elif c == 'x21':
            rs2 = "10101"
        elif c == 'x22':
            rs2 = "10110"

        elif c == 'x23':
            rs2 = "10111"
        elif c == 'x24':
            rs2 = "11000"
        elif c == 'x25':
            rs2 = "11001"
        elif c == 'x26':
            rs2 = "11010"
        elif c == 'x27':
            rs2 = "11011"

        elif c == 'x28':
            rs2 = "11100"
        elif c == 'x29':
            rs2 = "11101"
        elif c == 'x30':
            rs2 = "11110"

        elif c == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(func7,rs2,rs1,func3,rd,opcode)

        #****************************************************** I FORMAT INSTRUCTIONS *******************************************************

                    #ADDI FUNCTION
    def addI(a, b, c) :
        opcode = "0010011"
        func3 = "000"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #slli function

    def sllI(a, b, c) :
        opcode = "0010011"
        func3 = "001"
        d = int(c)
        s = format(d, "05b")
        ts = "0000000"
        imm = ts + s

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #slti function
    def sltI(a, b, c) :
        opcode = "0010011"
        func3 = "010"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)



            #sltuI Function

    def sltuI(a, b, c) :
        opcode = "0010011"
        func3 = "011"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #xorI Function

    def xorI(a, b, c) :
        opcode = "0010011"
        func3 = "100"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #srli
    def srlI(a, b, c) :
        opcode = "0010011"
        func3 = "101"
        d = int(c)
        s = format(d,"05b")
        ts = "0000000"
        imm = ts + s

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #srai Function

    def sraI(a, b, c) :
        opcode = "0010011"
        func3 = "101"
        d = int(c)
        s = format(d, "05b")
        ts = "0100000"
        imm = ts + s

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #orI Function
    def orI(a, b, c) :
        opcode = "0010011"
        func3 = "110"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

            #andI Function

    def andI(a, b, c) :
        opcode = "0010011"
        func3 = "111"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)



                    #LOAD INSTRUCTIONS

            #LB FUNCTION
    def LB(a, b, c):
            opcode = "0000011"
            func3 = "000"
            d = int(c)
            imm = format(d, "012b")

            if a == 'x0':
                rd = "00000"
            elif a == 'x1':
                rd = "00001"

            elif a == 'x2':
                rd = "00010"
            elif a == 'x3':
                rd = "00011"
            elif a == 'x4':
                rd = "00100"

            elif a == 'x5':
                rd = "00101"
            elif a == 'x6':
                rd = "00110"
            elif a == 'x7':
                rd = "00111"

            elif a == 'x8':
                rd = "01000"
            elif a == 'x9':
                rd = "01001"
            elif a == 'x10':
                rd = "01010"

            elif a == 'x11':
                rd = "01011"
            elif a == 'x12':
                rd = "01100"
            elif a == 'x13':
                rd = "01101"

            elif a == 'x14':
                rd = "01110"
            elif a == 'x15':
                rd = "01111"
            elif a == 'x16':
                rd = "10000"

            elif a == 'x17':
                rd = "10001"
            elif a == 'x18':
                rd = "10010"
            elif a == 'x19':
                rd = "10011"

            elif a == 'x20':
                rd = "10100"
            elif a == 'x21':
                rd = "10101"
            elif a == 'x22':
                rd = "10110"

            elif a == 'x23':
                rd = "10111"
            elif a == 'x24':
                rd = "11000"
            elif a == 'x25':
                rd = "11001"
            elif a == 'x26':
                rd = "11010"
            elif a == 'x27':
                rd = "11011"

            elif a == 'x28':
                rd = "11100"
            elif a == 'x29':
                rd = "11101"
            elif a == 'x30':
                rd = "11110"

            elif a == 'x31':
                rd = "11111"
            else:
                print("Error")

            if b == 'x0':
                rs1 = "00000"
            elif b == 'x1':
                rs1 = "00001"

            elif b == 'x2':
                rs1 = "00010"
            elif b == 'x3':
                rs1 = "00011"
            elif b == 'x4':
                rs1 = "00100"

            elif b == 'x5':
                rs1 = "00101"
            elif b == 'x6':
                rs1 = "00110"
            elif b == 'x7':
                rs1 = "00111"

            elif b == 'x8':
                rs1 = "01000"
            elif b == 'x9':
                rs1 = "01001"
            elif b == 'x10':
                rs1 = "01010"

            elif b == 'x11':
                rs1 = "01011"
            elif b == 'x12':
                rs1 = "01100"
            elif b == 'x13':
                rs1 = "01101"

            elif b == 'x14':
                rs1 = "01110"
            elif b == 'x15':
                rs1 = "01111"
            elif b == 'x16':
                rs1 = "10000"

            elif b == 'x17':
                rs1 = "10001"
            elif b == 'x18':
                rs1 = "10010"
            elif b == 'x19':
                rs1 = "10011"

            elif b == 'x20':
                rs1 = "10100"
            elif b == 'x21':
                rs1 = "10101"
            elif b == 'x22':
                rs1 = "10110"

            elif b == 'x23':
                rs1 = "10111"
            elif b == 'x24':
                rs1 = "11000"
            elif b == 'x25':
                rs1 = "11001"
            elif b == 'x26':
                rs1 = "11010"
            elif b == 'x27':
                rs1 = "11011"

            elif b == 'x28':
                rs1 = "11100"
            elif b == 'x29':
                rs1 = "11101"
            elif b == 'x30':
                rs1 = "11110"

            elif b == 'x31':
                rs1 = "11111"
            else:
                print("Error")

            print(imm, rs1, func3, rd, opcode)

            #LH FUNCTION
    def LH(a, b, c) :
        opcode = "0000011"
        func3 = "100"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

        #LBU FUNCTION
    def LBU(a, b, c) :
        opcode = "0000011"
        func3 = "001"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

        #LHU FUNCTION

    def LHU(a, b, c) :
        opcode = "0000011"
        func3 = "101"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

        #LW FUNCTION

    def LW(a, b, c) :
        opcode = "0000011"
        func3 = "010"
        d = int(c)
        imm = format(d,"012b")

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs1 = "00000"
        elif b=='x1' :
            rs1= "00001"

        elif b=='x2' :
            rs1 = "00010"
        elif b=='x3' :
            rs1= "00011"
        elif b == 'x4':
            rs1 = "00100"

        elif b == 'x5':
            rs1 = "00101"
        elif b == 'x6':
            rs1 = "00110"
        elif b == 'x7':
            rs1 = "00111"

        elif b == 'x8':
            rs1 = "01000"
        elif b == 'x9':
            rs1 = "01001"
        elif b == 'x10':
            rs1 = "01010"

        elif b == 'x11':
            rs1 = "01011"
        elif b == 'x12':
            rs1 = "01100"
        elif b == 'x13':
            rs1 = "01101"

        elif b == 'x14':
            rs1 = "01110"
        elif b == 'x15':
            rs1 = "01111"
        elif b == 'x16':
            rs1 = "10000"

        elif b == 'x17':
            rs1 = "10001"
        elif b == 'x18':
            rs1 = "10010"
        elif b == 'x19':
            rs1 = "10011"

        elif b == 'x20':
            rs1 = "10100"
        elif b == 'x21':
            rs1 = "10101"
        elif b == 'x22':
            rs1 = "10110"

        elif b == 'x23':
            rs1 = "10111"
        elif b == 'x24':
            rs1 = "11000"
        elif b == 'x25':
            rs1 = "11001"
        elif b == 'x26':
            rs1 = "11010"
        elif b == 'x27':
            rs1 = "11011"

        elif b == 'x28':
            rs1 = "11100"
        elif b == 'x29':
            rs1 = "11101"
        elif b == 'x30':
            rs1 = "11110"

        elif b == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        print(imm, rs1, func3, rd, opcode)

                #****************************************S-Format************************************#
        #SB FUNCTION

    def SB(a, b, c) :
        opcode = "0100011"
        func3 = "000"
        d = int(c)
        imm = format(d,"012b")
        a5 = imm[-5:]
        a7 = imm[-12:-5]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a7, rs2, rs1, func3, a5, opcode)

        # SH FUNCTION

    def SH(a, b, c) :
        opcode = "0100011"
        func3 = "001"
        d = int(c)
        imm = format(d,"012b")
        a5 = imm[-5:]
        a7 = imm[-12:-5]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a7, rs2, rs1, func3, a5, opcode)

        # SW function

    def SW(a, b, c) :
        opcode = "0100011"
        func3 = "010"
        d = int(c)
        imm = format(d,"012b")
        a5 = imm[-5:]
        a7 = imm[-12:-5]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a7, rs2, rs1, func3, a5, opcode)

        #***********************************************    U FORMAT INSTRUCTIONS *************************************************

        #LUI FUNCTION
    def LUI(a, b) :
        opcode = "0110111"
        d = int(b)
        imm = format(d,"032b")
        a20 = imm[:20]

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")


        print(a20, rd, opcode)

            #AUIPC

    def AUIPC(a, b) :
        opcode = "0010111"
        d = int(b)
        imm = format(d,"032b")
        a20 = imm[:20]

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")
        print(a20, rd, opcode)

                #*************************************** SUB FORMAT INSTRUCTIONS ***********************************

            #*********************   SB instrauctions ***********************

            # beq function

    def beq(a, b, c) :
        opcode = "1100011"
        func3 = "000"
        d = int(c)
        imm = format(d,"011b") + "0"
        a12 = imm[0]
        a11 = imm[1]
        a1 = imm[8:13]
        a5 = imm[2:8]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a12, a5, rs2, rs1, func3, a1, a11, opcode)

        #bne

    def bne(a, b, c) :
        opcode = "1100011"
        func3 = "001"
        d = int(c)
        imm = format(d,"011b") + "0"
        a12 = imm[0]
        a11 = imm[1]
        a1 = imm[8:13]
        a5 = imm[2:8]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a12, a5, rs2, rs1, func3, a1, a11, opcode)

        #bge

    def bge(a, b, c) :
        opcode = "1100011"
        func3 = "101"
        d = int(c)
        imm = format(d,"011b") + "0"
        a12 = imm[0]
        a11 = imm[1]
        a1 = imm[8:13]
        a5 = imm[2:8]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a12, a5, rs2, rs1, func3, a1, a11, opcode)

        #bllu

    def bllu(a, b, c) :
        opcode = "1100011"
        func3 = "110"
        d = int(c)
        imm = "0" + format(d,"011b")
        a12 = imm[0]
        a11 = imm[1]
        a1 = imm[8:13]
        a5 = imm[2:8]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a12, a5, rs2, rs1, func3, a1, a11, opcode)

        #bgeu

    def bgeu(a, b, c) :
        opcode = "1100011"
        func3 = "111"
        d = int(c)
        imm = format(d,"011b") + "0"
        a12 = imm[0]
        a11 = imm[1]
        a1 = imm[8:13]
        a5 = imm[2:8]

        if a=='x0' :
            rs1 = "00000"
        elif a=='x1' :
            rs1= "00001"

        elif a=='x2' :
            rs1 = "00010"
        elif a=='x3' :
            rs1= "00011"
        elif a == 'x4':
            rs1 = "00100"

        elif a == 'x5':
            rs1 = "00101"
        elif a == 'x6':
            rs1 = "00110"
        elif a == 'x7':
            rs1 = "00111"

        elif a == 'x8':
            rs1 = "01000"
        elif a == 'x9':
            rs1 = "01001"
        elif a == 'x10':
            rs1 = "01010"

        elif a == 'x11':
            rs1 = "01011"
        elif a == 'x12':
            rs1 = "01100"
        elif a == 'x13':
            rs1 = "01101"

        elif a == 'x14':
            rs1 = "01110"
        elif a == 'x15':
            rs1 = "01111"
        elif a == 'x16':
            rs1 = "10000"

        elif a == 'x17':
            rs1 = "10001"
        elif a == 'x18':
            rs1 = "10010"
        elif a == 'x19':
            rs1 = "10011"

        elif a == 'x20':
            rs1 = "10100"
        elif a == 'x21':
            rs1 = "10101"
        elif a == 'x22':
            rs1 = "10110"

        elif a == 'x23':
            rs1 = "10111"
        elif a == 'x24':
            rs1 = "11000"
        elif a == 'x25':
            rs1 = "11001"
        elif a == 'x26':
            rs1 = "11010"
        elif a == 'x27':
            rs1 = "11011"

        elif a == 'x28':
            rs1 = "11100"
        elif a == 'x29':
            rs1 = "11101"
        elif a == 'x30':
            rs1 = "11110"

        elif a == 'x31':
            rs1 = "11111"
        else:
            print("Error")

        if b=='x0' :
            rs2 = "00000"
        elif b=='x1' :
            rs2= "00001"

        elif b=='x2' :
            rs2 = "00010"
        elif b=='x3' :
            rs2= "00011"
        elif b == 'x4':
            rs2 = "00100"

        elif b == 'x5':
            rs2 = "00101"
        elif b == 'x6':
            rs2 = "00110"
        elif b == 'x7':
            rs2 = "00111"

        elif b == 'x8':
            rs2 = "01000"
        elif b == 'x9':
            rs2 = "01001"
        elif b == 'x10':
            rs2 = "01010"

        elif b == 'x11':
            rs2 = "01011"
        elif b == 'x12':
            rs2 = "01100"
        elif b == 'x13':
            rs2 = "01101"

        elif b == 'x14':
            rs2 = "01110"
        elif b == 'x15':
            rs2 = "01111"
        elif b == 'x16':
            rs2 = "10000"

        elif b == 'x17':
            rs2 = "10001"
        elif b == 'x18':
            rs2 = "10010"
        elif b == 'x19':
            rs2 = "10011"

        elif b == 'x20':
            rs2 = "10100"
        elif b == 'x21':
            rs2 = "10101"
        elif b == 'x22':
            rs2 = "10110"

        elif b == 'x23':
            rs2 = "10111"
        elif b == 'x24':
            rs2 = "11000"
        elif b == 'x25':
            rs2 = "11001"
        elif b == 'x26':
            rs2 = "11010"
        elif b == 'x27':
            rs2 = "11011"

        elif b == 'x28':
            rs2 = "11100"
        elif b == 'x29':
            rs2 = "11101"
        elif b == 'x30':
            rs2 = "11110"

        elif b == 'x31':
            rs2 = "11111"
        else:
            print("Error")

        print(a12, a5, rs2, rs1, func3, a1, a11, opcode)

            # ************************  UJ FORMAT *************************************** #

      # JAL FUNCTION

    def jal(a, b) :
        opcode = "1101111"
        d = int(b)
        imm = format(d,"019b") + "0"
        a20 = imm[0]
        a10 = imm[10:]
        a11 = imm[9]
        a12 = imm[:8]

        if a=='x0' :
            rd = "00000"
        elif a=='x1' :
            rd= "00001"

        elif a=='x2' :
            rd = "00010"
        elif a=='x3' :
            rd= "00011"
        elif a == 'x4':
            rd = "00100"

        elif a == 'x5':
            rd = "00101"
        elif a == 'x6':
            rd = "00110"
        elif a == 'x7':
            rd = "00111"

        elif a == 'x8':
            rd = "01000"
        elif a == 'x9':
            rd = "01001"
        elif a == 'x10':
            rd = "01010"

        elif a == 'x11':
            rd = "01011"
        elif a == 'x12':
            rd = "01100"
        elif a == 'x13':
            rd = "01101"

        elif a == 'x14':
            rd = "01110"
        elif a == 'x15':
            rd = "01111"
        elif a == 'x16':
            rd = "10000"

        elif a == 'x17':
            rd = "10001"
        elif a == 'x18':
            rd = "10010"
        elif a == 'x19':
            rd = "10011"

        elif a == 'x20':
            rd = "10100"
        elif a == 'x21':
            rd = "10101"
        elif a == 'x22':
            rd = "10110"

        elif a == 'x23':
            rd = "10111"
        elif a == 'x24':
            rd = "11000"
        elif a == 'x25':
            rd = "11001"
        elif a == 'x26':
            rd = "11010"
        elif a == 'x27':
            rd = "11011"

        elif a == 'x28':
            rd = "11100"
        elif a == 'x29':
            rd = "11101"
        elif a == 'x30':
            rd = "11110"

        elif a == 'x31':
            rd = "11111"
        else:
            print("Error")
        print(a20, a10,a11,a12, rd, opcode)

        #************************************************ MAIN ************************************************************#


    x, y = input("\nEnter the assembly instruction : ").split()
    z = y.split(',', 3)

    if x == 'add' :
        add(z[0],z[1],z[2])
    elif x=='sub' :
        sub(z[0],z[1],z[2])
    elif x=='sll' :
        sll(z[0],z[1],z[2])
    elif x=='slt' :
        slt(z[0],z[1],z[2])
    elif x=='sltu' :
        sltu(z[0],z[1],z[2])
    elif x=='xor' :
        xor(z[0],z[1],z[2])
    elif x=='srl' :
        srl(z[0],z[1],z[2])
    elif x=='sra' :
        sra(z[0], z[1], z[2])
    elif x=='or' :
        Or(z[0],z[1],z[2])
    elif x=='and' :
        And(z[0], z[1], z[2])
    elif x=='addI' :
        addI(z[0],z[1],z[2])
    elif x=='sllI' :
        sllI(z[0],z[1],z[2])
    elif x=='sltI' :
        sltI(z[0], z[1], z[2])
    elif x=='sltuI' :
        sltuI(z[0], z[1], z[2])
    elif x=='xorI' :
        xorI(z[0], z[1], z[2])
    elif x=='srlI' :
        srlI(z[0], z[1], z[2])
    elif x=='sraI' :
        sraI(z[0], z[1], z[2])
    elif x=='orI' :
        orI(z[0], z[1], z[2])
    elif x=='andI' :
        andI(z[0], z[1], z[2])
    elif x=='LH' :
        LH(z[0], z[1], z[2])
    elif x=='LBU' :
        LBU(z[0], z[1], z[2])
    elif x=='LHU' :
        LHU(z[0], z[1], z[2])
    elif x=='LW' :
        LW(z[0], z[1], z[2])
    elif x=='SB' :
        SB(z[0], z[1], z[2])
    elif x=='SH' :
        SH(z[0], z[1], z[2])
    elif x=='SW' :
        SW(z[0], z[1], z[2])
    elif x=='LUI' :
        LUI(z[0], z[1])
    elif x=='AUIPC' :
        AUIPC(z[0],z[1])
    elif x=='beq' :
        beq(z[0],z[1],z[2])
    elif x=='bne' :
        bne(z[0],z[1],z[2])
    elif x=='bge' :
        bge(z[0],z[1],z[2])
    elif x=='bllu' :
        bllu(z[0], z[1], z[2])
    elif x=='bgeu' :
        bgeu(z[0], z[1], z[2])
    elif x=='jal' :
        jal(z[0],z[1])
    else :
        "You have entered a wrong instruction or the instruction does not belong to RISC V 32I ISA!"

    t = input("Press 'y' to give next instruction. press 'n' to exit : ")
    if t == 'n':
        break






















