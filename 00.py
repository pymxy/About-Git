a = [x for x in range(0,101)]
b = [a[x:x+3] for x in range(0,len(a),3)]
print(b)