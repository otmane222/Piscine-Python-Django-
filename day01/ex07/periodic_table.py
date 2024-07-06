import sys

def starto():
	html_content = """	<!DOCTYPE html>
	<html lang="en">
	<head>
		<title>Sample HTML Page</title>
		<style>
			* {
				box-sizing: border-box;
				margin: 0;
				padding: 0;
			}
			table {
				border-collapse: collapse;
				text-align: center;
			}
			h4 {
				margin-bottom: 10px;
			}
			li {
				list-style-type: none;
			}
	
			th {
				background-color: #f2f2f2; /* Light gray background for header cells */
			}
	
			tr:nth-child(even) {
				background-color: #df7f7f; /* Alternating row colors */
			}
			tr:nth-child(odd) {
				background-color: #9aa4e9; /* Alternating row colors */
			}
		</style>
	</head>
	<body>
		<table>
			<tr>
	"""
	footer = """
			</tr>
		</table>
	</body>
	</html>
	"""
	i = 0
	with open("periodic_table.txt", "r") as file:
		for line in file:
			elements = line.split(",")
			if i % 10 == 0 and i != 0:
				html_content += f"			</tr>\n"
				html_content += f"			<tr>\n"
			
			if i == 0:
				html_content += f"			<td style='border: 1px solid black; padding:10px'>\n"
			else:
				html_content += f"				<td style='border: 1px solid black; padding:10px'>\n"
			html_content += f"					<h4>{elements[0].split(' ')[0]}</h4>\n"
			html_content += f"						<ul>\n"
			html_content += f"							<li>No {elements[1].split(':')[1]}</li>\n"
			html_content += f"							<li>{elements[2].split(' ')[1].strip()}</li>\n"
			html_content += f"							<li>{elements[3].split(':')[1]}</li>\n"
			html_content += f"							<li>{elements[4].split(':')[1].strip()} electron</li>\n"
			html_content += f"						</ul>\n"
			html_content += f"				</td>\n"
			i += 1
	html_content += footer
	with open("periodic_table.html", "w") as file:
		file.write(html_content)
	# print(html_content)


if __name__ == "__main__":
	starto()