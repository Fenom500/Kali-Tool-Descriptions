import bs4 as bs
import urllib.request as uReq

# Get website and run HTML Parser
sauce = uReq.urlopen('https://tools.kali.org/tools-listing')
soup = bs.BeautifulSoup(sauce, "html.parser")
Output_File = open('All Links.txt', 'w')


# Get all sections that have their own focus in the tool type
Sections = soup.find_all('div', class_='wpb_wrapper')

# Temporary line to prototype solely on first section
for working_section in Sections:
    # All titles of sections are stored under h5 tags
    Title = working_section.h5.text
    Output_File.write(str(Title)+'\n')

    # For loop go go through all links
    Link_Array = working_section.find_all('a')
    for link in Link_Array:
        Tool_name = link.text
        Output_File.write(Tool_name + '\n' + '\n')
        # Get the Link from the list and parse each link with BS
        Link = link['href']
        new_sauce = uReq.urlopen(Link)
        new_soup = bs.BeautifulSoup(new_sauce, 'html.parser')

        # Find Description of Tool and write to file
        Goal_Info = new_soup.body.main.find('p')
        Output_File.write(Goal_Info.text + '\n' + '\n' + '\n')
