def conv_comp2(n, casas):
    n = int(n[1:])
    n = bin(n)[2:]
    
    while (len(n)<casas):
        n = '0' + n
    
    n = n.replace('1', 'x')
    n = n.replace('0', '1')
    n = n.replace('x', '0')
    
    for i in range((casas-1),0,-1):
        if n[i] == '1':
            n = n[:i] + '0' + n[i+1:]
        elif n[i] == '0':
            n = n[:i] + '1' + n[i+1:]
            break
            
    return n

def conv_bin(n, casas):
    if type(n) == int:
        n = str(n)
    if n[0] == '-':
        n = conv_comp2(n, casas)
    else:
        if len(n)> 2:
            if n[1] == 'x':
                n = int(n,casas)
        n = bin(int(n))[2:]
        while (len(n)<casas):
            n = '0' + n
    return n

def bin_float_ieee_754(n):
    if n[0] == '-':
        bin = '1'
        n = n[1:]
    else:
        bin = '0'
    
    offset = 127
    cont = 0
    n = float(n)
    
    while n >= 2:
        cont += 1
        n = n/2

    while n < 1 :
        cont -= 1
        n = n*2

    exp = offset + cont
    
    bin += conv_bin(str(exp),8)
    
    cont = 0
    n = n - 1

    while cont < 23:
        n = n * 2
        bin += str(int(n))
        n = n - int(n)
        cont += 1
    
    return bin

def bin_double_ieee_754(n):
    if n[0] == '-':
        bin = '1'
        n = n[1:]
    else:
        bin = '0'
    
    offset = 1023
    cont = 0
    n = float(n)
    
    while n >= 2:
        cont += 1
        n = n/2

    while n < 1 :
        cont -= 1
        n = n*2

    exp = offset + cont
    
    bin += conv_bin(str(exp),11)
    
    cont = 0
    n = n - 1

    while cont < 52:
        n = n * 2
        bin += str(int(n))
        n = n - int(n)
        cont += 1
    
    return bin

def conv_hex(n,casas):
    n = hex(int(n))[2:]
    while (len(n)<casas):
        n = '0' + n
    return n

def conv_bintohex(n,casas):
    n = hex(int(n, 2))[2:]
    while (len(n)<casas):
        n = '0' + n
    return n

def rbin(reg):
    if reg == '$zero' or reg == '$0' or reg == '$f0':
        return '00000'
    if reg == '$at' or reg == '$1' or reg == '$f1':
        return '00001'
    if reg == '$v0' or reg == '$2' or reg == '$f2':
        return '00010'
    if reg == '$v1' or reg == '$3' or reg == '$f3':
        return '00011'
    if reg == '$a0' or reg == '$4' or reg == '$f4':
        return '00100'
    if reg == '$a1' or reg == '$5' or reg == '$f5':
        return '00101'
    if reg == '$a2' or reg == '$6' or reg == '$f6':
        return '00110'
    if reg == '$a3' or reg == '$7' or reg == '$f7':
        return '00111'
    if reg == '$t0' or reg == '$8' or reg == '$f8':
        return '01000'
    if reg == '$t1' or reg == '$9' or reg == '$f9':
        return '01001'
    if reg == '$t2' or reg == '$10' or reg == '$f10':
        return '01010'
    if reg == '$t3' or reg == '$11' or reg == '$f11':
        return '01011'
    if reg == '$t4' or reg == '$12' or reg == '$f12':
        return '01100'
    if reg == '$t5' or reg == '$13' or reg == '$f13':
        return '01101'
    if reg == '$t6' or reg == '$14' or reg == '$f14':
        return '01110'
    if reg == '$t7' or reg == '$15' or reg == '$f15':
        return '01111'
    if reg == '$s0' or reg == '$16' or reg == '$f16':
        return '10000'
    if reg == '$s1' or reg == '$17' or reg == '$f17':
        return '10001'
    if reg == '$s2' or reg == '$18' or reg == '$f18':
        return '10010'
    if reg == '$s3' or reg == '$19' or reg == '$f19':
        return '10011'
    if reg == '$s4' or reg == '$20' or reg == '$f20':
        return '10100'
    if reg == '$s5' or reg == '$21' or reg == '$f21':
        return '10101'
    if reg == '$s6' or reg == '$22' or reg == '$f22':
        return '10110'
    if reg == '$s7' or reg == '$23' or reg == '$f23':
        return '10111'
    if reg == '$t8' or reg == '$24' or reg == '$f24':
        return '11000'
    if reg == '$t9' or reg == '$25' or reg == '$f25':
        return '11001'
    if reg == '$k0' or reg == '$26' or reg == '$f26':
        return '11010'
    if reg == '$k1' or reg == '$27' or reg == '$f27':
        return '11011'
    if reg == '$gp' or reg == '$28' or reg == '$f28':
        return '11100'
    if reg == '$sp' or reg == '$29' or reg == '$f29':
        return '11101'
    if reg == '$fp' or reg == '$30' or reg == '$f30':
        return '11110'
    if reg == '$fp' or reg == '$31' or reg == '$f31':
        return '11111'

def checar_subinstrução (linha):
    inst = linha
    
    if linha[0] == 'li':
        if linha[2][0] == '-':
            aux = linha[2][1:]
            if int(aux) > 32768:
                return 4
            return 0
        elif linha[2][1] == 'x':
             if int(linha[2],16) >= 65536:
                return 4
        elif int(linha[2]) >= 65536:
                return 4
    
    if linha[0] in ('lb', 'sb', 'lw', 'sw'):
        if len(inst[2]) > 1:
                    if inst[2][1] == 'x':
                        if int(inst[2],16) >= 32768:
                            return 8
                    else:
                        if inst[2][0] == '-':
                            if abs(int(inst[2])) > 32768:
                                return 8
                        else:
                            if int(inst[2]) >= 32768:
                                return 8

    if linha[0] in ('andi', 'xori', 'ori'):
        if not linha[3][1] == 'x':
            if int(linha[3]) < 0:
                return 8
    if linha[0] in ('addi', 'andi', 'ori', 'xori', 'addiu', 'slti'):
        if linha[3][1] == 'x':
            if int(linha[3], 16) >= 65536:
                return 8
        elif abs(int(linha[3])) >= 65536:
                 return 8

    return 0

def opcode(n):
    if n == 'add':
        return '100000'   
    if n == 'sub':
        return '100010'
    if n == 'and':
        return '100100'
    if n == 'or':
        return '100101'
    if n == 'nor':
        return '100111'
    if n == 'xor':
        return '100110'
    if n == 'lw':
        return '100011'
    if n == 'sw':
        return '101011'
    if n == 'j':
        return '000010'
    if n == 'jr':
        return '001000'
    if n == 'jal':
        return '000011'
    if n == 'beq':
        return '000100'
    if n == 'bne':
        return '000101'
    if n == 'slt':
        return '101010'
    if n == 'lui':
        return '001111'
    if n == 'addu':
        return '100001'
    if n == 'subu':
        return '100011'
    if n == 'sll':
        return '000000'
    if n == 'srl':
        return '000010'
    if n == 'addi':
        return '001000'
    if n == 'andi':
        return '001100'
    if n == 'ori':
        return '001101'
    if n == 'xori':
        return '001110'
    if n == 'mult':
        return '011000'
    if n == 'div':
        return '011010'
    if n == 'mfhi':
        return '010000'
    if n == 'mflo':
        return '010010'
    if n == 'bgez':
        return '00001'
    if n == 'bgezal':
        return '10001'
    if n == 'clo':
        return '100001'
    if n == 'srav':
        return '000111'
    if n == 'sra':
        return '000011'
    if n == 'madd':
        return '000000'
    if n == 'msubu':
        return '000101'
    if n == 'jalr':
        return '001001'
    if n == 'addiu':
        return '001001'
    if n == 'lb':
        return '100000'
    if n == 'movn':
        return '001011'
    if n == 'mul':
        return '000010'
    if n == 'sb':
        return '101000'
    if n == 'slti':
        return '001010'
    if n == 'sltu':
        return '101011'
    if n == 'teq':
        return '110100'
    if n in ('add.d', 'sub.d', 'mul.d', 'div.d'):
        return '10001'
    if n in ('add.s', 'sub.s', 'mul.s', 'div.s'):
        return '10000'

def li_addiu(n):
    instbin = '00100100000' + rbin(n[1]) + conv_bin(n[2],16) 
    return [conv_bintohex(instbin,8)]

def li_luiori(n):
    if n[2][1] == 'x':
        aux2 = n[2]
        while not len(aux2) == 10:
            aux2 = aux2[:2] + '0' + aux2[2:]
        aux = aux2[:6]
        i1 = '0011110000000001' + conv_bin(aux,16)
        i2 = '00110100001' + rbin(n[1]) + conv_bin('0x'+aux2[6:],16)
        return [conv_bintohex(i1,8), conv_bintohex(i2,8)]
    if n[2][0] == '-':
        aux3 = conv_comp2(n[2],32)
    else:
        aux3 = conv_bin(n[2],16)
        
    aux2 = hex(int(aux3,2))
    while not len(aux2) == 10:
            aux2 = aux2[:2] + '0' + aux2[2:]
    aux = aux2[:6]
    i1 = '0011110000000001' + conv_bin(aux,16)
    i2 = '00110100001' + rbin(n[1]) + conv_bin('0x'+aux2[6:],16)
    return [conv_bintohex(i1,8), conv_bintohex(i2,8)]

def andiorixori(n):
    if n[3][0] == '-':
        aux = conv_comp2(n[3],16)
        i1 = '3c01ffff'    #lui $at, 0xffffffff
        i2 = '0011010000100001' + aux
        i3 = '000000' + rbin(n[2]) + rbin('$at') + rbin(n[1]) + '00000'+ opcode(n[0][:-1])
        return[i1, conv_bintohex(i2,8), conv_bintohex(i3,8)]
    elif n[3][1] == 'x':
        aux2 = n[3]
        while not len(aux2) == 10:
            aux2 = aux2[:2] + '0' + aux2[2:]
        aux = aux2[:6]
        i1 = '0011110000000001' + conv_bin(aux,16)
        i2 = '0011010000100001' + conv_bin('0x'+aux2[6:],16)
        if n[0] == 'addiu':
            i3 = '000000' + rbin(n[2]) + rbin('$at') + rbin(n[1]) + '00000'+ opcode('addu')
        else: 
            i3 = '000000' + rbin(n[2]) + rbin('$at') + rbin(n[1]) + '00000'+ opcode(n[0][:-1])
        return[conv_bintohex(i1,8), conv_bintohex(i2,8), conv_bintohex(i3,8)]
    
def tipoi(n):
    if n[3][0] == '-':
        aux2 = conv_comp2(n[3],32)
    else:
        aux2 = conv_bin(n[3],16)
    aux2 = hex(int(aux2,2))
    while not len(aux2) == 10:
            aux2 = aux2[:2] + '0' + aux2[2:]
    aux = aux2[:6]
    i1 = '0011110000000001' + conv_bin(aux,16)
    i2 = '0011010000100001' + conv_bin('0x'+aux2[6:],16)
    if n[0] == 'addiu':
        i3 = '000000' + rbin(n[2]) + rbin('$at') + rbin(n[1]) + '00000'+ opcode('addu')
    else: 
        i3 = '000000' + rbin(n[2]) + rbin('$at') + rbin(n[1]) + '00000'+ opcode(n[0][:-1])
    return[conv_bintohex(i1,8), conv_bintohex(i2,8), conv_bintohex(i3,8)]

def loadstore(n, x):
    if not x == 2:
        if x == 0:
            aux2 = n[2]
        elif x == 1:
            aux2 = hex(int(conv_comp2(n[2],32),2)) 
        while not len(aux2) == 10:
            aux2 = aux2[:2] + '0' + aux2[2:]
        aux = aux2[:6]
        aux3 = '0x' + aux2[6:]
        aux = conv_bin(aux,16)
            
        for i in range(15,0,-1):      #Somando 1
            if aux[i] == '1':
                aux = aux[:i] + '0' + aux[i+1:]
            elif aux[i] == '0':
                aux = aux[:i] + '1' + aux[i+1:]
                break
        i1 = '0011110000000001' + aux
        i2 = '00000000001' + rbin(n[3]) + '0000100000100001'
        i3 = opcode(n[0]) + rbin('$at') + rbin(n[1]) + conv_bin(aux3,16)
        return [conv_bintohex(i1,8), conv_bintohex(i2,8), conv_bintohex(i3,8)]
    if x == 2:
        aux4 = n[2]
        aux2 = hex(int(aux4))
        while not len(aux2) == 10:
            aux2 = aux2[:2] + '0' + aux2[2:]
        aux = aux2[:6]
        aux3 = '0x' + aux2[6:]
        aux = conv_bin(aux,16)
        i1 = '0011110000000001' + aux
        i2 = '00000000001' + rbin(n[3]) + '0000100000100001'
        i3 = opcode(n[0]) + rbin('$at') + rbin(n[1]) + conv_bin(aux3,16)
        return [conv_bintohex(i1,8), conv_bintohex(i2,8), conv_bintohex(i3,8)]

def diferencia_instrução(lista,i):
    instbin = ''
    inst = lista[i]
    if inst[0] in ('sub', 'add', 'and', 'or', 'nor','xor','slt', 'addu', 'subu', 'movn', 'sltu'):
        instbin = '000000' + rbin(inst[2]) + rbin(inst[3]) + rbin(inst[1]) + '00000' + opcode(inst[0])

        
    elif inst[0] in ('lw', 'sw', 'lb', 'sb'):
        
        if len(inst[2]) > 1:
            if inst[2][1] == 'x':
                if int(inst[2],16) >= 32768:
                    instbin = loadstore(inst, 0)
                    inst[-1].append(instbin)
                    #print(inst)
                    return
            else:
                if inst[2][0] == '-':
                    if abs(int(inst[2])) > 32768:
                        instbin = loadstore(inst,1)
                        inst[-1].append(instbin)
                        #print(inst)
                        return 
                else:
                    if int(inst[2]) >= 32768:
                        instbin = loadstore(inst,2)
                        inst[-1].append(instbin)
                        #print(inst)
                        return
        instbin = opcode(inst[0]) + rbin(inst[3]) + rbin(inst[1]) + conv_bin(inst[2],16)

    
    elif inst[0] in ('j','jal'):
        palavra = inst[1]
        for procura in range(len(lista)):
            if lista[procura][-1][1] == palavra:
                break
        offset = int((lista[procura][-2])/4)
        instbin = opcode(inst[0]) + conv_bin(offset,26)
        
    elif inst[0] == 'jr':
        instbin = '000000' + rbin(inst[1]) + '000000000000000' + opcode(inst[0])

    elif inst[0] in ('beq', 'bne'):
        palavra = inst[3]
        for procura in range(len(lista)):
            if lista[procura][-1][1] == palavra:
                break
        offset = int(((lista[procura][-2])-(inst[-2]+4))/4)
        instbin = opcode(inst[0])+ rbin(inst[1]) + rbin(inst[2]) + conv_bin(str(offset),16)

        
    elif inst[0] == 'lui':
        instbin = opcode(inst[0])+ '00000' + rbin(inst[1]) + conv_bin(inst[2],16)

    
    elif inst[0] in ('srl', 'sll', 'sra'):
        instbin = '00000000000' + rbin(inst[2]) + rbin(inst[1]) + conv_bin(inst[3],5) + opcode(inst[0])

    elif inst[0] in ('addi', 'andi', 'ori', 'xori', 'addiu', 'slti'):  
         
        if not inst[3][1] == 'x': 
            if inst[0] in ('andi', 'xori', 'ori') and int(inst[3]) < 0:
                if abs(int(inst[3])) < 65536:
                    instbin = andiorixori(inst)
                    inst[-1].append(instbin)
                   #print(inst)
                    return
            if abs(int(inst[3])) >= 65536:
                instbin = tipoi(inst)
                inst[-1].append(instbin)
                #print(inst)
                return
        else:
            if int(inst[3],16) >= 65536:

                instbin = andiorixori(inst)
                inst[-1].append(instbin)
                #print(inst)
                return
        instbin = opcode(inst[0]) + rbin(inst[2]) + rbin(inst[1]) + conv_bin(inst[3],16)

        
    elif inst[0] in ('mult', 'div', 'teq'):
        instbin = '000000' + rbin(inst[1]) + rbin(inst[2]) + '0000000000' + opcode(inst[0])

    elif inst[0] == 'li':
        if inst[2][0] == '-':
            aux = inst[2][1:]
            if int(aux) > 32768:
                instbin = li_luiori(inst)
                inst[-1].append(instbin)
                #print(inst)
                return
        elif inst[2][1] == 'x':
             if int(inst[2],16) >= 65536:
                instbin = li_luiori(inst)
                inst[-1].append(instbin)
                #print(inst)
                return
        elif int(inst[2]) >= 65536:
                instbin = li_luiori(inst)
                inst[-1].append(instbin)
                #print(inst)
                return
        instbin = li_addiu(inst)
        inst[-1].append(instbin)
        #print(inst)
        return
    
    elif inst[0] in ('mfhi', 'mflo'):
        instbin = '0000000000000000' + rbin(inst[1]) + '00000' + opcode(inst[0])

    
    elif inst[0] == 'bgez' or inst[0] == 'bgezal':
        palavra = inst[2]
        for procura in range(len(lista)):
            if lista[procura][-1][1] == palavra:
                break
        offset = int(((lista[procura][-2])-(inst[-2]+4))/4)
        instbin = '000001' + rbin(inst[1]) + opcode(inst[0]) + conv_bin(str(offset),16)

    
    elif inst[0] ==  'clo':
        instbin = '011100' + rbin(inst[2]) + '00000' + rbin(inst[1]) + '00000' + opcode(inst[0])

    
    elif inst[0] == 'srav':
         instbin = '000000' + rbin(inst[3]) + rbin(inst[2]) + rbin(inst[1]) + '00000' + opcode(inst[0])


        
    elif inst[0] in ('madd','msubu'):
        instbin = '011100' + rbin(inst[1])+ rbin(inst[2]) + '0000000000' + opcode(inst[0])

        
    elif inst[0] in ('jalr'):
        instbin = '000000' + rbin(inst[1]) + '000001111100000' + opcode(inst[0])
        
        
    elif inst[0] == 'mul':
        instbin = '011100' + rbin(inst[2]) + rbin(inst[3]) + rbin(inst[1]) + '00000' + opcode(inst[0])

    
    elif inst[0] in ('add.d', 'add.s'):
        instbin = '010001' + opcode(inst[0]) + rbin(inst[3]) + rbin(inst[2]) + rbin(inst[1]) + '000000'

        
    elif inst[0] in ('sub.d', 'sub.s'):
        instbin = '010001' + opcode(inst[0]) + rbin(inst[3]) + rbin(inst[2]) + rbin(inst[1]) + '000001'

        
    elif inst[0] in ('mul.d', 'mul.s'):
        instbin = '010001' + opcode(inst[0]) + rbin(inst[3]) + rbin(inst[2]) + rbin(inst[1]) + '000010'

        
    elif inst[0] in ('div.d', 'div.s'):
        instbin = '010001' + opcode(inst[0]) + rbin(inst[3]) + rbin(inst[2]) + rbin(inst[1]) + '000011'

    
    elif inst[0] == 'c.eq.d':
        instbin = '01000110001' + rbin(inst[2]) + rbin(inst[1]) + '00000110010'

    
    elif inst[0] == 'c.eq.s':
        instbin = '01000110000' + rbin(inst[2]) + rbin(inst[1]) + '00000110010'
    
    inst[-1].append([conv_bintohex(instbin,8)])

def escreve_instruções_arquivo(file_leitura, file_text):  
    file_leitura.seek(0,0) # Começar a ler o arquivo desde o começo para contar o número de linhas

    endereço = 4194304 #0x00400000
    numlinha = 2

    aux = []
    aux2 = []
    lista_de_linhas = []
    while not file_leitura.readline() == '.text\n':
        numlinha+= 1


    linha = file_leitura.readline()
    while not (linha == '' or linha == '.data\n'):     #LEITURA DE TODAS AS LINHAS
        
        if linha == '\n':
            numlinha+=1
            linha = file_leitura.readline()
        else:
            aux2 = linha
            if aux2[-1] == '\n': 
                aux2 = aux2[:-1]
            linha = linha.split()
            for i in range(len(linha)):   
                if linha[i][-1] == ',':         # Retirar as vírgulas
                    linha[i] = linha[i][:-1]
                if linha[i][-1] == ')':         #separar os saltos
                    linha[i] = linha[i][:-1]
                    aux = linha[i]
                    aux = aux.split('(')
                    linha.pop()
                    linha.append(aux[0])
                    linha.append(aux[1])
            
            linha.append(numlinha)
            linha.append(aux2)
            linha.append(endereço)
            linha.append([0,''])
            if linha[0][-1] == ':' :     # Label
                linha[-1].append(1)
                linha[-1].append(linha[0][:-1])
                linha[-1].pop(0)
                linha[-1].pop(0)
                linha.pop(0)
                
                
            endereço += checar_subinstrução(linha)
            
            lista_de_linhas.append(linha)
            #print(linha)
            endereço+=4
            numlinha += 1
            linha = file_leitura.readline()

    for i in range(len(lista_de_linhas)):
        diferencia_instrução(lista_de_linhas, i)

    file_text.write('DEPTH = 4096;\n')
    file_text.write('WIDTH = 32;\n')
    file_text.write('ADDRESS_RADIX = HEX;\n')
    file_text.write('DATA_RADIX = HEX;\n')
    file_text.write('CONTENT\n')
    file_text.write('BEGIN\n\n')

    adress = 0
    adresshex = hex(adress)[2:]
    while len(adresshex) < 8:
        adresshex = '0' + adresshex
    for i in range(len(lista_de_linhas)):
        for j in range(len(lista_de_linhas[i][-1][-1])):
            file_text.write(adresshex + ' : ' +lista_de_linhas[i][-1][-1][j]+';')
            if j == 0:
                file_text.write('  % '+ str(lista_de_linhas[i][-4])+ ': '+lista_de_linhas[i][-3]+' %')
            adress+=1
            adresshex = hex(adress)[2:]
            while len(adresshex) < 8:
                adresshex = '0' + adresshex
            file_text.write('\n')

    file_text.write('\nEND;\n')

def ajuste_memoria(lista_memoria):
    nova_lista = []
    i = 0
    cont_space = 0
    while i < len(lista_memoria):
        if(len(lista_memoria[i])==16):
            if(lista_memoria[i-1]=='00' or lista_memoria[i-1]=='xx'):
                nova_lista.append('00000000') 
            
            nova_lista.append(lista_memoria[i][8:]) 
            nova_lista.append(lista_memoria[i][:8])
            
            i += 1

        elif(lista_memoria[i] == 'yy' or cont_space == 1):
            aux = ''
            cont_space = 1
            while len(aux) < 8:
                if(i < len(lista_memoria) and (len(aux)+len(lista_memoria[i])<=8)):
                    if(lista_memoria[i]=='yy'):
                        aux =  '00' + aux
                    elif(not lista_memoria[i]=='xx'):
                        aux = lista_memoria[i] + aux

                    if(len(aux)==8):
                        cont_space = 0
                    i += 1
                elif(i <len(lista_memoria) and (len(aux)+len(lista_memoria[i])>8)):
                    if(not lista_memoria[i]=='xx'):
                        tam = 8 - len(aux)
                        aux = lista_memoria[i][-tam:] + aux
                        lista_memoria[i]=lista_memoria[i][:-tam]
                else:
                    aux = '00'+ aux
            nova_lista.append(aux) 
        else:
            aux = ''
        
            while len(aux) < 8:
                if( i < len(lista_memoria) and len(aux)== 2 and len(lista_memoria[i])== 4):
                    if(not lista_memoria[i]=='xx'):
                        aux = lista_memoria[i] +'00'+ aux
                    i += 1
                elif(i < len(lista_memoria) and (len(aux)+len(lista_memoria[i])<=8)):
                    if(not lista_memoria[i]=='xx'):
                        aux = lista_memoria[i] + aux
                    i += 1
                else:
                    aux = '00'+ aux
            nova_lista.append(aux)  
    lista_memoria = nova_lista
    return lista_memoria

def tipo_data(lista_linhas):
    lista_memoria = []
    for i in range(len(lista_linhas)):
        if(lista_linhas[i][0] == ".space"):
            for j in range(int(lista_linhas[i][1])):
                lista_memoria.append('yy')

        if(lista_linhas[i][1] == ".space"):
            for j in range(int(lista_linhas[i][2])):
                lista_memoria.append('yy')

        if(lista_linhas[i][1] == ".ascii"):
            aux = []
            for j in range(len(lista_linhas[i])-2):
                for k in range(len(lista_linhas[i][j+2])):
                    num = ord(lista_linhas[i][j+2][k])
                    num = hex(num)[2:]
                    if(num != '22'):
                        aux.append(num)
                aux.append(hex(ord(' '))[2:])
            
            aux.pop()
            aux.append('xx')
            lista_memoria += aux
            
        if(lista_linhas[i][1] == ".asciiz"):
            aux = []
            for j in range(len(lista_linhas[i])-2):
                for k in range(len(lista_linhas[i][j+2])):
                    num = ord(lista_linhas[i][j+2][k])
                    num = hex(num)[2:]
                    if(num != '22'):
                        aux.append(num)
                aux.append(hex(ord(' '))[2:])
            
            aux.pop()
            aux.append('00')
            lista_memoria += aux

        if(lista_linhas[i][1] == ".float"):
            for j in range(len(lista_linhas[i])-2):
                aux = bin_float_ieee_754(lista_linhas[i][j+2])
                lista_memoria.append(conv_bintohex(aux,8))
        
        if(lista_linhas[i][1] == ".double"):
            for j in range(len(lista_linhas[i])-2):
                aux = bin_double_ieee_754(lista_linhas[i][j+2])
                lista_memoria.append(conv_bintohex(aux,16))

        if(lista_linhas[i][1] == ".word"):
            for j in range(len(lista_linhas[i])-2):
                aux = conv_bin(lista_linhas[i][j+2],32)
                lista_memoria.append(conv_bintohex(aux,8))
        
        if(lista_linhas[i][1] == ".half"):
            for j in range(len(lista_linhas[i])-2):
                aux = conv_bin(lista_linhas[i][j+2],16)
                lista_memoria.append(conv_bintohex(aux,4))
        
        if(lista_linhas[i][1] == ".byte"):
            tam = len(lista_linhas[i])-2
            for j in range(tam):
                if(not lista_linhas[i][j+2].isdigit() and not lista_linhas[i][j+2][0] == '-'):
                    lista_linhas[i][j+2] = str(ord(lista_linhas[i][j+2]))
                aux = conv_bin(lista_linhas[i][j+2],8)
                lista_memoria.append(conv_bintohex(aux,2))
    lista_memoria = ajuste_memoria(lista_memoria)
    return lista_memoria

def escreve_memoria_arquivo(file_leitura, file_data):
    file_leitura.seek(0,0) # Começar a ler o arquivo desde o começo para contar o número de linhas
    lista_de_linhas = []

    linha = file_leitura.readline()
    while not linha == '.data\n':
        linha = file_leitura.readline()

    linha = file_leitura.readline()
    while not  linha == '.text\n' and not  linha == '':
        aux = ''
        if (not  linha == '\n') and (not '#' in linha):
            linha = linha.split()

            for i in range(len(linha)):   
                if linha[i][-1] == ',':         
                    linha[i] = linha[i][:-1]
                if linha[i][0] == "'":         
                    aux = linha[i][1:]
                    linha[i] = aux
                if linha[i][-1] == "'": 
                    aux = linha[i][:-1]
                    linha[i] = aux
            
            lista_de_linhas.append(linha)
            # Tipos de datas: .aling/.space, .asciiz, .ascii, .double, .float 

        linha = file_leitura.readline()

    lista_memoria = tipo_data(lista_de_linhas)

    file_data.write('DEPTH = 16384;\n')
    file_data.write('WIDTH = 32;\n')
    file_data.write('ADDRESS_RADIX = HEX;\n')
    file_data.write('DATA_RADIX = HEX;\n')
    file_data.write('CONTENT\n')
    file_data.write('BEGIN\n\n')

    for address in range(len(lista_memoria)):
        address_hex = conv_hex(address,8)
        string = address_hex+' : '+lista_memoria[address]+';\n'
        file_data.write(string)

    file_data.write('\nEND;\n')

arquivo = input("Insira o documento o caminho do arquivo .asm: ")
nome_arquivo = arquivo[0:-4]
cont_barra = -1
for i in range(len(arquivo)):
    if(arquivo[i]=='/' or arquivo[i]=="\\"):
        cont_barra = i

nome_arquivo = nome_arquivo[cont_barra+1:]
file_leitura = open(arquivo, 'r')
file_text = open(nome_arquivo+'_text.mif', 'w')
file_data = open(nome_arquivo+'_data.mif', 'w')

escreve_memoria_arquivo(file_leitura, file_data)
escreve_instruções_arquivo(file_leitura, file_text)

file_leitura.close()
file_text.close()
file_data.close()
