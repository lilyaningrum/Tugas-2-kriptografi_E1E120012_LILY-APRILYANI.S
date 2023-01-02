s = []
for i in range(256):
    s.append(i)
print("Array S :")
print(s)

print("")
    
plaintext = "2012"
p = bytearray(plaintext, "utf8")

i = 0;
j = 0;
c = ""
for idx in range(len(p)):
    i = (i + 1) % 256
    j = (j + s[i]) % 256
    s[i] , s[j] = s[j], s[i] ## swap

    t = (s[i] + s[j]) % 256
    u = s[t]
    
    c += chr(u ^ p[idx])

print("Plaintext      :", plaintext)
print("Hasil xor pgra : " + c)