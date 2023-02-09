file = open("in.txt", "r")

lines = ""
for line in file:
    lines += line.strip()

lines = lines.split("<br>")

for i in range(len(lines)):
    lines[i] = lines[i].replace("<table class=\"n\" cellspacing=\"1\"><tbody><tr class=\"header\">", "<tr>")
    lines[i] = lines[i].replace("</tbody></table>", "")
    lines[i] = lines[i].replace("</tr>","")
    lines[i] = lines[i].split("<tr>")
    lines[i] = lines[i][1:]

    for j in range(len(lines[i])):
        lines[i][j] = lines[i][j].replace("</th>", "</td>")
        lines[i][j] = lines[i][j].replace("<th colspan=\"2\" width=\"55px\">", "<td class=\"tiny\">")
        lines[i][j] = lines[i][j].replace("<th colspan=\"2\">", "<td class=\"tiny\">")
        lines[i][j] = lines[i][j].replace("<td class=\"tiny stdwr\">", "<td class=\"tiny\">")
        lines[i][j] = lines[i][j].replace("<td class=\"tiny\">", "")
        lines[i][j] = lines[i][j].replace("<th class=\"tiny\">", "")
        lines[i][j] = lines[i][j].replace("<td rowspan=\"2\">", "")
        lines[i][j] = lines[i][j].replace("<td><a href=\"coursen.php?cid=","")
        lines[i][j] = lines[i][j].replace("\"><img src=\"images/flag.gif\" alt=\"flag\"></a>", "</td>")
        lines[i][j] = lines[i][j].split("</td>")
courses = {}
std = {}
points = {}
times = {}
cont1 = 0
cont = 0
html = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if j == 0:
            for k in range(1, len(lines[i][j]) - 1):
                std[str(cont1)] = lines[i][j][k]
                cont1 += 1
        elif j == 1:
            for k in range(1, len(lines[i][j]) - 1):
                points[str(cont)] = lines[i][j][k]
                cont += 1
        elif j % 2 == 0:
            if i == 0:
                html.append(f"<option value={lines[i][j][0]}>{lines[i][j][0]}</option>")
                courses[str(j)] = lines[i][j][0]
                times[str(j)] = [[],[]]
            for k in range(3, len(lines[i][j]) - 1):
                times[str(j)][0].append(lines[i][j][k].replace("\'",":").replace("\"","."))
        else:
            for k in range(2, len(lines[i][j]) - 1):
                times[str(j - 1)][1].append(lines[i][j][k].replace("\'",":").replace("\"","."))

#print("\n".join(html))
print(str(courses).replace("'","\""))
print(str(points).replace("'","\""))
print(str(std).replace("'","\""))
print(str(times).replace("'","\""))
