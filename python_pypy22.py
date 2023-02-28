szó_lista=[]
szó=input('Adj meg kis a-val vagy nagy A-val kezdődő szavakat! Az enter gombbal tudsz tovább lépni. ')
if szó.startswith('a') or szó.startswith('A'):
    szó_lista.append(szó)

while szó !='':
    szó=input('Adj meg kis a-val kezdődő szavakat! Az enter gombbal tudsz tovább lépni. ')
    if szó.startswith('a') or szó.startswith('A'):
        szó_lista.append(szó)

print(szó_lista)
print('A program úgy működik hogy bekér szavakat a használótól egy while ciklussal és ha ENTER-t nyom akkor befejezi a kérdezést eközben a program egy listába rakja az a-val kezdődő szavakat. Ezután kiírja a végeredményt. Az elvárt adatok azok amik egy a betűvel kezdődő szavak.')