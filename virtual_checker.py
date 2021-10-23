from os import system
from urllib.request import urlopen

try:
    import wmi

except:
    system("py -m pip install wmi")
    from os import system

try:
    from bs4 import BeautifulSoup

except:
    system("py -m pip install wmi")
    from os import system

virtual_checker = """
						██╗   ██╗██╗██████╗ ████████╗██╗   ██╗ █████╗ ██╗
						██║   ██║██║██╔══██╗╚══██╔══╝██║   ██║██╔══██╗██║
						██║   ██║██║██████╔╝   ██║   ██║   ██║███████║██║
						╚██╗ ██╔╝██║██╔══██╗   ██║   ██║   ██║██╔══██║██║
						 ╚████╔╝ ██║██║  ██║   ██║   ╚██████╔╝██║  ██║███████╗
						  ╚═══╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝\n
						 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗
						██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
						██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
						██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
						╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
						 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
				 				1 > virtual checker		by github.gg/zeloww
				 			2 > list of all real manufacturers"""

def all_manufacturers():
	result = ""
	url = "https://en.wikipedia.org/wiki/List_of_computer_system_manufacturers"

	response = urlopen(url).read()
	soup = BeautifulSoup(response, 'html.parser')

	result += "\nlist of all current computers manufacturers:\n"
	result += soup.find("div", {"class":"div-col"}).text
	result += "\nlist of all computers manufacturers that have ceased production:\n\n"

	data = soup.find("div", {"class":"mw-parser-output"}).find_all("ul")[10].text
	for tag in data.splitlines():
		result += tag.split(" -")[0] + "\n"

	return result

def virtual_check():
	result = ""
	manufacters_list = []
	url = "https://en.wikipedia.org/wiki/List_of_computer_system_manufacturers"

	try:
		response = urlopen(url).read()
		soup = BeautifulSoup(response, 'html.parser')

		result += soup.find("div", {"class":"div-col"}).text.lower()
		data = soup.find("div", {"class":"mw-parser-output"}).find_all("ul")[10].text.lower()

		for tag in data.splitlines():
			result += tag.split(" -")[0] + "\n"

		for line in result.splitlines():
			manufacters_list.append(line)

	except:
		manufacters_list = ['abs computer technologies', 'acer', 'ag neovo', 'alphabet inc.', 'google', 'amiga, inc.', 'acube systems srl', 'hyperion entertainment', 'aigo', 'amd', 'aleutia', 'alienware', 'amax information technologies', 'aopen', 'apple', 'asrock', 'asus', 'avadirect', 'axioo international', 'benq', 'biostar', 'brother industries', 'burroughs corporation', 'corona data systems', 'chassis plans', 'chip pc', 'cisco systems', 'clevo', 'crystal group', 'compal', 'cooler master', 'cyberpowerpc', 'dai-tech', 'data general', 'dell', 'wyse technology', 'dfi', 'digital storm', 'elitegroup computer systems (ecs)', 'eagle computer', 'epson', 'evans & sutherland', 'everex', 'evga', 'falcon northwest', 'fic', 'fujitsu', 'foxconn', 'founder technology', 'gigabyte', 'aorus', 'gopro', 'gradiente', 'groupe bull', 'grundig (parent: arçelik)', 'hasee', 'hcl', 'hewlett packard enterprise', 'cray', 'silicon graphics international', 'hp inc.', 'fortify software', 'hp autonomy', 'compaq', 'digital equipment corporation', 'hisense', 'hitachi', 'htc', 'huawei', 'hyundai', 'ibm', 'intel', 'inventec', 'itautec', 'igel', 'jetta international', 'kohjinsha', 'kontron ag', 'lanix', 'lanner electronics', 'lanslide gaming pcs', 'lenovo', 'medion', 'lg', 'liteon', 'maingear', 'meebox', 'mesh computers', 'microsoft', 'micro-star international', 'micro center', 'myria', 'mitac', 'motion computing', 'monel', 'motorola', 'ncomputing', 'ncr', 'nec', 'nvidia', 'nzxt', 'olidata', 'oracle', 'origin pc', 'panasonic', 'positivo informática', 'puget systems', 'quanta computer', 'rca', 'razer', 'samsung', 'sapphire technology', 'shuttle', 'síragon', 'sony', 'supermicro', 'supernovagaming', 'systemax', 'system76', 't-platforms', 'tabletkiosk', 'tadpole computer', 'tatung', 'toshiba', 'tyan', 'unisys', 'v3 gaming pc', 'vaio', 'velocity micro', 'vestel', 'via technologies', 'viewsonic', 'viglen', 'vizio', 'valve', 'walton group', 'wistron', 'wortmann', 'xiaomi', 'zelybron', 'zoostorm', 'zotac', 'zspace', 'acorn computers', 'alliant computer systems', 'altos computer systems', 'amdahl corporation', 'amstrad', 'apollo computer', 'apricot computers', 'ardent computer', 'ast computers, llc', 'atari corporation', 'bell & howell', 'burroughs', 'celerity computing', 'commodore international', 'compaq', 'compuadd', 'computer automation', 'control data corporation (cdc)', 'convergent technologies', 'convex computer', 'corona data systems', 'cromemco', 'data general', 'datapoint', 'digital equipment corporation', 'durango systems corporation', 'eagle computer', 'eckert–mauchly computer', 'egenera', 'elonex — sells tablets (as of 2011)', 'emcc', 'encore computer', 'english electric', 'emachines', 'escom', 'everex', 'evesham', 'franklin computer corporation', 'gateway', 'general electric', 'gericom', 'gould electronics', 'hewlett-packard', 'honeywell', 'international computers and tabulators (ict)', 'international computers limited (icl)', 'kaypro', 'leading edge', 'leo computers', 'luxor ab', 'magnavox', 'magnuson computer systems', 'maxdata (germany)', 'micron technology', 'mitsubishi electronics', 'mpc (formerly micronpc)', 'multiflow computer', 'next', 'nixdorf computer', 'northgate computer systems', 'osborne computer', 'olivetti', 'packard bell', 'philco-ford', 'philips', 'prime computer', 'processor technology', 'psystar', 'pyramid technology', 'quantex microsystems', 'radio shack', 'rca', 'research machines', 'remington rand', 'sanyo', 'scientific data systems', 'sequent computer systems', 'siemens', 'silicon graphics', 'sinclair research', 'solbourne computer', 'soyo', 'sperry', 'sperry rand', 'stardent', 'stratus computer', 'sun microsystems', 'systems engineering laboratories', "systime computers ltd – once britain's second largest, acquired by control data corporation in 1985, broken up in 1989.", 'tandon corporation', 'tandy corporation', 'tiny computers', 'texas instruments', 'averatec', 'tulip computers', 'vigor gaming (usa)', 'voodoopc', 'vtech', 'walton', 'wang laboratories', 'wipro', 'xerox', 'zenith data systems', 'zeos']

	manufacturer = wmi.WMI().Win32_ComputerSystem()[0].Manufacturer
	print("Your manufacturer is '{}'".format(manufacturer))

	if manufacturer.lower() in manufacters_list:
		return True

	else:
		return False

def main():
	while True:
		system("cls")
		system("color d")
		print(virtual_checker)

		choice = input(">>> ")

		if choice == "1":
			if virtual_check():
				input("\033[32m[+] You aren't a virtual machine!\033[0m")

			else:
				input("\033[31m[-] You are a virtual machine!\033[0m")

		elif choice == "2":
			input(all_manufacturers())

if __name__ == "__main__":
	main()