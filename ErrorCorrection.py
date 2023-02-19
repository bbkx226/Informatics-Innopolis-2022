run=int(input())
total = 0
if(run==1):  # Generate Hammer code - Encoding
    # 2r >= m+r+1 - Positioning redundant bits where the bis can be placed at the position of 2**n
    # m - data bits, r - redundant bits, 2r as redundant bits can be either 0 or 1
    string=input() # 1000011
    data=list(string) # ['1','0','0','0','0','1','1']
    data.reverse()    # ['1','1','0','0','0','0','1']
    power, ch, dataPos, r, buffer = 0, 0, 0, 0, []

    while ((len(string)+r+1)>(pow(2,r))): # Calculating redundant bits required - Step 1
        r += 1

    for i in range((r+len(data))): # Positioning the redundant bits - Step 2
        position=(2**power) # position of redundant bits - 1, 2, 4, 8, 16, ...

        if(position==(i+1)): # Append the redundant bits only when it's on the exact position
            buffer.append(0)
            power += 1

        else: # Else append the data bits into the list
            buffer.append(int(data[dataPos]))
            dataPos += 1

    # buffer - [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]

    for parity in range(0,(len(buffer))): # Calculate the values of each redundant bits - Step 3
        # P1 parity - 3, 5, 7, 9, 11, ... (Order From Right to Left) ['0', '1', '1', '0']
        # P2 parity - 3, 6, 7, 10, 11, ... (Order From Right to Left) ['0', '0', '1', '0', '0']
        # P4 parity - 5-7, 12-15, 20-23, ...
        ph=(2**ch)
        if(ph==(parity+1)):
            start=ph-1
            i, ExOr = start, []

            while(i<len(buffer)): # Append the parity bits in the string to the list to do Exclusive-Or
                block=buffer[i:i+ph]
                ExOr.extend(block)
                i += 2*ph # Jumps to the position of each parity bit

            for z in range(1,len(ExOr)):
                buffer[start]=buffer[start]^ExOr[z]
            ch+=1

    buffer.reverse()
    print(''.join(map(str, buffer)))
    for i in range(len(string)):
        if string[i] == '1':
            total += 2**i
    print(total)

else: # Error detection
    stringHammed=input()
    data=list(stringHammed)
    data.reverse()
    temp, power, ch, r, j, error, buffer, parity_list, buffer_copy, final= 0, 0, 0, 0, 0, 0, [], [], [], []

    for k in range(0,len(data)): # Positioning the redundant bits
        p=(2**power)
        buffer.append(int(data[k]))
        buffer_copy.append(data[k])
        if(p==(k+1)):
            power += 1
            
    for parity in range(0,(len(buffer))): # Calculate the values of each redundant bits
        ph=(2**ch)
        if(ph==(parity+1)):

            start=ph-1
            i, ExOr=start, []

            while(i<len(buffer)):
                block=buffer[i:i+ph]
                ExOr.extend(block)
                i+=2*ph

            for z in range(1,len(ExOr)):
                buffer[start]=buffer[start]^ExOr[z]
            parity_list.append(buffer[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if(error!=0):
        if(buffer_copy[error-1]=='0'):
           buffer_copy[error-1]='1'

        elif(buffer_copy[error-1]=='1'):
            buffer_copy[error-1]='0'
    
    for i in range(1, len(buffer_copy)+1):
        if i & (i - 1) == 0 and i != 0: # 1, 2, 4, 8
            pass
        else:
            final.append(buffer_copy[i-1])
    final.reverse()
    print(''.join(map(str, final)))
    for i in range(len(final)):
        if final[i] == '1':
            total += 2**i
    print(total)