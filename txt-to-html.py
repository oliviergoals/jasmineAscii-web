file1 = open("art.txt","r")
file2 = open("art-final.txt","w")
file3 = open("art-final-two.txt","w")

lines = file1.readlines()
print(lines)

for i in lines:
    file3.write(i)
    line = "<pre>" + i[0:-2] + "</pre>" + "<br></br>"
    line = line.replace("A","<p style={{fontWeight:'100'}}>~</p>")
    line = line.replace("B","<p style={{fontWeight:'300'}}>~</p>")
    line = line.replace("C","<p style={{fontWeight:'500'}}>~</p>")
    line = line.replace("D","<p style={{fontWeight:'700'}}>~</p>")
    new_line = line.replace("E","<p style={{fontWeight:'900'}}>~</p>")
    file2.write(new_line)

file1.close()
file2.close()
file3.close()